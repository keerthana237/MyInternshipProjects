import time

# Game state variables
artifact_power = None
village_prosperity = 0

def introduction():
    print("Welcome to 'The Enchanted Quest'!")
    time.sleep(1)
    print("You stand at the edge of the Enchanted Forest, ready to embark on your adventure.")
    time.sleep(1)
    print("Your goal is to find the legendary artifact hidden within the forest.")
    time.sleep(1)
    print("Your actions will shape the outcome of the village and your own fate.")
    time.sleep(1)

def chapter_1():
    global village_prosperity
    print("\nChapter 1: The Forest's Edge")
    time.sleep(1)
    print("You can:")
    print("1. Enter the forest without hesitation.")
    print("2. Search for a guide or a map in the nearby village.")
    print("3. Turn back and abandon the quest.")

    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        print("You enter the forest with determination.")
    elif choice == "2":
        print("You decide to seek guidance from the village.")
        time.sleep(1)
        village_prosperity += 1  # Village prosperity increases
    elif choice == "3":
        print("You abandon the quest and return to the village.")
        time.sleep(1)
        village_prosperity -= 1  # Village prosperity decreases

def chapter_2():
    global village_prosperity
    print("\nChapter 2: Paths Untraveled")
    time.sleep(1)
    print("You can:")
    print("1. Follow the well-worn path.")
    print("2. Take the hidden, overgrown trail.")
    print("3. Cross a rickety bridge over a chasm.")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        print("You follow the well-worn path, which leads to a peaceful grove with a sparkling stream.")
        time.sleep(1)
        village_prosperity += 2  # Village prosperity increases
    elif choice == "2":
        print("You take the overgrown trail, encountering strange flora and fauna. You find a hidden glade.")
    elif choice == "3":
        print("You cross the rickety bridge, barely making it to the other side. You've saved time, but at a risk.")

def chapter_3():
    global artifact_power
    print("\nChapter 3: Mysterious Encounters")
    time.sleep(1)
    print("You can:")
    print("1. Befriend a talking squirrel.")
    print("2. Assist a mischievous forest spirit in a prank.")
    print("3. Defend yourself against a territorial woodland guardian.")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        print("The talking squirrel becomes your helpful guide, leading you deeper into the forest.")
    elif choice == "2":
        print("You assist the forest spirit, which rewards you with a magical charm that aids your quest.")
        artifact_power = "Charm of the Forest"
    elif choice == "3":
        print("You engage in a battle with the guardian and win, gaining respect among forest creatures.")
        artifact_power = "Guardian's Strength"

def chapter_4():
    global artifact_power
    print("\nChapter 4: The Hidden Glade")
    time.sleep(1)
    print("You can:")
    print("1. Search the glade for clues.")
    print("2. Meditate and wait for a vision.")
    print("3. Attempt to leave the glade, fearing traps.")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        print("You find a hidden inscription that reveals the location of the artifact.")
    elif choice == "2":
        print("While meditating, you receive a vision, guiding you to the artifact's exact location.")
    elif choice == "3":
        print("As you attempt to leave, you trigger a trap that leads to an underground chamber containing the artifact.")

def chapter_5():
    global village_prosperity
    print("\nChapter 5: The Confrontation")
    time.sleep(1)
    print("You can:")
    print("1. Engage in a battle with the spirit.")
    print("2. Attempt to negotiate with the spirit.")
    print("3. Try to steal the artifact and make a quick escape.")
    global artifact_power
    choice = input("Enter your choice (1/2/3): ")
    success= None
    if choice == "1" and artifact_power=="Guardian's Strength":
        print("You engage in a fierce battle with the spirit, and after a hard-fought struggle, you defeat it.")
        time.sleep(1)
        success = True
    elif choice == "2" and artifact_power=="Charm of the Forest":
        print("You attempt to negotiate with the spirit, explaining your quest and seeking its cooperation.")
        time.sleep(1)
        print("The spirit agrees to share its power, forming a unique bond with you.")
        success=True
    elif choice == "3":
        print("You make a daring attempt to steal the artifact while the spirit is distracted.")
        time.sleep(1)
        print("you failled to escape from the spirit after stealing the artifact")
        success=False
    else:
        print("you failled to retrive the artifact")
        success=False
    print(village_prosperity)
    print(success)

    if success==True and village_prosperity>0:
        print("congratualtions, youve completed the quest gloriously")
    else:
        print(" you failled your mission.")

if __name__ == "__main__":

        introduction()
        chapter_1()
        chapter_2()
        chapter_3()
        chapter_4()
        chapter_5()

