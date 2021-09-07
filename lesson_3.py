# Set the variable in_list to whatever value you want. Let's use 
# [ 5, 2, 3, 1, 4, 6, 8, 7 ] as an example.

# Use for loops, while loops, and whatever else we've learned to 
# set the variable x to the length of in_list - but you may NOT use len! 
# Try to mimic the behavior of len.

################################################

# Create a program to accept words from a user, and add them to a dictionary.
# At the end, use print(mydict) to print out the user's work to them

################################################

# Extend your dictionary program from assignment #2 to have some added capabilities:

# Make sure the user cannot enter more than one translation for the same word, 
# in either direction. For example, if ‘dog’: ‘Hund’ is already an entry in the 
# dictionary, then adding a new translation for ‘dog’ OR another word that translates 
# to ‘Hund’ should fail.

# Make sure the user cannot input a key that contains a space, but a value that 
# contains a space is acceptable. So adding ‘the dog’ : ‘Hund’ should fail, but 
# ‘dog’ : ‘der Hund’ is fine.

################################################

# Instead of printing out the dictionary when the program is done, ask the user 
# for a sentence and “translate” it, word-by-word, as output. 

# If a word has no translation, use the word unchanged.

################################################

from typing import List


def length_of_list(in_list: list) -> int:
    """
    :param in_list: A list.
    :return: The length of <code>in_list</code>.
    """
    x: int = 0
    for _ in in_list:
        x = x + 1
    return x


def dictionaries() -> dict:
    """
    Generates a dictionary.
    :return: The generated dictionary.
    """
    mydict: dict = {}
    while True:
        word: str = input("Enter a word:\n")
        mydict[word]: str = input(f"Enter a translation for the word \"{word}\":\n")
        add_another: str = input("Word recorded! Would you like to add another word? (y/n) ")
        if add_another.lower() != "y" and add_another.lower() != "yes":
            break
    return mydict


def dictionaries_extended() -> dict:
    """
    Generates a dictionary, but with checking for spaces in words as well as duplicate words or translations.
    :return: The generated dictionary.
    """
    mydict: dict = {}
    while True:
        word: str = input("Enter a word:\n")
        # check for spaces
        if " " in word:
            add_another: str = input(
                "Whoops, you cannot enter a word that contains a space! Enter another word? (y/n) ")
            if add_another.lower() != "y" and add_another.lower() != "yes":
                break
            else:
                continue
        # check for duplicated key
        if word in mydict:
            add_another: str = input("Whoops, that word is already in the dictionary! Enter another word? (y/n) ")
            if add_another.lower() != "y" and add_another.lower() != "yes":
                break
            else:
                continue
        translation: str = input(f"Enter a translation for the word \"{word}\":\n")
        # check for duplicated value
        if translation in mydict.values():
            add_another: str = input(
                "Whoops, there is already a word with that translation! Enter another word? (y/n) ")
            if add_another.lower() != "y" and add_another.lower() != "yes":
                break
            else:
                continue
        mydict[word]: str = translation
        add_another: str = input("Word recorded! Would you like to add another word? (y/n) ")
        if add_another.lower() != "y" and add_another.lower() != "yes":
            break
        else:
            continue
    return mydict


def translate(translate_dict: dict) -> str:
    """
    Translates a given sentence using the dictionary and prints the output.
    :param translate_dict: The dictionary to use in translating the sentence.
    :return: The translated sentence.
    """
    original_sentence_list: List[str] = (
        input("Successfully created your dictionary! Enter a sentence to translate:\n")
    ).split(" ")
    translated_sentence_list: List[str] = []
    for word in original_sentence_list:
        translated_sentence_list.append(translate_dict[word] if word in translate_dict else word)
    translated_sentence: str = " ".join(translated_sentence_list)
    print(f"Here is your translated sentence:\n{translated_sentence}")
    return translated_sentence


def main():
    try:
        length_of_list(in_list=[1, 3, 5, 7, 9, 2, 4, 6, 8])
        use_extended: str = input("Would you like to use the extended version of the dictionary generator, "
                                  + "instead of the normal version? (y/n) ")
        dictionary = dictionaries() if use_extended != "y" and use_extended.lower() != "yes"\
            else dictionaries_extended()
        translate(translate_dict=dictionary)
    except Exception:
        print("Whoops, an unknown error occured! Please report this.")


if __name__ == "__main__":
    main()
