import time  # enabels the use of time commands
import sys  # enables system comm


def calc():  # A simple Calculator
    time.sleep(0.75)
    print("Welcome To The Calculator")
    num_1 = int(input("- "))
    num_2 = int(input("- "))
    print(num_1 + num_2)
    time.sleep(0.5)
    calc2()


def calc2():
    print("do another calculation \"again\" or go back?")
    cq_1 = input("- ")
    if cq_1 == "again":
        calc()
    elif cq_1 == "back":
        print("Go back to calculate another day")
        choose()
    else:
        print("invalid input...")
        time.sleep(0.5)
        calc2()


def prgrm():  # a small introduction to the program
    print("Welcome to \"AJAY\"")
    time.sleep(0.5)
    print("AJAY is a little text based adventure with alot of choices")
    time.sleep(0.5)
    print("i would describe is as a book where you get to decide what the main charecter does...")
    time.sleep(0.5)
    print("Have fun playing!")
    choose()


def choose():  # asks the user what fuction he/she wants to use
    print("What do you want to do? calc, game or exit")
    choose_2()


def choose_2():
    q_3 = input("- ")
    if q_3 == "calc":
        calc()
    elif q_3 == "exit":
        sys.exit
    elif q_3 == "game":
        game_1choise()
    else:
        print("invalid input")
        time.sleep(1)
        choose_2()


def main():  # The Main Function
    print("Hello user welcome to \"theProgram\"")
    time.sleep(1)
    print("Do you want to start? y/n")
    q_1 = input("- ")
    if q_1 == "y":
        prgrm()
    elif q_1 == "n":
        print("Okay bye!")
        time.sleep(1)
        print("exiting TheProgram...")
        time.sleep(0.5)
        sys.exit
    else:
        print("Thats Not A valid Input")
        print("You Should Enter \"y\" or \"n\"")
        time.sleep(0.5)
        main()


def game_1choise():
    print("welcome to \"A journey Awaits you...\"")
    time.sleep(0.75)
    print("if you want to play press \"y\" if you want to go back type \"back\"")
    gq_1 = input("- ")
    if gq_1 == "y":
        game_2()
    elif gq_1 == "back":
        choose()
    else:
        print("invalid input...")
        time.sleep(1)
        game_1choise()


def game_2():
    time.sleep(1)
    print("lets begin, Aaron")
    time.sleep(1)
    print("you wake up knowing nothing about where you are and what you are")
    time.sleep(1)
    print("the only thing you know is that you have to get back to where you don't know...")
    time.sleep(1)
    print("but sheer instinct tells you that you need start walking")
    time.sleep(1)
    print("walk to the \"mountain\" in the distance or explore the \"forest\" nearby")
    game_2choise()


def game_2choise():
    gq_2 = input("- ")
    if gq_2 == "forest":
        forest()
    elif gq_2 == "mountain":
        mountain()
    else:
        print("invalid input...")
        time.sleep(1)
        game_2choise()


def mountain():
    print("you walked to the mountain it was a though walk but you made it...")
    time.sleep(1)
    print("after ours of walking you finally arrive at the mountain")
    time.sleep(1)
    print("you see a cave entrance:\"cave\" but also a light coming from the top of the mountain:\"top\"")
    mountainchoise()


def mountainchoise():
    gq_4 = input("- ")
    if gq_4 == "cave":
        cave()
    elif gq_4 == "top":
        mountaintop()
    else:
        print("invalid input...")
        time.sleep(1)
        mountainchoise()


def mountaintop():
    print("you begin your journey to the top...")
    time.sleep(0.5)
    print("as you walk a blizzard starts kicking in")
    time.sleep(0.5)
    print("you keep walking...")
    time.sleep(0.5)
    print("but after half an our the blizzard starts getting worse")
    time.sleep(0.5)
    print("\"keep walking\" or \"build shelter\"")
    MNT_choise()


def MNT_choise():
    gq_12 = input("- ")
    if gq_12 == "keep walking":
        mountaintop_2()
    elif gq_12 == "build shelter":
        MNT_shelter()
    else:
        MNT_choise()


def MNT_shelter():
    print("you dig a tiny cave in the snow and cover it up with sticks, there are no more leaves at this altitude")
    time.sleep(0.5)
    print("its getting dark outside...")
    time.sleep(0.5)
    print("you could try to dig a hole and make a \"fire\" or \"sleep\" and don't waste any energy")
    MNT_shelter_choise()


def MNT_shelter_choise():
    question13 = input("- ")
    if question13 == "fire":
        MNT_fire()
    elif question13 == "sleep":
        MNT_sleep()
    else:
        MNT_shelter_choise()

def MNT_sleep():
    print("WIP")

def MNT_fire():
    print("WIP")

