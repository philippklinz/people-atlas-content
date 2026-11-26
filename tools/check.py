#!/usr/bin/env python3
"""Dependency-free contract checks. No network requests or historical verification."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(ok, message):
    if not ok: errors.append(message)
def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))
def text(value):
    return isinstance(value, str) and bool(value.strip())
def localized(value):
    return isinstance(value, dict) and all(text(value.get(k)) for k in ['en','de'])
def year(value):
    return type(value) is int and -10000 <= value <= 2200 and value != 0
def date(value):
    if not isinstance(value, dict): return False
    precision=value.get('precision')
    if precision=='unknown': return set(value)=={'precision'}
    if precision in ['year','approximate']: return set(value)=={'precision','year'} and year(value['year'])
    if precision=='range': return set(value)=={'precision','earliest','latest'} and year(value['earliest']) and year(value['latest']) and value['earliest']<=value['latest']
    return False
def bounds(value):
    if not value or value.get('precision')=='unknown': return None
    return (value['earliest'],value['latest']) if value['precision']=='range' else (value['year'],value['year'])
def path_ok(value):
    return text(value) and not value.startswith('/') and not re.search(r'[:\\?#%]',value) and all(part not in ['.','..',''] for part in value.split('/'))
def url_ok(value):
    if not text(value): return False
    parsed=urlparse(value)
    return parsed.scheme=='https' and bool(parsed.netloc) and not parsed.username and not parsed.password
def source_projection(value):
    if isinstance(value,dict):
        if 'en' in value and 'de' in value: return value['en']
        return {k:source_projection(v) for k,v in value.items()}
    if isinstance(value,list): return [source_projection(v) for v in value]
    return value
def source_hash(catalog,categories,people):
    data=source_projection({'catalog':catalog,'categories':categories,'people':people})
    return hashlib.sha256(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    catalog=load('catalog.json')
    check(catalog.get('schemaVersion')=='1.0.0','Unsupported schema version')
    check(localized(catalog.get('title')),'Catalogue translations')
    check(catalog.get('languages')==['de','en'],'Unexpected complete editions')
    check(re.fullmatch(r'\d{4}-\d{2}-\d{2}',catalog.get('updated','')),'Catalogue date')
    paths=[catalog['categories'],*catalog['collections']]
    check(len(paths)==len(set(paths)),'Duplicate content path')
    for path in paths: check(path_ok(path),'Invalid content path: '+path)
    if errors: raise ValueError('\n'.join(errors))
    categories=load(catalog['categories'])
    people=[p for path in catalog['collections'] for p in load(path)]
    category_ids={c['id'] for c in categories}
    check(len(category_ids)==len(categories),'Duplicate category IDs')
    icons={'science','mathematics','physics','nature','computing','philosophy','invention','politics','art','literature'}
    for c in categories:
        check(re.fullmatch(r'[a-z][a-z0-9-]{1,79}',c['id']), 'Invalid category ID: '+c['id'])
        check(localized(c.get('name')) and localized(c.get('description')),'Category translations: '+c['id'])
        check(c.get('icon') in icons,'Invalid icon: '+c['id'])
        check(not c.get('parent') or c['parent'] in category_ids,'Unknown category parent')
        visited={c['id']};parent=c.get('parent')
        while parent and parent in category_ids:
            if parent in visited: errors.append('Category cycle: '+c['id']);break
            visited.add(parent);parent=next(x for x in categories if x['id']==parent).get('parent')
    person_ids=set()
    for p in people:
        id=p['id']
        check(re.fullmatch(r'[a-z][a-z0-9-]{1,79}',id) and id not in person_ids,'Invalid/duplicate person: '+id)
        person_ids.add(id)
        check(text(p.get('name')) and isinstance(p.get('aliases'),list) and all(text(x) for x in p['aliases']),'Names: '+id)
        check(localized(p.get('summary')) and localized(p.get('biography')),'Person translations: '+id)
        check(p.get('categories') and len(p['categories'])==len(set(p['categories'])) and set(p['categories'])<=category_ids,'Category references: '+id)
        check(p.get('status') in ['living','deceased','unknown'],'Life status: '+id)
        check(date(p.get('birth')) and (p.get('death') is None if p.get('status')=='living' else date(p.get('death'))),'Life dates: '+id)
        if date(p.get('birth')) and (p.get('death') is None or date(p['death'])):
            birth=bounds(p['birth']);death=bounds(p.get('death'))
            check(not birth or not death or birth[0]<=death[1],'Reversed lifespan: '+id)
        check(isinstance(p.get('highlights'),list),'Highlights: '+id)
        for h in p.get('highlights',[]): check(date(h.get('date')) and localized(h.get('text')),'Highlight: '+id)
        check(isinstance(p.get('sources'),list) and p['sources'],'Missing sources: '+id)
        for source in p.get('sources',[]): check(text(source.get('title')) and url_ok(source.get('url')),'Source: '+id)
        if 'dateNote' in p: check(localized(p['dateNote']),'Date note: '+id)
        if 'portrait' in p:
            image=p['portrait']
            check(path_ok(image.get('path')) and (ROOT/image['path']).is_file(),'Missing portrait: '+id)
            check(localized(image.get('alt')) and text(image.get('credit')) and text(image.get('license')),'Portrait attribution: '+id)
            check(url_ok(image.get('source')) and url_ok(image.get('licenseUrl')),'Portrait source/license: '+id)
    check(set(catalog.get('featured',[]))<=person_ids,'Unknown featured ID')
    fingerprint=source_hash(catalog,categories,people)
    if '--source-hash' in sys.argv:
        print(fingerprint);return
    status=load('i18n-status.json')
    check(status.get('sourceSha256')==fingerprint,'Stale source fingerprint: reconcile translations, then update i18n-status.json')
    if errors: raise ValueError('\n'.join(errors))
    print('PASS: '+str(len(people))+' people, '+str(len(categories))+' categories; references, dates, translations and local assets.')
    print('Historical accuracy and independent language review are not certified by this check.')

if __name__=='__main__':
    try: main()
    except (ValueError,KeyError,TypeError,OSError) as error:
        print('FAIL:',error,file=sys.stderr);sys.exit(1)
