# aoc2023

[2023 Advent Of Code](https://adventofcode.com/2023) - My solutions

"2 years late but still some fun".

## Python

  * `python/day1part1.py` - It's a regular expression thing with a
  heuristic handling one edge case.

  * `python/day1part2.py` - The elaboration caused quite a nice little
  parsing problem, what with the shared characters and all. I took a
  pragmatic approach to get back to numbers without disturbing that which
  I quite like as a bit elegant. I mean the code looks like crap,
  though....

  * `python/day2part1.py` - About 75% text parsing by code and thought.
  Actual problem is relatively simple once the input's been parsed, just a
  bit of bookkeeping here and there to sort out the answer.

  * `python/day2part2.py` - All the hard work done by the parser for
  part1, this is just a calc problem once you've got a datastructure with
  the game elements in.

  * `python/day3part1.py` - Nothing wrong with my comparisons. About an
  hour and a half wasted on missing a case with a number hanging on the
  end of the line thanks to forgetting a clean-up case....

  * `python/day3part2.py` - Made a bit of heavy weather solving this,
  although I'd done most of the hard work in part 1 I'm not particularly
  happy with my approach to actually looking for gear ratios. It works,
  but it feels clunky aand overwrought. But... a win is a win.
