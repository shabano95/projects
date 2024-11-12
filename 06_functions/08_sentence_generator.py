def make_sentence(word, part_of_speech):
    # Check the part of speech and construct the sentence accordingly
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    word = input("Please type a noun, verb, or adjective: ")  # Get the word from user
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))  # Get part of speech
    make_sentence(word, part_of_speech)  # Call the function to print the sentence

# Call the main function to start the program
if __name__ == "__main__":
    main()
