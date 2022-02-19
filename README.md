# adventofcode2021
Advent Of Code solutions. https://adventofcode.com/2021

## Question analysis

(Subjective) Relative Difficulty:
![#595843](https://via.placeholder.com/15/595843/000000?text=+) Warmup
![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) Easy
![#F28705](https://via.placeholder.com/15/F28705/000000?text=+) Medium
![#A62F03](https://via.placeholder.com/15/A62F03/000000?text=+) Hard

- [![#595843](https://via.placeholder.com/15/595843/000000?text=+) [1]](https://adventofcode.com/2021/day/1): [Roll Tide!](https://www.youtube.com/watch?v=K0_5Nup_uBw)
- [![#595843](https://via.placeholder.com/15/595843/000000?text=+) [2]](https://adventofcode.com/2021/day/2): Translate english into `code`.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [3]](https://adventofcode.com/2021/day/3): A *bit* of recursion practice for later ;)
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [4]](https://adventofcode.com/2021/day/4): Some OOP goes a long way.
- [![#595843](https://via.placeholder.com/15/595843/000000?text=+) [5]](https://adventofcode.com/2021/day/5): Good'ole bunch of if-elses.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [6]](https://adventofcode.com/2021/day/6): Consider a O(Day) solution instead of O(Fish*Day).
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [7]](https://adventofcode.com/2021/day/7): Bruteforce O(N^2), notice that optimal location will be already occupied by a crab, arithmetic sum for fuel cost.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [8]](https://adventofcode.com/2021/day/8): Solved on paper first, disambiguate segments by comparing to known digits (mapped based on unique length).
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [9]](https://adventofcode.com/2021/day/9): BFS from the identified low points (flood-fill).
- [![#595843](https://via.placeholder.com/15/595843/000000?text=+) [10]](https://adventofcode.com/2021/day/10): Apply the scoring rules on a stack.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [11]](https://adventofcode.com/2021/day/11): Simulation, propagate each flashing octopus until no more updates each turn.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [12]](https://adventofcode.com/2021/day/12): DFS with some additional conditional added to pass part 2.
- [![#595843](https://via.placeholder.com/15/595843/000000?text=+) [13]](https://adventofcode.com/2021/day/13): Don't actually fold the paper, just work with the input coordinates until the last step.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [14]](https://adventofcode.com/2021/day/14): Simulation impossible, similar to Day 6, need to derive compressed representation of state.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [15]](https://adventofcode.com/2021/day/15): Straightforward A* search solution (manhattan heuristic).
- [![#A62F03](https://via.placeholder.com/15/A62F03/000000?text=+) [16]](https://adventofcode.com/2021/day/16): Recurse with care, 'Hard' due to many edge cases, my solution doesn't pass one sample o.O but passes for my input...
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [17]](https://adventofcode.com/2021/day/17): Possible to bruteforce simulations, but need to notice the bounds for possible initial velocities.
- [![#F28705](https://via.placeholder.com/15/F28705/000000?text=+) [18]](https://adventofcode.com/2021/day/18): Practice implementing binary tree with some traversals, part 2 required some modifications to not mutate nodes in-place.
- [![#F28705](https://via.placeholder.com/15/F28705/000000?text=+) [19]](https://adventofcode.com/2021/day/19): Bruteforce but tricky due to the amount of cases to consider. Helpful to imagine the 24 possible orientations with a Rubik's Cube and rotate coordinates with some matrix algebra.
- [![#488C03](https://via.placeholder.com/15/488C03/000000?text=+) [20]](https://adventofcode.com/2021/day/20): Need to take note of edge cases (idx 0 & 255) and impact of each enhancement pass on 'infinite' cells.
- [![#F28705](https://via.placeholder.com/15/F28705/000000?text=+) [21]](https://adventofcode.com/2021/day/21): Recursion problem with a dash of math, compress tree depth first with some combinatorics ([really short solution](/21/main2.py)).
- [![#A62F03](https://via.placeholder.com/15/A62F03/000000?text=+) [22]](https://adventofcode.com/2021/day/22): Interesting geometry qns, some initial math needed for insight, thereafter bruteforce possible ([notes](/22)).
- [![#F28705](https://via.placeholder.com/15/F28705/000000?text=+) [23]](https://adventofcode.com/2021/day/23): Graph problem (shortest path), much of the search space is filtered out by the rules of amphipod etiquette.
- [![#A62F03](https://via.placeholder.com/15/A62F03/000000?text=+) [24]](https://adventofcode.com/2021/day/24): 9^14 brute-force impossible, need to reverse-engineer the 'binary' and do some backtracking ([notes](/24)).
- [![#595843](https://via.placeholder.com/15/595843/000000?text=+) [25]](https://adventofcode.com/2021/day/25): Merry Christmas!

## Some thoughts

First year participating in AdventofCode, only heard about it after Christmas though :P It's quite enjoyable, none of the questions were obtusely difficult, though a couple needed some interesting insights.

* Q[1-5]: Warmup
* Q[6-15]: Some algo/DS needed
* Q[16-20]: I found more tricky than difficult, care in implementation
* Q[21-24]: Worth attempting, quite interesting questions
* Q[25]: Where did the last star come from?!
