quote = "If you can't fly, then run, If you can't run, then walk, If you can't walk, then crawl, But whatever you do,You have to keep moving forward"
#My first function that I will explain is the len() function. This function determines the length of a string.
#My second function I will explain is the str() function. This function converts values to a string form, so they can be combined with other strings. This was useful in this program since the len() function produces a interger, which needs to be converted to a string, so it can be attached to another string in this print statement.
print('The length of the quote is: ' + str(len(quote)))
#My final function I will explain is the split() function. This function splits a string into a list, using seperators and maxsplits. There can be diffierent values for these two parameters, but I made them default.
parts_of_quote = quote.split()
print('The number of parts in the quote: ' + str(len(parts_of_quote)))
