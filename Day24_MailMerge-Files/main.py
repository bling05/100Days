#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []
with open("./Input/Names/invited_names.txt") as file:
    for name in file.readlines():
        names.append(name.strip("\n"))

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        new = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")
        new.write(f"{letter.replace('[name]', name)}")