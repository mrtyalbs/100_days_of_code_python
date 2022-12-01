import pandas

# Create a dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

letter_list_output = [alphabet_dict[letter] for letter in word]

print(letter_list_output)
