# Millie UI Pressure Cases

`cases.json` contains behavioral pressure cases for testing the skill in real agent runtimes.

The package validator verifies structure and JSON validity only. It does **not** claim these cases
pass until an actual agent is run against them. For skill evolution, capture a baseline failure,
change the skill, rerun the same cases, and record regressions.