def mountaintop_2():
    print("You decide to continue walking")
    time.sleep(0.5)
    print("The blizzard keeps getting worse...")
    print("I i.. is this how I die? you think to yourself")
    time.sleep(0.5)
    print("you ignore the freezing cold and keep walking nontheless")
    end_4()


def end_4():
    print("...")
    print("...")
    print("You can't move your fingers, your head is foggy")
    time.sleep(0.5)
    print("everything begins to fade")
    time.sleep(0.5)
    print("\"If only I had built a shelter first\", you think to yourself as the sky clears")
    time.sleep(2.5)
    print("And you slowly die...")
    aorb()


def cave():
    print("you wander around a bit ")
    time.sleep(0.5)
    print("but after a while you get sleepy")
    time.sleep(0.5)
    cave_2()


def cave_2():
    print("you can \"explore\" further or get some \"sleep\"")
    gq_9 = input("- ")
    if gq_9 == "explore":
        deepcave()
    elif gq_9 == "sleep":
        cave_3()
    else:
        print("invalid input...")
        time.sleep(0.5)
        cave_2()


def cave_3():
    print("You find a good spot to sleep and decide to call it a day...")
    time.sleep(0.5)
    print("its about 9AM you slowly wake up")
    time.sleep(0.5)
    print("you look at your hand and see that you are in a log cabin")
    time.sleep(0.5)
    print("your hands are tied together with duct tape")
    time.sleep(0.5)
    print("you can try to \n"escape"\n or \n"wait"\n")
    cave_3choice()
    
def cave_3choice():
    print("you can try to \n"escape"\n or \n"wait"\n")
    gq_cave = input("- ")
    if gq_cave == "wait":
        forest_tied()
    elif gq_cave == "escape":
        cabin()
    else:
        print("invalid input...")
        time.sleep(0.5)
        cave_3choice()
        
def forest_ties:
    print ("WIP")

def deepcave():
    print("WIP")


def forest():
    print("you chose to explore the forest")
    time.sleep(1)
    print("as you walk you get a feeling that your being followed...")
    time.sleep(1)
    print("you see a little cabin in the distance is seems there's light, enter the cabin:\"y/n\"?")
    forestchoise()


def forestchoise():
    gq_3 = input("- ")
    if gq_3 == "y":
        cabin()
    elif gq_3 == "n":
        DeepForest()
    else:
        print("invalid input...")
        time.sleep(1)
        forestchoise()


def deepforest():
    print("you walk deep into the forest, deeper and deeper and deeper...")
    time.sleep(0.5)
    print("after ours of walking you think \"i should really get some sleep\"")
    time.sleep(0.5)
    print("you decide to try and find shelter")
    time.sleep(0.5)


def cabin():
    print("you open the door, there is a fire in the fireplace but no one is home")
    time.sleep(1)
    print("you decide to eat and get some rest")
    time.sleep(1)
    print("you've eaten and are very tired you go to bed...")
    time.sleep(1)
    print("right as you fall asleep you hear a loud knock on the door, \"BAM BAM BAM\"")
    time.sleep(1)
    print("confused and scared you awnser: \"y...yes\"")
    time.sleep(1)
    print("a loud but rather deep voice awnsers:GET OUT OF THE HOUSE OR WE WILL BLOW IT UP!")
    time.sleep(1)
    print("you realise you don't have alot of time nor choises what should you do?")
    time.sleep(1)
    print("open the suspicious looking trap door on the ground:\"open trap door\" or obey the loud man:\"obey man\"")
    traporobey()


def traporobey():
    gq_5 = input("- ")
    if gq_5 == "open trap door":
        basement()
    elif gq_5 == "obey man":
        end_1()
    else:
        print("invalid input...")
        time.sleep(1)
        traporobey()


def end_1():
    print("you decide to obey the man, you open the door")
    time.sleep(1)
    print(
        "you hear a loud BENG and you feel steel touching your head, but as you try to respond everything goes black...")
    time.sleep(1)
    print("you hear a womens voice whispering in your ear \"Aaron, Aaron! you have to try again...\"")
    time.sleep(1)
    aorb()


def aorb():
    print("go \"back\" or try \"again\"")
    gq_6 = input("- ")
    if gq_6 == "again":
        game_2()
    elif gq_6 == "back":
        choose()
    else:
        print("invalid input...")
        time.sleep(1)
        aorb()


def basement():
    print("you fall 2 meters and land on your knee, you think your leg is broken you need medical attention fast")
    time.sleep(0.5)
    print("you call for help, to your suprise someone awnsers...")
    time.sleep(0.5)
    print("you're not supposed to be here Aaron...")
    time.sleep(0.5)
    print("how does he know my name?!?!")
    time.sleep(0.5)
    print("scream \"help\" or try to \"crawl\" away...")
    basementchoise()


