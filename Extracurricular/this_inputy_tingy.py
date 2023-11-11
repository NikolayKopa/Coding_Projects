print ("Hi my name is Fishstick and I like swimming in my mum's bathroom which has many interesting POI's like The Volcano, Polar Peak, and Dusty Divot.")
print ("I am a pro gamer and have around 20 top 25's in solos, 1 top 10 in squads and 5 top 20's in duos but I have no wins which is actually bad for your account.")
print ("But even though you have Black Knight, Renegade Raider, Mako Glider, Areal Assualt Trooper, and Recon Expert, I am still more OG and better than you")
print ("Anyway I just wanted to tell you that this isn't a setup for a kidnapping and we are actual friends.")
raw_input ("What is your favorite skin in Fortnite, mine is Jonesy because he is so cute and looks like Tfue?")
print ("*music starts playing*")
print ("*searches up Jonesy's age")
print ("*FBI OPEN UP!!!!!!!!!!!!!!!!") 
names=["John","Bob"]
ages=["3","785"]
print (names)
print (ages) 
raw_input("Based on the article you should have read above, do you think Fishstick is trash?")
print ("Okay fine you think I am bad then I will see how good you are, can you type your name so we could 1v1!") 
print ("By the way can you type your name below even though I insulted you.")
notDone= True 
while (notDone): 
    name = raw_input("Name")
    if(name == ""):
        notDone = False
    else :
        names.append(name)
        age= raw_input("age")
        ages.append(age) 
print (names)
print (ages)
sizeone= len(names)
sizetwo= len(ages)
i=0
while (i<sizeone):
    j= i+1
    while (j<sizeone):
        if(names[i]>names[j]):
            tempone=names[i]
            temptwo=ages[i]
            names[i]=names[j]
            ages[i]=ages[j] 
            names[j]=tempone
            ages[j]=temptwo 
        j=j+1
    i=i+1
print (names) 
print (ages)
