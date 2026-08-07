# Day 2 Notes

Built on Day 1 basics - mainly learned how to actually do calculations 
with user input instead of just printing it back.

## What I learned
- input() always returns a string, even if the user types a number - 
  so you have to cast it with float() or int() before doing any maths 
  with it
- float() vs int() - use float() when decimals matter (money), int() 
  when you just need whole numbers
- round() - lets you control how many decimal places a number shows, 
  useful for anything involving currency
- f-strings - way cleaner than using + to combine strings and 
  variables, especially when mixing text and numbers together
- Order of operations actually matters in code the same way it does in 
  maths - division happens before addition unless you use brackets to 
  force it

## Scripts I wrote
- **Age Calculator** - takes a birth year, calculates current age, 
  prints it with an f-string
- **Restaurant Bill Splitter** - splits a bill with a service charge 
  across multiple people
- **Grocery Receipt Generator** - takes 3 items and prices, calculates 
  a total, applies a 5% discount, prints it formatted like a receipt

  ## Mistakes I made
- On the bill splitter, I divided the service charge by the number of 
  people before adding it to the total bill, instead of dividing the 
  whole combined total. Order of operations bug - needed brackets 
  around (total_bill + actual_service_charge) to fix it properly
- Used len(item1+item2+item3) in the receipt generator and it actually 
  worked, but not for the reason I thought. I assumed it would 
  calculate len() on each item separately and add those numbers 
  together. What it actually does is concatenate the three strings 
  into one long string first, then measures the length of that combined 
  string. Got the right answer by accident, not by understanding what 
  was happening - worth remembering the difference