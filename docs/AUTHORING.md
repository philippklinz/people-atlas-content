# Authoring a person

1. Choose a permanent lowercase slug, independent of translated names.
2. Add a record to an existing people collection, or add a new collection path to catalog.json.
3. Provide canonical name, aliases, category IDs, life dates, status, English/German summary and biography, highlights and at least one relevant source.
4. Use known years, approximate years, source-backed ranges or unknown dates as appropriate. Never insert year zero or a guessed endpoint for visual convenience.
5. Add a local portrait only when its origin and reuse terms can be documented. Record creator, source page, license, license URL and translated alt text. A missing portrait is valid.
6. Run python3 tools/check.py. Inspect the result in the engine, including its category combination, time range, person URL and both languages.
7. Update catalog.updated and reconcile i18n-status.json source fingerprints after reviewing translation changes.

## Date examples

    {"year": 370, "precision": "approximate"}
    {"earliest": 350, "latest": 370, "precision": "range"}
    {"precision": "unknown"}

The range describes the uncertainty of one endpoint, not a lifespan. Do not manufacture bounds for an approximate date. A person whose birth or death is unknown remains visible in the list but has no invented timeline bar.

A deceased person has a death date object (possibly unknown). A living person has status=living and death=null. Unknown life status is separate from living status.

## Sources and wording

Use institutional biographies, scholarly reference works, archives, museums or primary records where available. Sources must support the actual claims and dates. Distinguish original contributions from broad contextual statements; avoid unsupported priority claims.

Write concise original summaries. Keep external source titles as published, even when the surrounding UI is translated. Cite important disagreements in dateNote and add sources for both readings where appropriate.

## Categories

A person can have several category IDs. Scientists includes its descendants automatically, so assigning scientists in addition to mathematicians is unnecessary. All category IDs are data; adding a category must not require engine code changes. Icon choices are part of the schema's visual vocabulary.

## Language maintenance

English is the translation source. Reconcile German text when the English original changes, keeping dates, names, qualifications and evidence intact. The 22 planned EU editions are not published as completed translations. Track source fingerprints and review status honestly.
