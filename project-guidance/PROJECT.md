# EU Bicycle Trade

## Table Of Contents

- [Business Scenario And Objective](#business-scenario-and-objective)
- [Data Scope](#data-scope)
- [Source Verification](#source-verification)
- [Snapshot And Reproducibility](#snapshot-and-reproducibility)
- [Data Contract](#data-contract)
- [Measures And Interpretation](#measures-and-interpretation)
- [Deliverables And Technical Requirements](#deliverables-and-technical-requirements)
- [Product Acceptance](#product-acceptance)

## Business Scenario And Objective

A bicycle distributor in Poland is reviewing its portfolio and purchasing
assumptions. The Head of Category Management asks the analyst to compare
historical trade in Poland, Germany, and the Netherlands.

**Research question:** how is trade in conventional and electric cycles changing
in Poland compared with Germany and the Netherlands?

The project is a reproducible analysis supporting that scenario: trade changes,
the electric category's role, seasonality, and questions for further business
investigation. The scenario defines the analytical task; it is not evidence of
an actual client commission. Trade alone cannot determine purchasing quantities.

## Data Scope

| Dimension | Agreed scope |
| --- | --- |
| Source | Eurostat COMEXT `DS-045409`, acquired directly from Eurostat |
| Period | January 2017–December 2025; no 2026 or later data |
| Reporters / partner | Poland, Germany, the Netherlands, compared separately / `WORLD` |
| Flows / measures | Imports and exports separately / nominal EUR and quantity in pieces |
| Conventional category | CN8 `87120030`: provisionally non-motorised bicycles with ball bearings |
| Electric category | CN8 `87116010`: provisionally pedal-assisted bicycles, tricycles and quadricycles with an auxiliary electric motor rated at no more than 250 W continuous power |

Forecasting, ML, individual partner-country analysis, dashboards, web apps,
databases, cloud infrastructure, and purchasing recommendations are outside
this delivery. Later stages may extend `eu-bicycle-trade`.

## Source Verification

Source availability, dimensions/codes, monthly frequency, filtered acquisition,
indicator scales, historical category definitions/units, flags, confidentiality,
revisions, coverage, and reuse/redistribution rights remain unverified.
M02 in [LEARNING.md](LEARNING.md#m02--source-audit-and-sample) resolves these
dependencies before affected calculations. No query or real sample is prevalidated.
A filtered COMEXT API download or direct Eurostat export is acceptable.

Unresolved code/unit comparability blocks affected calculations; unavailable
real data blocks analysis acceptance. Synthetic data cannot replace the source
audit. Changes to the agreed source, codes, dates, or units require an owner
decision; kg or 100 kg cannot substitute for pieces. Third-party rights remain
outside the repository's own licenses.

Source references:
[database/classifications](https://ec.europa.eu/eurostat/web/international-trade-in-goods/database),
[methodology](https://ec.europa.eu/eurostat/cache/metadata/en/ext_go_detail_sims.htm),
[COMEXT API guide](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started/comext-database).

## Snapshot And Reproducibility

Unchanged source responses have a manifest containing dataset, filters, exact
URL, retrieval time with timezone, format, snapshot ID, and file checksums.
Each acquisition creates a new snapshot without overwriting earlier versions.
Processing uses the local snapshot without contacting Eurostat.

The distribution method depends on verified reuse terms and size: a small tracked
snapshot or an accessible, precisely identified external artifact with checksum.
A clean checkout must make the exact snapshot obtainable; downloading the latest
revision cannot reproduce an earlier report.

## Data Contract

The internal contract is finalized from the source audit and exploratory data
analysis (EDA). Field names below are internal, not assumed API response names.

| Field | Requirement |
| --- | --- |
| `month` | Consistent monthly representation, 2017-01–2025-12 |
| `reporter` / `partner` | Verified codes mapped to the three agreed countries / `WORLD` |
| `flow` / `product_cn` | Unambiguous import/export mapping / string `87120030` or `87116010` |
| `value_eur` / `quantity_pieces` | Finite nonnegative value in verified units, or explicit missing value |
| `status/provenance` | Separate flags for each measure and a link to source response/snapshot |

The unique key is month × reporter × partner × flow × CN8. Indicator rows must
be unique before joining measures; other source dimensions are explicitly
fixed/filtered. Overlapping partner aggregates or product totals/components
cannot be added together. Reference coverage is 108 months × 3 reporters ×
2 flows × 2 codes = 1296 keys, not guaranteed observations.

Validation covers schema, parsing/types, keys, dimensions, units, dates, numerical
ranges, and coverage separately for EUR and pieces. Structural errors, wrong
units, and duplicate keys stop processing. Missing observations produce quality
findings and restrict calculations. Absent rows, missing/confidential values,
and genuine zeros remain distinct; no undocumented repairs, unsupported
imputation, or replacement with zero. Flag eligibility follows source metadata
and is explicit in the contract; eligible preliminary values retain labels.

## Measures And Interpretation

Results retain unit, period, completeness, flags where relevant, and snapshot ID.
Calculations remain separate by reporter, flow, product, and measure unless
the definition explicitly combines a dimension.

| Measure | Definition and eligibility |
| --- | --- |
| Annual total | Sum 12 usable months. Label partial sums with month count; an entirely missing series cannot become zero. |
| Year-on-year change | `(current / previous - 1) × 100%` for comparable complete annual totals. A missing/zero base is undefined with a reason; no prior year exists for 2017 within scope. |
| Descriptive seasonality | Monthly shares of a positive complete annual total, averaged by calendar month across eligible years. State year count; no eligible years means undefined. |
| Electric share | `electric / (conventional + electric) × 100%` for comparable available categories and a positive denominator, separately for EUR/pieces, country, flow, and period. Annual shares use complete annual sums, not mean monthly shares. |
| Trade balance | Exports minus imports in matching units, country, product, and period. Both sides are required, with complete years for annual balances; negative balances are valid. |

These categories form a selected basket, not the whole bicycle market; the
electric category includes tricycles and quadricycles. The three countries do
not form a distinct EU market aggregate. Trade is not retail sales or consumer
demand, and nominal EUR is not inflation-adjusted growth. Seasonality is
descriptive, not seasonal adjustment or forecasting. Interpretation accounts
for classification changes, confidentiality, source flags, and export FOB/import
CIF valuation, separating findings from causal hypotheses and purchasing advice.

## Deliverables And Technical Requirements

The delivery comprises a source audit and contract, preserved snapshot/manifest,
the learner's EDA notebook, validated monthly dataset, data quality report,
tables/charts for all agreed measures, and a concise business report with
traceable findings, limitations, and follow-up questions.

The stack is Python, Jupyter, pandas, Git/GitHub, pytest, Ruff, one type checker
(mypy or Pyright), and GitHub Actions; NumPy or SQL is optional where useful.
Python/dependency versions, environment, and the simplest justified design
remain implementation decisions to agree before implementation.

Exploration stays in notebooks; production modules separate input/output,
configuration, validation, calculations, and orchestration, with typing, error
handling, and useful logging. Acquisition has an explicit command; a separate
one-command pipeline produces all analytical deliverables from the local snapshot.
Critical failures return nonzero without misleading success artifacts. Logs
identify stages, snapshot, counts, and quality summaries, not full responses
or secrets.

## Product Acceptance

- The source audit/contract supports every used calculation. The EDA notebook
  runs from a fresh kernel, and reports expose data quality and interpretation limits.
- An unfamiliar person can clone the repository, obtain the exact snapshot,
  follow README setup, and generate all deliverables with one pipeline command.
  Identical data/configuration/code gives identical numerical results;
  run timestamps may differ.
- Offline unit/integration tests cover valid data, calculation edge cases,
  corrupt input, incomplete years, and critical failures. Expected results are
  derived independently of tested functions; network failures use fakes.
- Ruff lint/format checks, the chosen production-code type checker, pytest,
  and actual GitHub Actions pass for the accepted version.
- README documents problem/scope, Python/dependency versions, setup, snapshot
  access, acquisition/pipeline/test/quality commands, outputs, architecture,
  decisions, limitations, and common failures/remedies.
- Report claims trace to outputs and snapshot. Public artifacts describe actual
  project work; README presentation/licensing follows
  [MAINTENANCE.md](MAINTENANCE.md), without implying a real client commission.
