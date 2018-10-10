#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string
import nltk

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated)

        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)

        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    stemmer = SnowballStemmer("english", ignore_stopwords=True)
    stemmer2 = SnowballStemmer("english", ignore_stopwords=True)
    print(stemmer2.stem("having"))
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        # words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        raw_words = nltk.word_tokenize(text_string)

        after_words = []
        for i in range(len(raw_words)):
            after_words.append(stemmer.stem(raw_words[i]))

        words = ' '.join(after_words)
    return words



def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()

