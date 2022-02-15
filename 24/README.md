# Binary reverse-engineering + backtracking search

## Step 1: Reverse-engineer function from binary

## Step 2: Backtrack solution from last function (14 total)

## Small Sample testing

This takes the last 5 function runs, rolling over `z` from previous function outputs with an additional `inp z` at the start of the sample sub program `input_last5` (`12` in this case as per the first line in `serial_number`).

`cat input_last5 serial_number | python main.py`
