import re

def count_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    return len(sentences)
def count_letters(text):
    letter_count = sum(char.isalpha() for char in text)
    return letter_count

sentence = str(input())
num_letters = count_letters(sentence)
words = len(sentence.split())
num_sentences = count_sentences(sentence)
L = (num_letters / words) * 100
S = (num_sentences / words ) * 100
CLI = 0.0588 * L - 0.296 * S - 15.8
print("Grade",end=" ")
print(round(CLI))
