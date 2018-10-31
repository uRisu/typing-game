import time
import sys

totalTime = 0
firstTime = 0
secondTime = 0

sentence = input("Please type in a sentence that you want to use to test your friend.\n")
sentenceLength = len(sentence)

for i in range(25):
    print("\n")
    
def pause():
    time.sleep(0.6)
    
#----------------------the actual game starts from here------------------------
def playing():
    errorFlag = 0
    
    print("You'll need to type in the given sentence as fast as you can.\nCapitals, spaces and punctuations do matter. \nHint: number of characters:",sentenceLength,"\n")
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
        
    print("Start typing!\n\n")
    print(sentence)
    startTime = time.clock() #The user is writing...

    mySentence = input() 
    finishTime = time.clock() 
    print("\nSentence to type:",sentence)
    pause()
    print("       You typed:",mySentence,"\n")
    pause()
    
    for i in range (sentenceLength):
        if mySentence[i] != sentence[i]:
            errorFlag += 1 #Looking for errors, char by char.
            
    totalTime = finishTime - startTime
    totalTime = round(totalTime,3)

    if errorFlag == 0:
        print("Perfect! No error found!")
        pause()
    else:
        print("Uh-uh. Your sentence has",errorFlag,"errors.")
        pause()

    print("Total time taken:",totalTime,"seconds.\n")
    pause()
    
    return totalTime
#------------------------------------to here-----------------------------------------

firstTime = playing()

userChoice = input("\nWould you like to try again with the same sentence? (y/n)\n")

while True:
    if userChoice== "n":
        print("\nThank you for playing.")
        sys.exit()
    
    elif userChoice =="y":
        print("\nAlright. Another go.\n")
        pause()
        break
    
    else:
        userChoice = input("\nWould you like to try again with the same sentence? (y/n)\n")

secondTime = playing()

if firstTime > secondTime:
    difference = round(firstTime-secondTime,3)
    print("Your first attempt took more time. You got faster by",difference,"second(s).\n")
    
elif firstTime < secondTime:
    difference = round(secondTime-firstTime,3)
    print("Your second attempt took more time. You got slower by",difference,"second(s).\n")
    
elif firstTime == secondTime:
    print("Unbelievable! Your first and second attemps took exactly the same amount of time! Are you a computer?\n")

print("Thank you for playing. Run the program again to play again!")
