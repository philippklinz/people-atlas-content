# Künstler:innen: Ausbau und Evidenzvermerk

Stand: 2026-11-27. Die Datei `people/expansion-artists.json` enthält 40 neue Personen, 57 datierte Werke beziehungsweise Beiträge und 81 Quellenverweise. Die deutschen und englischen Kurzbiografien umfassen jeweils 40–65 Wörter. Alle Texte wurden eigenständig formuliert; keine Porträts, Liedtexte oder fremden Abbildungen wurden übernommen.

Die Auswahl erweitert bildende Kunst, Musik und Tanz. Sie enthält 16 Künstlerinnen, darunter Komponistinnen und Interpretinnen. Künstlerinnen werden nicht allein aufgrund ihres Geschlechts der Auswahl „Frauen in Wissenschaft und Forschung“ zugeordnet. Der Bestand ist ein erster Ausbau und erhebt keinen Anspruch auf Vollständigkeit.

## Prüfung und Grenzen

- Alle 40 Datensätze bestehen die Personenschema-Prüfung mit `Draft202012Validator` und `FormatChecker`.
- Der Abgleich mit sämtlichen vorhandenen `people/*.json` ergab keine kollidierenden IDs dieser Sammlung.
- `python3 tools/check.py` wurde ausgeführt. Der Gesamtlauf stoppt derzeit mit `Stale source fingerprint: reconcile translations, then update i18n-status.json`. Die Integration von Katalog und Übersetzungsstatus liegt bei der koordinierenden Instanz; diese Dateien wurden hier nicht bearbeitet.
- Die Quellenprüfung erfolgte anhand tatsächlich abgerufener Museums-, Archiv-, Verlags- und Forschungsseiten beziehungsweise ihrer indexierten Textauszüge. Bei einigen Seiten verhindern JavaScript oder Zugriffssperren einen vollständigen Direktabruf; die verwendeten Sachangaben waren in den Rechercheauszügen lesbar. Beim ägyptischen PDF wurde der indexierte Absatz zur Geburtsdatierung konsultiert; der vollständige PDF-Abruf scheiterte an der Dateigröße.
- Eine unabhängige historische und sprachliche Zweitprüfung steht aus. Schema-Prüfung und Quellenabgleich ersetzen sie nicht. Eine abschließende Ansicht der integrierten Sammlung im Atlas erfolgt durch die koordinierende Instanz.

## Evidenz pro ID

Die Nummern S1–S3 beziehen sich je Zeile auf die Quellenreihenfolge im Datensatz. Zugriffstag sämtlicher unten aufgeführter Quellen: 2026-11-27.

