PLACEHOLDER = "[name]"


with open("C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day24/inputs/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day24/inputs/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day24/outputs/readyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

