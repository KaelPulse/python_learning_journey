# Day 4 Notes

Modules today - importing built-in ones, writing my own file and 
importing that too, plus lists. Also ended up doing more debugging 
than expected on a couple of the smaller exercises.

## What I learned
- import brings in reusable code, usually functions, from another 
  file - but it doesn't magically share variables between files. 
  Each file runs on its own, so a module can't see variables from 
  main.py unless you actually pass them in
- To use your own file as a module, you just import it by filename 
  (no .py) and call things from it using dot notation, like 
  Password_strenght.check_strenght(password)
- Lists - storing multiple related values, indexing, and using them 
  with things like random.sample() to pick several random items at 
  once without repeats
- random.sample() picks a given number of random unique items from a 
  list
- random.shuffle() shuffles a list in place - it doesn't return 
  anything, so trying to do shuffled = random.shuffle(list) just gives 
  you None, not the shuffled list. Learned this one the hard way
- "".join(list) turns a list of characters back into one normal 
  string, with whatever you put in the quotes as the separator between 
  each item. Wasn't taught yet but needed it to finish the password 
  generator, so looked it up - good to already understand it before 
  I get it properly explained later.
- Functions haven't covered return yet, so used print() inside my 
  module function instead. Worth revisiting this project later once 
  return is taught, since right now main.py can't actually use the 
  result for anything, it just displays it

## Projects I built
- Rock, Paper, Scissors - went through several real bugs on this one: 
  comparing a number to a random word by mistake, a NameError from a 
  variable only existing inside one branch, and an indentation issue 
  where my win/lose logic wasn't actually nested where it needed to be
- Password Generator with a custom module - generates a random 
  password from letters, numbers and symbols based on user input, 
  shuffles them, joins them into a string, then checks the strength 
  using a function imported from a separate file

## Debugging notes
Rock Paper Scissors took a few passes - kept almost fixing it but 
missing one part of the fix each time (fixed the comparison, then hit 
a NameError, then had to fix indentation). Same root lesson each time 
though - a variable only exists inside the block where it was created, 
so anything that needs it has to live inside that same block too.

The password generator also had the None bug from random.shuffle() not 
returning anything, and separately a None being printed because my 
module function used print() instead of return, which I didn't 
understand until it was explained - print() shows something on screen 
but doesn't hand a value back to whatever called the function.