def basementchoise():
    gq_7 = input("- ")
    if gq_7 == "help":
        basement2()
    elif gq_7 == "crawl":
        basement4()
    else:
        print("invalid input...")
        time.sleep(1)
        basementchoise()


def basement2():
    print("the man aproaches you slowly you think he means no harm...")
    time.sleep(0.5)
    print("until you you see his fist moving towards your face, you try to duck but its too late everything goes black")
    time.sleep(5)
    print("no... this is not the end")
    time.sleep(0.5)
    print("you gently open your eyes only to be blinded with a bright light")
    time.sleep(0.5)
    print("as you get used to the light you realise your in a cage...")
    time.sleep(0.5)
    print("you see a sign it sais: \"SEA members captured: 1...")
    time.sleep(0.5)
    print("...{SEA stands for: SpaceExplorationAgency, you are apart of SEA}...")
    time.sleep(0.5)
    print("you have two options \"scream\" or \"accept\" your fate...")
    basement2choise()


def basement2choise():
    gq_8 = input("- ")
    if gq_8 == "scream":
        basement3()
    elif gq_8 == "accept":
        end_2()
    else:
        print("invalid input...")
        time.sleep(0.5)
        basement2choise()


def end_2():
    print("after ours or days or month of waiting you slowly realise...")
    time.sleep(0.5)
    print("t... this")
    time.sleep(0.5)
    print("is the end")
    time.sleep(0.5)
    print("your sense of time and reality are gone")
    time.sleep(0.5)
    print("slowly everything fades away")
    time.sleep(3)
    print("goodbye...")
    time.sleep(3)
    choose()


def basement3():
    print("you scream for help it doesn't seem to help")
    time.sleep(0.5)
    print("after a while you give up")
    time.sleep(0.5)
    print("to your suprise somepne enters the room filled with caches")
    time.sleep(0.5)


def basement4():
    print("you try to crawl away, but your almost certant its a losthope")
    print("until the man trips and falls, you think \"this is my chance\"")
    print("you open the door and lock it, but the lock looks rather fragile")
    print("you hear the man struggling outside")
    print("there are alot of things inside the rectangle shaped room")
    print("a pile of wooden boards, they seem to fit in the hooks next to the door")
    print("a medkit, for your broken leg")
    print("you also see a red door")
    print("these are your choises:")
    print("1. \"barricade\" the \"door\"")
    print("2. \"enter\" the red \"door\"")
    print("3. \"use\" the \"medkit\" for your leg")
    print("4. go back outside to \"finish\" the \"man\" now he's still in shock")
    basement4choise()


def basement4choise():
    gq_10 = input("- ")
    if gq_10 == "barricade door":
        end_3()
    elif gq_10 == "enter door":
        basement5()
    elif gq_10 == "use medkit":
        test()
    elif gq_10 == "finish man":
        test()
    elif gq_10 == "secret":
        dream_ending()
    else:
        print("invalid input..")
        time.sleep(1)
        basement4choise()


def dream_ending():
    print("you hear a voice calling you...")
    time.sleep(0.5)
    print("you slowly open your eyes, a women looking around her 50's greets you")
    time.sleep(0.5)
    print("it's your mom...")
    time.sleep(0.5)
    print("you think to yourself: \"that was one hell of a dream\"")
    time.sleep(5)
    aorb()


def basement5():
    print("you see a ladder running up to a vault style looking door")
    time.sleep(0.5)
    print("you climb the ladder and open the door")
    time.sleep(0.5)
    print("you open the door and climb outside, you immediatly smell something wierd")
    time.sleep(0.5)
    print("you turn around and see that the little cabin is blown up you think \"huh that man outside wasn't joking\"")
    time.sleep(0.5)
    print("what should you do now?")
    time.sleep(0.5)
    print("walk to the \"mountain\" after al or explore deeper into the \"forest\"")
    basement5choise()


def basement5choise():
    gq_11 = input("- ")
    if gq_11 == "mountain":
        mountain()
    elif gq_11 == "forest":
        deepforest()
    else:
        print("invalid input...")
        time.sleep(0.5)
        basement5choise()


def end_3():
    time.sleep(0.5)
    print("you slowly pick up the beams and try to put them into the hooks")
    time.sleep(0.5)
    print("right as you lift one of the beams the man kicks in the door")
    time.sleep(0.5)
    print("he has a gun...")
    time.sleep(0.5)
    print("you can almost see the craze in his raging eyes")
    time.sleep(0.5)
    print("you already know this is the end...")
    time.sleep(0.5)
    print("the man pulls the trigger and the world around you fades away, accompanied with a sharp pain in your chest")
    time.sleep(0.5)
    aorb()


# a function that serves no purpose it is only called for tests DO NOT REMOVE CAN BE VITAL TO TEST FUNCTIONS
def test():
    print("it worked")


main()

