import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("INTERMEDIATE/day26/project/nato_data.csv")
# print(data.to_dict())

alphabet_data = {row.letter: row.code for (index, row) in data.iterrows()}
# print(alphabet_data)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def alphabet_function():
    word = input("Enter a word: ").upper()
    try:
        output = [alphabet_data[letter] for letter in word]
    except KeyError:
        print("Sorry only letters are supported in alphabet")
        alphabet_function()
    else:
        print(output)

alphabet_function()