# Day 5 Notes

For loops and range() today. Lower focus day overall - kept making 
small slips (typos, forgetting to initialise a variable before a loop) 
that I'd probably have caught faster on a clearer day.

## What I learned
- for loops repeat a block of code once for each item in something, 
  like a list or a range of numbers
- range(1, 101) gives numbers 1 through 100 - the second number isn't 
  included, so you need to go one higher than the actual number you 
  want to end on
- += is shorthand for "take the current value, add to it, store it 
  back" - but the variable needs to already exist with a starting 
  value before you can use += on it inside a loop, otherwise it 
  doesn't know what to add to
- Caught a bug in one of Angela's own lesson examples - a list of 
  scores was written with quotes around the numbers, making them 
  strings instead of actual numbers, which meant comparing them with > 
  would have crashed. Fixed it by removing the quotes

## What I built
- Fixed a Gauss sum exercise (adding total = 0 before the loop to fix 
  a NameError)
- FizzBuzz 1-100 using a for loop - had a bug where one of my 
  conditions checked the same thing twice by mistake instead of 
  checking the other number, making it impossible to ever be true

## Notes on today
Didn't rebuild yesterday's password generator with a loop like the 
lesson suggested - decided that was more effort than the day had in 
it, and yesterday's version already solves the same problem, just with 
random.sample() instead of a loop. Might revisit that specific 
refactor another day as extra loop practice.