# Process

## Tools
- ChatGPT for assisting with code generation and Matplotlib layout adjustments.

## Kept
- I kept the dual-axis chart structure (`twinx()`) suggested by AI because it allows showing both hourly temperature and precipitation on a single graph effectively.

## Rejected
- I rejected an initial suggestion that used `pandas` to process the JSON data. Instead, I replaced it with Python's built-in `json` module and an explicit `for` loop to directly satisfy the course requirements for custom functions and loops without extra dependencies.