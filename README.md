# People Atlas content

An initial curated collection of 28 people and 10 overlapping categories, from antiquity to the modern era. Each entry includes a short original biography, life dates, categories and external sources. Portraits are included where attribution and reuse terms have been recorded.

The collection is read by [people-atlas-engine](https://github.com/philippklinz/people-atlas-engine), but has no dependency on the engine's rendering code.

## Files

- catalog.json: version, languages, collection paths and featured records.
- categories.json: category definitions and the scientific category hierarchy.
- people/: biography collections.
- assets/portraits/: local images with attribution in each person's record.
- schemas/1.0.0/: the JSON Schema contract.
- docs/AUTHORING.md: how to add or revise a person.
- tools/check.py: dependency-free structural and semantic checks.

There is no content compilation step. Publish the JSON files and images as static files, or let the engine read this repository through GitHub Raw.

## Editorial scope

This is an introductory selection, not a complete or representative history. It includes multiple fields and some overlapping careers, but coverage is uneven and currently centred on a limited set of well-documented examples. Categories are contemporary navigational aids.

Dates are represented at year resolution. Approximate dates are explicitly marked. Individual notes explain important calendar differences. A life overlap does not imply a meeting, collaboration or influence.

English and German are complete for the initial collection. The other 22 official EU languages remain planned under Modern Objectivity MO-13. Prose and translations are AI-assisted; independent historical and native-language review remains pending. Sources were consulted on 26 November 2026.

## Check

From this directory:

    python3 tools/check.py

The checker validates structure, references, dates, translations and local assets; it does not establish the truth of historical claims or legal status independently.

## License

Original prose, category text and tooling: GPL-2.0-only; see LICENSE. Third-party portraits retain the individual licenses and credits in each record and ASSETS.md. Source pages remain under their own terms; their text is not reproduced wholesale.
