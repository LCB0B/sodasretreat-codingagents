# SODAS Retreat Exercise: Measuring Attention to Energy

## Research question

> How has presidential attention to energy evolved in State of the
> Union addresses since 1946?

Seven groups will use the same English-language speech corpus and a coding
agent to answer this question. Each group may make its own analytical choices.
At the end, we will combine the seven sets of estimates and examine how much
the conclusions vary across approaches.

This is a measurement-multiverse exercise. The objective is not to discover
the single correct measure. It is to produce a defensible measure, inspect it,
and make the consequential choices transparent.

## Groups

Work only in your assigned folder:

- `groups/amber/`
- `groups/blue/`
- `groups/coral/`
- `groups/green/`
- `groups/purple/`
- `groups/silver/`
- `groups/teal/`

Do not modify another group's files.

## Input

The common corpus is provided as `corpus.csv` in this directory. It contains
one document for every year from 1946 through 2020, with columns for year,
president, party, document type, and full text. Treat the supplied corpus and
its time period as fixed. Do not retrieve or substitute a different version of
the speeches. See `DATA.md` for sources and document-selection rules.

## Task

Use a coding agent to construct an annual measure of the share of each speech
devoted to energy. Your group decides:

- what counts as attention to energy;
- how the text should be preprocessed;
- whether to use a dictionary, classification, or another transparent method;
- how to handle indirect or historically changing terminology; and
- how to validate the resulting measure.

Energy may be discussed as a matter of supply, prices, national security,
industrial policy, conservation, or environmental transition. References to
oil, gas, coal, nuclear power, electricity, or renewable energy may therefore
fall inside or outside the concept depending on the group's definition. Treat
these choices as measurement problems rather than merely technical problems.

## Required outputs

Submit exactly three files in your group folder. Templates are already present.

### `results.csv`

The file must have exactly these columns:

```text
year,estimate
1946,0.000
1947,0.012
```

Requirements:

- one row for every speech year in the supplied corpus;
- years sorted in ascending order;
- `estimate` must be numeric and between 0 and 1;
- estimates must represent the unsmoothed annual measurements;
- no missing values; and
- no additional columns.

### `analysis.md`

Complete all sections of the supplied template. Keep it concise, but provide
enough information for the other groups to understand what produced your
estimates. Include the important instructions given to the coding agent and
describe where group members intervened.

### `evaluation.md`

Reflect on the advantages and disadvantages of using a coding agent for this
task. Complete all sections of the supplied template and distinguish, where
possible, between limitations of the agent, limitations of the chosen method,
and choices made by the group.

## Submission

Before submitting, confirm that your folder contains only the completed
`results.csv`, `analysis.md`, and `evaluation.md` files.

If using Git, commit and push only your group's three files. If using a shared
upload folder, replace the templates in your assigned folder with the completed
versions. Submit before the break so the seven result files can be combined
while participants are away.

## Success criteria

A successful submission:

- covers every year in the common corpus;
- measures the same substantive quantity in every year;
- follows the required file format;
- explains the group's analytical choices;
- reports at least one substantive validation check; and
- acknowledges important limitations; and
- reflects on the advantages and disadvantages of using a coding agent.

## Common failure modes

- **An overly broad measure:** generic references to prices, industry,
  technology, or national security are counted as energy attention.
- **An overly narrow measure:** only the exact word *energy* is counted,
  missing references to particular fuels, electricity, or conservation.
- **An inconsistent denominator:** the measure changes from word share to
  sentence share across years.
- **Uninspected output:** plausible-looking estimates are accepted without
  examining the underlying text.
- **A malformed submission:** years are missing, estimates fall outside
  0--1, or the CSV contains additional columns.
