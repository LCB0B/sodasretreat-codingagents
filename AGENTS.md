# Instructions for coding agents

## Objective

Assist the group in estimating the annual share of each State of the Union
address devoted to energy from 1946 through 2020. This is a measurement
multiverse exercise: there is no prescribed definition or preferred method.

Read `README.md` before beginning and use `DATA.md` for corpus documentation.

## Input

Use `corpus.csv` as the only speech corpus. Treat its documents, metadata, and
time period as fixed. Do not edit it, replace it, or retrieve additional speech
texts.

## Analytical freedom

The group has final authority over all substantive and methodological choices,
including the definition of energy attention, preprocessing, measurement
method, treatment of historical terminology, denominator, and validation.
You may explain or propose alternatives, but do not treat any particular
approach as required. Make consequential choices visible to the group and
apply the chosen quantity consistently across years.

## Outputs

After identifying the group's color, complete the three templates in the
corresponding `groups/<color>/` folder. Do not modify repository documentation,
the input corpus, or another group's files. The completed folder must contain
exactly:

- `results.csv`: exactly the columns `year,estimate`, with one row for each of
  the 75 years from 1946 through 2020, sorted by year. Estimates must be
  unsmoothed, numeric, between 0 and 1, and contain no missing values.
- `analysis.md`: a concise account of the definition, measurement, agent
  workflow, consequential choices, and limitations. Complete every section of
  the template; if the group did not check the measure, say so in one line
  rather than leaving the section empty.
- `evaluation.md`: the group's reflections on the advantages and disadvantages
  of using a coding agent, necessary human oversight, trust, and future use.
  Do not invent opinions for the group; elicit their views and help record them.

Do not add scripts, intermediate files, or extra columns to the submitted
folder. Before finishing, verify the required filenames and the complete CSV
schema and year coverage.

## Submission

Do not commit or push the outputs. One group member must email the three files
as attachments, using the group color as the subject line (for example,
`amber`). Keep all three filenames unchanged and submit before the break.
