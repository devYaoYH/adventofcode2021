# Binary reverse-engineering + backtracking search

## Step 1: Reverse-engineer function from binary

- Notice the repeating pattern for each `inp w`.
- Extract the 'variable' components within each block (lines `div z _`, `add x _`, `add y _`).

## Step 2: Backtrack solution from last function (14 total)

- Inverse the function (instead of passing `(w,z') -> z`, `(z) -> (w,z')`) to backtrack what value of `z'` is required as the output from the previous block.
- For Part 1 (max), keep largest `w` for each value of `z'` to backtrack, Part 2 (min) is then just a slight modification.

## Testing reverse-engineered function against original binary

This takes the last 5 function runs, rolling over `z` from previous function outputs with an additional `inp z` at the start of the sample sub program `input_last5` (`12` in this case as per the first line in `serial_number`).

`cat input_last5 serial_number | python main.py`
