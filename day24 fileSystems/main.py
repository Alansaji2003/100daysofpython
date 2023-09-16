PLACEHOLDER = "[name]"


with open("./invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name.strip())
        print(new_letter)
        with open(f"./Letter_for_{name.strip()}.txt", mode="w") as completed:
            completed.write(new_letter)