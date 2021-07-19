from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
from random import choice, choices
from re import match

all_tokens = []
with open(input(), "r", encoding="utf-8") as in_file:
    for line in in_file.readlines():
        tokens = WhitespaceTokenizer().tokenize(line)
        all_tokens += tokens
amount_of_bigrams = len(all_tokens) - 2

trigrams = {}
#  trigram = Head:word1 + word2; Tail: word3
for trigram in range(amount_of_bigrams):
    trigrams.setdefault(f'{all_tokens[trigram]} {all_tokens[trigram + 1]}', []).append(all_tokens[trigram + 2])
for trigram in trigrams:
    trigrams[trigram] = Counter(trigrams[trigram])

for _ in range(10):
    word = choice(list(trigrams.keys()))
    while match(r"[A-Z].*[a-z]\ .+\Z", word) is None:
        word = choice(list(trigrams.keys()))
    result_sentences = word.split()
    while len(result_sentences) < 5 or result_sentences[-1][-1] not in "?.!":
        trigram = dict(trigrams[word])
        word = choices(list(trigram.keys()), weights=list(trigram.values()))[0]
        result_sentences.append(word)
        word = f'{result_sentences[-2]} {result_sentences[-1]}'
    print(*result_sentences)
