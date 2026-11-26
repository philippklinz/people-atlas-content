# People Atlas content rules

Read README.md, docs/AUTHORING.md and schemas/1.0.0 before editing.

- Content is independent from the engine and requires no application build. Edit JSON records and commit them directly.
- Preserve permanent IDs. Existing person URLs must keep resolving when names or translations change.
- Follow the versioned data contract. Coordinate breaking changes with people-atlas-engine; never silently reinterpret an existing field.
- Every biography requires sources. Cite the actual relevant page, and distinguish structural checks from historical review.
- Preserve uncertain, disputed and unknown dates. Civil year zero is invalid. Living status is explicit, never inferred from a missing death date.
- Category membership can overlap. A parent includes descendants; do not introduce cycles.
- Original prose must be maintained in English and German for the current complete editions. MO-13 targets all 24 EU languages; do not advertise unfinished translations.
- Portraits are local assets with creator, source, license and accessible descriptions. Do not hotlink images or invent historical portraits.
- Original prose is GPL-2.0-only. Preserve the individual rights of third-party images and source texts. Summarise sources in original wording.
- Run python3 tools/check.py after changes. Validate against the JSON Schemas when an editor supports them. Passing checks does not certify historical correctness.
