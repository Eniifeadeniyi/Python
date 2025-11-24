def count_occurrence(sentence, element):
    count = 0
    for word in sentence.split(" "):
        if word.lower() == element.lower():
            count += 1
    return count

def search_for_element(sentence,element):
    count = 0
    start = ()
    for letter in sentence:
        for char in element:
            if letter.lower == char.lower():
                print("hi")
                start += (count,)


paragraph = input("Enter a paragraph: ")
key_word = input("Enter a word to search for: ")
print("Occurence -> " + str(count_occurrence(paragraph, key_word)))
search_for_element(paragraph, key_word)