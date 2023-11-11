word_meaning= {('1','Incumbent'):'The person currently in a particular job or political office',
('2','Precinct'): 'Polling place based on location',
('3','Electoral College'): ('The number of electors a state receives', 'Equal to that states' 'Senators and representatives')}
pick_word = input("Type in the word or number to get the definition : 1.Incumbent, 2.Precinct, 3.Electoral College")
for words in word_meaning:
   for i in words:
       if pick_word == i:
           print(words[1], ':',word_meaning[words])