| ID | Evidenz und Datierungsentscheidung | Quellen |
| --- | --- | --- |
| `michelangelo` | Lebensdaten und Deckengemälde: S1; Entstehungszeitraum, kein Einzeljahr. | [S1](https://www.nationalgallery.org.uk/artists/michelangelo) |
| `raphael` | Lebensdaten und beide römischen Aufgaben: S1. | [S1](https://www.nationalgallery.org.uk/artists/raphael) |
| `albrecht-durer` | Lebensdaten und Apokalypse: S1; Melencolia I zusätzlich S2. | [S1](https://www.metmuseum.org/de/essays/albrecht-durer-1471-1528) · [S2](https://www.metmuseum.org/art/collection/search/336228) |
| `artemisia-gentileschi` | S1: Tod ausdrücklich unbekannt; letzter Beleg August 1654. | [S1](https://www.nationalgallery.org.uk/artists/artemisia-gentileschi) |
| `rembrandt` | Lebensdaten: S1; Vollendung der Nachtwache, nicht Auftragsbeginn: S2. | [S1](https://www.nationalgallery.org.uk/artists/rembrandt) · [S2](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch) |
| `johannes-vermeer` | Lebensdaten: S1; datiertes Frühwerk: S2. Keine gesicherte Camera-obscura-Nutzung behauptet. | [S1](https://www.nationalgallery.org.uk/artists/johannes-vermeer) · [S2](https://www.metmuseum.org/de/essays/johannes-vermeer-1632-1675) |
| `diego-velazquez` | Lebensdaten: S1; Porträt in S2 ausdrücklich ungefähr datiert. | [S1](https://www.nationalgallery.org.uk/artists/diego-velazquez) · [S2](https://www.nationalgallery.org.uk/paintings/diego-velazquez-philip-iv-of-spain) |
| `francisco-goya` | S1 belegt Lebensdaten, Taubheit und Veröffentlichung der Caprichos. | [S1](https://www.metmuseum.org/ja/essays/francisco-de-goya-1746-1828-and-the-spanish-enlightenment) |
| `katsushika-hokusai` | Lebensdaten und ungefähre Blattdatierung: S1; Druck- und Pigmentkontext: S2. | [S1](https://www.metmuseum.org/art/collection/search/36491?searchField=All&showOnly=openAccess) · [S2](https://www.metmuseum.org/ja/essays/hokusai-great-wave) |
| `utagawa-hiroshige` | Beide Museumsobjekte belegen Künstlerdaten und die jeweiligen Blattdatierungen. | [S1](https://www.metmuseum.org/art/collection/search/55433?searchField=All&showOnly=openAccess) · [S2](https://www.metmuseum.org/art/collection/search/36545) |
| `shen-zhou` | Lebensdaten und Werk: S1; biografischer Kontext: S2. | [S1](https://www.metmuseum.org/art/collection/search/49549) · [S2](https://www.metmuseum.org/art/collection/search/39556) |
| `zhao-mengfu` | S1: Künstlerdaten und ungefähre Werkdatierung; kein exaktes Jahr suggeriert. | [S1](https://www.metmuseum.org/art/collection/search/40508) |
| `claude-monet` | S1 belegt Lebensdaten, Werk und Ausstellungsteilnahme. | [S1](https://www.nationalgallery.org.uk/artists/claude-monet) |
| `vincent-van-gogh` | Biografie und Lebensdaten: S1; konkrete Londoner Sonnenblumen-Fassung: S2. | [S1](https://www.vangoghmuseum.nl/en/art-and-stories/art/vincent-van-gogh) · [S2](https://www.nationalgallery.org.uk/paintings/vincent-van-gogh-sunflowers) |
| `paul-cezanne` | Lebensdaten und Kontext: S1; konkrete Kartenspieler-Fassung: S2. | [S1](https://www.metmuseum.org/pt/essays/paul-cezanne-1839-1906) · [S2](https://www.metmuseum.org/art/collection/search/435868) |
| `henri-matisse` | Lebensdaten: S1; Studie statt endgültiger Tanz-Auftrag: S2; Jazz: S3. | [S1](https://www.moma.org/artists/3832-henri-matisse) · [S2](https://www.moma.org/collection/works/79124/) · [S3](https://www.moma.org/collection/works/105387) |
| `pablo-picasso` | Lebensdaten: S1; Werkjahr und koloniale Vermittlungswege: S2; Kontext: S3. | [S1](https://www.moma.org/artists/4609-pablo-picasso) · [S2](https://www.moma.org/collection/works/79766?package_id=PS&page=1&sov_referrer=package) · [S3](https://www.moma.org/calendar/galleries/5696) |
| `wassily-kandinsky` | S1 belegt Lebensdaten, Künstlerkreis und Komposition 8. | [S1](https://www.guggenheim.org/teaching-materials/selections-from-the-permanent-collection/vasily-kandinsky-1866-1944-composition-8-komposition-8) |
| `piet-mondrian` | Künstlerdaten und Werkzeitraum: S1; New Yorker Kontext: S2. | [S1](https://www.moma.org/collection/works/78682) · [S2](https://www.moma.org/slideshows/207/2604) |
| `gustav-klimt` | Lebensdaten: S1/S2. Highlight nennt Ausstellung, nicht umstrittenen Entstehungsbeginn. | [S1](https://www.belvedere.at/en/stories/who-was-gustav-klimt) · [S2](https://sammlung.belvedere.at/objects/6678/der-kuss-liebespaar) |
| `frida-kahlo` | Lebensdaten und beide Werke: S1; spätere Spiegelmontage: S2. | [S1](https://www.moma.org/collection/artists/2963) · [S2](https://www.moma.org/collection/works/79374?page=1) |
| `diego-rivera` | Lebensdaten und Freskenzeitraum: S1; Produktions- und Arbeitskontext: S2. | [S1](https://dia.org/collection/detroit-industry-murals/58537) · [S2](https://dia.org/riveracourt) |
| `georgia-okeeffe` | Lebensdaten und Summer Days: S1; Jimson Weed: S2. | [S1](https://whitney.org/artists/962) · [S2](https://access-ok.okeeffemuseum.org/object/1/) |
| `kathe-kollwitz` | Lebensdaten und Biografie: S1; Publikationsjahr, nicht Gesamtentstehungszeit: S2. | [S1](https://allenartcollection.oberlin.edu/people/4037/kathe-kollwitz/objects) · [S2](https://kollwitz.de/collection/peasants-war) |
| `berthe-morisot` | Lebensdaten: S1; Werk und Ausstellung: S2; institutioneller Geschlechterkontext: S3. | [S1](https://www.musee-orsay.fr/fr/ressources/repertoire-artistes-personnalites/berthe-morisot-18682) · [S2](https://www.musee-orsay.fr/fr/oeuvres/le-berceau-1132) · [S3](https://www.culture.gouv.fr/thematiques/musees/Les-musees-en-France/les-collections-des-musees-de-france/decouvrir-les-collections/les-femmes-artistes-sortent-de-leur-reserve/icones/Morisot-Berthe) |
| `hilma-af-klint` | Lebensdaten: S1; Tempelserie: S2; unterstützte Großformate: S3. Spiritualismus als Überzeugung. | [S1](https://guide.modernamuseet.se/stockholm/en/collection/hilma-af-klint/) · [S2](https://www.guggenheim.org/exhibition/hilma-af-klint?mod=article_inline) · [S3](https://www.guggenheim-bilbao.eus/en/exhibition/the-ten-largest-1907) |
| `amrita-sher-gil` | Lebensdaten und Ausbildung: S1; Red Verandah: S2. | [S1](https://ngmaindia.gov.in/ngma_mumbai_vg-amritasher-gil.asp) · [S2](https://ngmaindia.gov.in/virtual-tour-of-amrita-sher-gil.asp) |
| `raja-ravi-varma` | S1: Lebensdaten, Druckpraxis und katalogisierte Oleografie; kein Gemäldejahr unterstellt. | [S1](https://www.ngmaindia.gov.in/virtual-tour-of-raja-ravi-varma.asp) |
| `augusta-savage` | Lebensdaten/Biografie: S1; Gamin: S2; Weltausstellungsplastik: S3. | [S1](https://americanart.si.edu/artist/augusta-savage-4269) · [S2](https://americanart.si.edu/education/oh-freedom/augusta-savage) · [S3](https://www.si.edu/object/nmaahc_2010.66.112) |
| `lygia-clark` | Lebensdaten und Manifest: S1; bewegliches Objekt: S2. | [S1](https://www.moma.org/collection/artists/27445) · [S2](https://www.moma.org/audio/playlist/181/2403) |
| `mary-cassatt` | Lebensdaten und Salon: S1; Weltausstellungsmural: S2. | [S1](https://www.metmuseum.org/it/essays/mary-stevenson-cassatt-1844-1926) · [S2](https://www.moma.org/collection/artists/1016) |
| `johann-sebastian-bach` | Lebensdaten und Ämter: S1; Konzertjahr zusätzlich S2. Keine überholten Passionsdatierungen übernommen. | [S1](https://www.deutsche-biographie.de/pnd11850553X.html) · [S2](https://catalogue.bnf.fr/ark%3A/12148/cb13909433c) |
| `wolfgang-amadeus-mozart` | Lebensdaten: S1; Uraufführung: S2; Textautor: S3. | [S1](https://mozarteum.at/wolfgang-amade-mozart) · [S2](https://kv.mozarteum.at/de/work/die-zauberflote-7137) · [S3](https://dme.mozarteum.at/DME/libretti-catalog/liste.php?id=896) |
| `ludwig-van-beethoven` | Lebensdaten: S1; Uraufführung und Hörverlust: S2; Ausbildung: S3. | [S1](https://www.beethoven.de/de/de/beethoven) · [S2](https://www.beethoven.de/de/g/zeittafel-beethoven-in-wien) · [S3](https://www.beethoven.de/de/g/zeittafel-beethoven-in-bonn) |
| `clara-schumann` | Lebensdaten und berufliche Biografie: S1; eigenes Konzert und Premiere: S2. | [S1](https://www.deutsche-biographie.de/gnd11861164X.html) · [S2](https://www.breitkopf.com/work/20680/klavierkonzert-a-moll-op.-7) |
| `fanny-hensel` | Lebensdaten, Konzerte und Veröffentlichungen: S1; Klavierzyklus: S2. | [S1](https://www.mendelssohn-gesellschaft.de/mendelssohns/biografien/fanny-hensel) · [S2](https://www.mendelssohn-stiftung.de/de/fannyjahr) |
| `billie-holiday` | Lebensdaten, Interpretation und Aufnahme: S1; Recording Registry bestätigt S2. | [S1](https://music.si.edu/object-day/billie-holidays-strange-fruit-1939) · [S2](https://www.loc.gov/programs/national-recording-preservation-board/recording-registry/descriptions-and-essays/african-americans-on-the-recording-registry/) |
| `nina-simone` | Lebensdaten und Protestkontext: S1; datierter Tonträger: S2. | [S1](https://nmaahc.si.edu/nina-simone) · [S2](https://nmaahc.si.edu/object/nmaahc_2011.132.9ab?destination=%2Fexplore%2Fcollection%2Fsearch%3Fedan_fq%255B0%255D%3Dset_name%253A%2522Musical%2520Crossroads%2522%26page%3D1) |
| `martha-graham` | Lebensdaten/Kompanie: S1; kollaborative Produktion/Premiere: S2; Chronik: S3. | [S1](https://marthagraham.org/epk/) · [S2](https://marthagraham.org/2021-joyce-program/) · [S3](https://www.loc.gov/collections/martha-graham/articles-and-essays/timeline/) |
| `umm-kulthum` | S1 nennt 1898, S2 diskutiert 1898/1904; Aufnahmejahr und Mitwirkende: S3. | [S1](https://sis.gov.eg/en/egypt/egyptian-figures/umm-kolthoum/) · [S2](https://www.fineart.gov.eg/AllPics/Catalogs/PDF/400/EGYPT-VOICE.pdf) · [S3](https://mediatheque.philharmoniedeparis.fr/mediatheque/doc/ALOES/1081317/oum-kalsoum-anta-oumri-enta-omri-tu-es-ma-vie-mohammed-ab-el-wahhab-composition?_lg=fr-FR) |

## Nächster Ausbau

Die Auswahl bleibt stark von europäischen und nordamerikanischen Sammlungen geprägt. Für eine weitere Recherche sind insbesondere mehr afrikanische, südostasiatische, indigene amerikanische und pazifische Künstler:innen erforderlich. Auch Architektur, Film, Fotografie, Kunsthandwerk, Theater sowie vorneuzeitliche Musik sind bislang zu schmal vertreten.

Als unbestätigte Recherchekandidat:innen vorgemerkt: Ben Enwonwu, Gerard Sekoto, Tarsila do Amaral, Tōyō Sesshū, Pan Yuliang, Yayoi Kusama, Emily Kame Kngwarreye, Nam June Paik, Satyajit Ray, Akira Kurosawa, Ousmane Sembène, Bessie Smith, Chiquinha Gonzaga, M. S. Subbulakshmi, Lili Boulanger und Isadora Duncan. Vor einer Aufnahme müssen Lebensdaten, Werkdatierungen, Kategorien und Quellen neu geprüft werden; lebende Personen benötigen einen ausdrücklich aktuellen Status.

Für spätere längere Biografien: Werkzusammenhänge und Auftraggeber:innen ausführlicher darstellen, institutionelle Ausschlüsse und Zusammenarbeit stärker belegen, Rezeption von zeitgenössischer Tätigkeit trennen und weitere eigenständige Quellen pro Person ergänzen. Für öffentliche Kontroversen oder sensible biografische Angaben sind gezielte Belege und eine eigene redaktionelle Prüfung erforderlich.
