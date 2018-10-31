import time
import sys

totalTime = 0
firstTime = 0
secondTime = 0

sentence = input("Please type in a sentence that you want to use to test your friend.\n")
Slength = len(sentence)
for i in range(25):
    print("\n")
    
def pause():
    time.sleep(0.6)
    
#----------------------the actual game code------------------------
def playing():
    errorFlag = 0
    global Slength
    
    print("You'll need to type in the given sentence as fast as you can.\nCapitals, spaces and punctuations do matter. \nHint: number of characters:",Slength,"\n")
    pause()
    userStart = input("Please type in 's' when you're ready. Press Enter when finished.")

    while True:
        if userStart == "s":
            print("\a","3...")
            pause()
            print("\a","2...")
            pause()
            print("\a","1...")
            pause()
            break
        else:
            userStart = input("Please type in 's' when you're ready.")
        
    print("\n\n\n"+sentence)
    startTime = time.clock() #The user is writing...

    mySentence = input() 
    finishTime = time.clock() 
    print("\nSentence to type:",sentence)
    pause()
    print("       You typed:",mySentence,"\n")
    pause()
    
    MSlength = len(mySentence)
    
    if MSlength > Slength: #Comparing user's sentence to the original sentence (OTW there will be an error in line 62.)
        sentenceLength = Slength
        errorFlag = MSlength - Slength
        
    elif MSlength < Slength:
        sentenceLength = MSlength
        errorFlag = Slength - MSlength
        
    elif MSlength == Slength:
        sentenceLength = Slength

    for i in range (sentenceLength):
        if mySentence[i] != sentence[i]:
            errorFlag += 1 #Looking for errors, char by char.
         
    totalTime = finishTime - startTime
    totalTime = round(totalTime,3)

    if errorFlag == 0:
        print("Perfect! No error found!")
        pause()
    else:
        print("Uh-uh. Your sentence has",errorFlag,"error(s).")
        pause()

    print("Total time taken:",totalTime,"seconds.\n")
    pause()
    
    return [totalTime,errorFlag]
#----------------------------------------------------------------------------

firstTime = playing()

userChoice = input("\nWould you like to try again with the same sentence? (y/n)\n")

while True:
    if userChoice== "n":
        print("\nThank you for playing.")
        sys.exit()
        input()
    
    elif userChoice =="y":
        print("\nAlright. Another go.\n")
        pause()
        break
    
    else:
        userChoice = input("\nWould you like to try again with the same sentence? (y/n)\n")

secondTime = playing()

if firstTime[0] > secondTime[0]:
    difference = round(firstTime[0]-secondTime[0],3)
    print("Your first attempt took more time. You got faster by",difference,"second(s).")
    
elif firstTime[0] < secondTime[0]:
    difference = round(secondTime[0]-firstTime[0],3)
    print("Your second attempt took more time. You got slower by",difference,"second(s).")
    
elif firstTime[0] == secondTime[0]:
    print("Unbelievable! Your first and second attemps took exactly the same time! Are you a computer?")
   

if firstTime[1] > secondTime[1]:
    difference = firstTime[1]-secondTime[1]
    print("Your first attempt had",difference,"more errors than the second one.\n")

elif firstTime[1] < secondTime[1]:
    difference = secondTime[1]-firstTime[1]
    print("Your second attempt had",difference,"more errors than the first one.\n")

elif firstTime[1] ==0 and secondTime[1]==0:
    print("No error for both attempts! Well done!\n")
    
else:
    print("Your first and second attempts had the same number of errors. No improvement.")

print("Thank you for playing. Run the program again to play again!")

input()
