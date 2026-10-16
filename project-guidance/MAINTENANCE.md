# Project Presentation And Licensing Maintenance

These instructions govern README updates and license/reuse maintenance.
The final-project specification is in [PROJECT.md](PROJECT.md).

## Project README

- Lead root README with EU Bicycle Trade and the research question. Describe
  motivation, source/scope, methods, outputs, limitations, status, and reproducibility.
- Write on the owner's behalf in the first person. Present genuine research
  motivation and the working project; keep fictional client/role scenarios,
  learning phases, and pack-copying narratives out of the presentation.
- End with one short note naming **Data Science × AI** and stating that the owner
  created the course and its AI framework. Use "I created" and briefly name
  curriculum/competencies, agent authoring workflow, teaching sequence, instruction
  routing, and completion criteria; avoid biography or detailed framework explanation.
- Do not link to AGENTS, guidance, units, materials, or progress. The TOC may link
  within README; the project presentation must be understandable on its own.
- Separate plans from verified work/results. Add Python/dependency versions,
  setup, exact snapshot access, acquisition/pipeline/test/quality commands,
  outputs, architecture, decisions, and common failures/remedies only when
  implemented and checked. Do not invent data, commands, findings, or passed checks.
- On updates, verify first-person voice, the final note's brevity/position,
  absence of teaching narratives/instruction links, and evidence for status claims.
- Preserve the public reuse section before the final authorship note; apply
  License And Reuse below when maintaining licensing notices.

## License And Reuse

- Preserve the content split in [README.md](../README.md#license-and-reuse),
  with the complete MIT text in [LICENSE](../LICENSE) and the complete CC BY 4.0
  text in [LICENSE-CONTENT](../LICENSE-CONTENT). Keep both files when copying
  this pack to the project repository; they are shipped artifacts.
- Apply MIT to original code, including notebook code cells and executable
  examples embedded in teaching materials. Apply CC BY 4.0 to original non-code
  materials, including AI instructions and generated teaching materials. A mixed
  notebook or document follows this content split rather than a single license
  based on its extension.
- Keep the publication/project credit request voluntary for MIT code. Do not
  describe it as an extra license condition or promise that private code copies
  may omit MIT notices. Preserve the distinction between private use and public
  sharing of CC BY materials.
- Preserve third-party licenses and source notices. Before adding or distributing
  external data/materials, verify their terms and mark any exceptions to the
  repository's default split alongside the affected artifact. The source audit
  in [PROJECT.md](PROJECT.md#source-verification) covers verification of Eurostat snapshot reuse; do not
  apply the owner's licenses to source data or third-party rights.
- Keep attribution examples tied to Jarosław Krzysztofik and EU Bicycle Trade.
  Add a public repository or source-version URL only after verifying it; do not
  invent one. Changes to the approved licenses or their scope require the owner's
  explicit approval.
