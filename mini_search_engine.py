def count_occurrence(sentence, element):
    count = 0
    for word in sentence.split(" "):
        if word.lower() == element.lower():
            count += 1
    return count

def delete(sentence,end_index):
    return sentence[end_index+1:]

def search_for_element(sentence,element):
    indexes = []
    index = 0
    last = 0
    if sentence.find(element) == -1:
        return "Not found!"
    for _ in range(count_occurrence(sentence, element)):
            index = sentence.find(element,last)
            indexes.append(index)
            last = index + (len(element) - 1)
            indexes.append(last)
    return indexes


paragraph = input("Enter a paragraph: ")
key_word = input("Enter a word to search for: ")
print("Occurence -> " + str(count_occurrence(paragraph, key_word)))
print(search_for_element(paragraph, key_word))