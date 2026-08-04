# Corpus documentation

## Contents

`corpus.csv` is a frozen corpus of United States presidential State of the
Union addresses and messages. It contains 75 records: one document for every
calendar year from 1946 through 2020.

The columns are:

- `year`: calendar year of the document;
- `president`: president who delivered or submitted the selected document;
- `party`: president's political party (`Democratic` or `Republican`);
- `document_type`: `speech` or `written`; and
- `text`: full document text.

## Sources

The main source is version 1.0.4 of Taylor B. Arnold's R package `sotu`,
published on CRAN on August 17, 2022:

- https://cran.r-project.org/package=sotu
- https://doi.org/10.32614/CRAN.package.sotu

The package supplies the document texts and metadata through 2020. Its CRAN
documentation notes that the speech corpus is in the public domain.

The 1973 document is Richard Nixon's *State of the Union Message to the
Congress: Overview and Goals*, taken from the stdlib SOTU dataset:

- https://github.com/stdlib-js/datasets-sotu
- https://github.com/stdlib-js/datasets-sotu/blob/main/data/1973_richard_nixon_r.txt

The stdlib dataset dedicates its database and contents to the public domain
under PDDL 1.0 and CC0 1.0.

Document dates, delivery modes, and exceptional years were checked against the
American Presidency Project's reference table:

- https://www.presidency.ucsb.edu/documents/presidential-documents-archive-guidebook/annual-messages-congress-the-state-the-union

Suggested citation for the reference table:

> Peters, Gerhard, and John T. Woolley. "The State of the Union, Background
> and Reference Table." *The American Presidency Project*. University of
> California, Santa Barbara.

## Selection rules

The corpus contains exactly one document per year. The general rule is to use
the spoken address when one is available and otherwise use the principal
written message. This avoids giving participants different source documents
for the same year.

The following years required an explicit choice:

| Year | Included | Excluded or omitted |
|---:|---|---|
| 1953 | Dwight D. Eisenhower's spoken address | Harry S. Truman's outgoing written message |
| 1956 | Dwight D. Eisenhower's spoken summary | Eisenhower's longer written message |
| 1961 | John F. Kennedy's spoken address | Eisenhower's outgoing written message |
| 1972 | Richard M. Nixon's spoken address | Nixon's written message |
| 1973 | Nixon's written *Overview and Goals* message | Five later policy-specific messages and associated radio addresses |
| 1974 | Nixon's spoken address | Nixon's written message |
| 1978 | Jimmy Carter's spoken address | Carter's written message |
| 1979 | Carter's spoken address | Carter's written message |
| 1980 | Carter's spoken address | Carter's written message |
| 1981 | Ronald Reagan's first-year joint-session speech | Carter's outgoing written message |

First-year joint-session speeches are included even when they were not
formally titled "State of the Union." This follows a common convention in SOTU
corpora and keeps the series annual. The 1969 and 1977 documents are classified
as speeches following the American Presidency Project reference table.

## Validation

The frozen file was checked for:

- exactly 75 records and five columns;
- complete and unique year coverage from 1946 through 2020;
- ascending year order;
- no missing values;
- party values limited to `Democratic` and `Republican`;
- document types limited to `speech` and `written`; and
- nonempty full text for every record.

The text has not been tokenized, stemmed, lowercased, or otherwise preprocessed.
Participants should make and report those analytical choices themselves.
