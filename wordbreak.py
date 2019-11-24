import sys
from nltk.corpus import machado
from tqdm import tqdm


def word_break(vocab, word):
    if len(word) == 0:
        yield []

    else:
        length = len(word)
        for i in range(1, length+1):
            # Have prefix on vocab
            sub_string = word[:i]
            if sub_string not in vocab:
                continue
            for each in word_break(vocab, word[i:]):
                yield [sub_string] + each


if __name__ == "__main__":
    word = sys.argv[1]
    idx = machado.fileids()
    vocab = []
    for i, each in tqdm(enumerate(idx)):
        vocab.extend(machado.words(each))
    vocab = set(vocab)
    vocab = list(vocab)
    for result in word_break(vocab, word):
        print(result)
