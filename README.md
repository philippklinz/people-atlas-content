# People Atlas content

A growing curated collection of 413 people and 12 overlapping categories, from antiquity to the modern era. Each entry includes an original German/English biography, life dates, works or contributions, category memberships and external sources. Portraits are included where attribution and reuse terms have been recorded.

The collection is read by [people-atlas-engine](https://github.com/philippklinz/people-atlas-engine), but has no dependency on the engine's rendering code.

## Files

- catalog.json: version, languages, collection paths and featured records.
- categories.json: category definitions and the scientific category hierarchy.
- people/: biography collections.
- assets/portraits/: local images with attribution in each person's record.
- schemas/1.0.0/: the JSON Schema contract.
- docs/AUTHORING.md: how to add or revise a person.
- [docs/COVERAGE.md](docs/COVERAGE.md): category counts and a complete roster for this edition.
- [research/](research/README.md): sources, dating decisions and further candidates from the category research passes.
- tools/check.py: dependency-free structural and semantic checks.

There is no content compilation step. Publish the JSON files and images as static files, or let the engine read this repository through GitHub Raw.

## Editorial scope

The November 2026 additions brought the collection from 28 to 413 people and expanded the original profiles. Coverage spans more regions, eras and disciplines, including social research, engineering and performing arts. The [astronaut collection](research/astronauts.md) follows 30 people from Vostok 1 to joint research missions aboard space stations. It includes the three astronauts who trained for Apollo 1. Research notes record gaps and further candidates. Each person has a single record across all their categories.

Women in science and research is an additional cross-disciplinary category with 89 entries, including all 29 mathematicians identified in that selection. Every person also retains their subject categories. German category and group labels use gender-inclusive wording.

Dates are represented at year resolution. Approximate and disputed dates are explicitly marked; unknown endpoints remain unknown. People without a plottable lifespan remain available in the list and through their permanent person links. Individual notes explain important calendar differences. A life overlap does not imply a meeting, collaboration or influence.

English and German text is present throughout the collection. The other 22 official EU languages remain planned under Modern Objectivity MO-13. Prose and translations are AI-assisted. Independent historical and native-language review remains pending. Sources were consulted on 26–28 November 2026. Each record gives its consultation dates.

## Check

From this directory:

    python3 tools/check.py

The checker validates structure, references, dates, translations and local assets; it does not establish the truth of historical claims or legal status independently.

## License

Original prose, category text and tooling: GPL-2.0-only; see LICENSE. Third-party portraits retain the individual licenses and credits in each record and ASSETS.md. Source pages remain under their own terms; their text is not reproduced wholesale.
