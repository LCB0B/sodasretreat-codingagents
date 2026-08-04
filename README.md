# SODAS Retreat Exercise: Measuring Climate Attention

## Research question

> How has presidential attention to climate change evolved in State of the
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

The common corpus will be provided as `corpus.csv` in this directory. Treat
the supplied corpus and its time period as fixed. Do not retrieve or substitute
a different version of the speeches.

## Task

Use a coding agent to construct an annual measure of the share of each speech
devoted to climate change. Your group decides:

- what counts as attention to climate change;
- how the text should be preprocessed;
- whether to use a dictionary, classification, or another transparent method;
- how to handle indirect or historically changing terminology; and
- how to validate the resulting measure.

Historical speeches may discuss relevant phenomena without using contemporary
terms such as *climate change*. Conversely, words such as *climate*, *green*,
or *energy* may appear in unrelated contexts. Treat these as measurement
problems rather than merely technical problems.

## Required outputs

Submit exactly two files in your group folder. Templates are already present.

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

## Suggested workflow (50 minutes)

1. **Define the concept (10 minutes).** Agree on what should and should not
   count as climate attention.
2. **Build the measure (20 minutes).** Ask the agent to implement and apply the
   approach to the complete corpus.
3. **Validate it (10 minutes).** Inspect positive cases, false positives,
   apparent false negatives, and unusual years.
4. **Finalize the outputs (10 minutes).** Check the CSV schema and complete the
   analytical note.

A simple, inspected measure is preferable to an elaborate method that the
group does not have time to validate.

## Submission

Before submitting, confirm that your folder contains only the completed
`results.csv` and `analysis.md` files.

If using Git, commit and push only your group's two files. If using a shared
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
- acknowledges important limitations.

## Common failure modes

- **An overly broad measure:** generic references to energy, nature, weather,
  or the environment are counted as climate attention.
- **An overly narrow measure:** only the exact phrase *climate change* is
  counted, missing older or indirect language.
- **An inconsistent denominator:** the measure changes from word share to
  sentence share across years.
- **Uninspected output:** plausible-looking estimates are accepted without
  examining the underlying text.
- **A malformed submission:** years are missing, estimates fall outside
  0--1, or the CSV contains additional columns.

