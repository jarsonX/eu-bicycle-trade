# EU Bicycle Trade

I am building a reproducible analysis of conventional and electric cycle trade
in Poland, Germany, and the Netherlands, using monthly Eurostat data for
2017–2025.

**Research question:** how is trade in conventional and electric cycles changing
in Poland compared with Germany and the Netherlands?

## Table Of Contents

- [Research Motivation](#research-motivation)
- [Data And Scope](#data-and-scope)
- [Planned Outputs](#planned-outputs)
- [Analytical And Technical Approach](#analytical-and-technical-approach)
- [Interpretation Limits](#interpretation-limits)
- [License And Reuse](#license-and-reuse)
- [Course And Authorship Note](#course-and-authorship-note)

## Research Motivation

I want to understand how Poland's cycle trade has evolved relative to Germany
and the Netherlands. I will compare imports and exports by value and quantity,
examine the share of the electric category, and describe seasonal patterns.

The aim is to establish which changes are supported by the data, where the
countries differ, and which findings warrant further investigation. A repeatable
analytical process will make the results traceable and easier to verify.

## Data And Scope

| Dimension | Agreed scope |
| --- | --- |
| Source | Eurostat COMEXT `DS-045409`, acquired directly from Eurostat |
| Period | January 2017–December 2025 |
| Reporting countries | Poland, Germany, the Netherlands |
| Partner | `WORLD` |
| Flows | Imports and exports, analysed separately |
| Measures | Nominal EUR values and quantities in pieces |
| Product categories | CN8 `87120030` and `87116010`, provisionally conventional and electric cycles |
| Target grain | Month × reporting country × partner × flow × CN8 |

Source availability, historical product definitions, units, flags, and coverage
must be verified before relying on the data. The reference grid contains 1296
keys; it does not guarantee that every observation is published or usable.

## Planned Outputs

- A source audit, preserved data snapshot, and acquisition manifest.
- My exploratory data analysis notebook, reproducible from a fresh kernel.
- A validated monthly dataset and data quality report.
- Tables and charts covering annual totals, year-on-year changes, descriptive
  seasonality, electric-category shares, and exports minus imports.
- A concise business report with traceable findings, limitations, and follow-up
  questions.
- A pipeline runnable with one command, tests for data quality and calculations,
  and automated quality checks.

## Analytical And Technical Approach

I will inspect the source and explore the real data before finalizing the internal
contract and pipeline design. Calculations will preserve units, completeness,
source flags, and snapshot provenance. Missing observations, genuine zeros,
incomplete years, and undefined ratios will be handled explicitly.

The planned stack is Python, Jupyter, pandas, Git/GitHub, pytest, Ruff, one type
checker (mypy or Pyright), and GitHub Actions, with NumPy or SQL where useful.
Exploration will stay in notebooks; production code will separate input/output,
configuration, validation, calculations, and orchestration. Tests and CI will
run offline on small fixtures.

Forecasting, ML, individual partner analysis, dashboards, web applications,
databases, cloud infrastructure, and purchasing recommendation systems are
outside the project scope.

## Interpretation Limits

The two selected CN8 categories do not cover the whole bicycle market. The
electric category also includes tricycles and quadricycles; its historical
definition and comparability require verification. Trade figures do not measure
retail sales or consumer demand and cannot alone determine order quantities.

EUR values are nominal. Seasonality is descriptive. The report will account for
source flags, classification changes, and export FOB/import CIF valuation, and
keep observations separate from causal hypotheses. The three countries will
remain separate comparisons rather than a combined EU market estimate.

## License And Reuse

I make my original code and materials available for reuse, modification, and
redistribution, including commercial use, under the following licenses.
Copyright (c) 2026 Jarosław Krzysztofik.

| Content | License |
| --- | --- |
| Code, scripts, tests, notebook code cells, and executable examples | MIT — full text in [LICENSE](LICENSE) |
| Original non-code materials: README, documentation, AI instructions, lectures, exercise descriptions, notebook narrative, reports, and charts | Creative Commons Attribution 4.0 International (CC BY 4.0) — full text in [LICENSE-CONTENT](LICENSE-CONTENT) |

**Personal use:** you do not need to contact me, pay a fee, or publish an
acknowledgment. Keep the copyright and permission notices required by MIT in
copies or substantial portions of the code, including private copies.

**Sharing materials:** when publicly sharing my CC BY 4.0 materials or adaptations,
credit me, link to the source and license, indicate changes, and retain the
supplied copyright, license, and warranty disclaimer notices as required by
the license. A short credit can begin with:

> Based on EU Bicycle Trade by Jarosław Krzysztofik, licensed under CC BY 4.0.

Add a link to this repository or the specific source file/version, and to
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). State what you changed
when applicable; linking to the source notices can help retain them.

**Publications and projects using the code:** I would appreciate a mention of
my name and a link to this repository in your article, presentation, report,
project README, or product credits. This is a voluntary request, separate from
MIT's requirement to preserve its copyright and permission notices.

Third-party data, dependencies, quotations, and other externally sourced
materials retain their own terms. These licenses cover only rights I can grant;
they do not relicense Eurostat data or override source attribution and
redistribution requirements. The data audit will verify the terms for the
specific source and snapshot before redistribution.

## Course And Authorship Note

This project is part of my **Data Science × AI** course. I designed the 
curriculum, learning objectives, and an AI agent framework for creating course 
materials and guiding my learning.

Within this framework, authoring agents generate project specifications, lessons, 
and instructions for teaching agents. The teaching agents then use those materials 
to coach me through the lessons and project work. I defined the workflow, teaching 
sequence, instruction routing, and completion criteria, with AI supporting 
preparation, implementation, and review.

This repository contains one project from that learning path, together with its 
lessons and teaching agent instructions. The framework used to generate those 
materials and instructions is maintained separately and is not included here.
