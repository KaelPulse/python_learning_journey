# Day 3 Notes

Conditionals today - if/elif/else, comparisons, modulo, nested ifs, 
and logical operators (and/or/not). This was a heavier day than the 
first two, especially once things started nesting.

## What I learned
- Comparison operators (> < >= <= == !=) and how they return True/False
- Modulo (%) - gives you the remainder of a division, useful for 
  things like checking even/odd or divisibility
- Important gotcha: `if number % 4:` is NOT the same as checking 
  divisibility - it's checking if there's a remainder, so it's 
  backwards from what it looks like. Need `== 0` to actually check 
  divisibility properly
- Nested if statements - putting an if inside another if to build 
  multi-step logic
- if/elif/else chains - only one branch runs, first match wins
- Logical operators: and needs both sides True, or needs one side 
  True, not flips a value
- and is evaluated before or, and not only applies to the single value 
  right next to it, not a whole expression - parentheses needed to 
  force different order
- Chained comparisons like `5 <= age <= 17` work properly when both 
  sides point the same direction. Something like `18.5 <= bmi >= 24.9` 
  looks like a range check but isn't - it's actually two separate 
  conditions joined with and, and doesn't do what it looks like

## Projects I built
- Rollercoaster height/age pricing (from the lesson)
- Number Sorter - takes 3 numbers, finds highest and lowest, handles 
  ties between any combination of the three
- Leap Year Checker
- Movie Ticket Pricing - age brackets + weekday/weekend pricing
- BMI Calculator - calculates BMI, categorises it, gives different 
  toned advice depending on category and whether the person is under 
  or over 18
- Gym Membership Cost Calculator - stacks 3 independent discounts 
  (age, student, frequency) across 8 possible combinations
- Tilt with Kael - a League of Legends-themed spin on the Treasure 
  Island project, using nested conditionals for queue accept, champ 
  pool choice, and lane selection

## Debugging patterns I ran into today (and actually fixed myself)
- Chained comparison bug: `age >= 12 <=18` doesn't check a range the 
  way it looks like it should - same mistake reappeared later with 
  `18.5 <= bmi >= 24.9`, so this is clearly a pattern I need to watch 
  for specifically
- Truthy/falsy trap with modulo: `if year % 4:` isn't the same as 
  checking divisibility - needed `== 0` to be explicit
- Silent fallthrough: if/elif chains with no final else can result in 
  nothing printing at all if none of the conditions match. Hit this 
  three separate times today across different exercises (Number 
  Sorter, two different points in the Gym Calculator) - clearly a 
  pattern to check for every time I write a conditional chain now
- Using float() to try to round a number (float(x, 2)) - float() only 
  takes one argument and doesn't round, that's what round() is for
- Referencing a variable outside the block where it was actually 
  created, causing a NameError - the variable only exists if that 
  specific branch of the code actually ran

## How today went
The Number Sorter and Gym Membership exercises both took several 
attempts to get fully correct - probably 4-5 rounds of testing edge 
cases, finding bugs, fixing them, then finding the next one. Didn't 
get either right on the first or even second try, but worked through 
each bug by actually tracing the logic by hand and testing specific 
inputs rather than guessing at fixes. Slower than I'd like but feels 
like the debugging muscle is actually building.