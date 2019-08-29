import nltk
from math import sqrt,log
from nltk.corpus import stopwords

stop_words = list(stopwords.words('english'))

def bi_gramDict(wordsList):
    bigram = {}
    lis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for a in lis:
        for b in lis:
            bigram[a+b] = []
            for word in wordsList:
                if a+b in word:
                    bigram[a+b].append(word)
    return bigram
def uni_gramDict(wordsList):
    unigram = {}
    lis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for a in lis:
        unigram[a] = []
        for word in wordsList:
            if a in word:
                unigram[a].append(word)
    return unigram
def printSimilarWord(queryWord):
    unigram = uni_gramDict(stop_words)
    #print(unigram)
    bigram = bi_gramDict(stop_words)
    #print(bigram)
    similarWord = {}
    for letter in queryWord:
        for word in unigram[letter]:
            if word not in similarWord.keys():
                similarWord[word] = 1
            else:
                similarWord[word] += 1
    for i in range(len(queryWord)-1):
        for word in bigram[queryWord[i]+queryWord[i+1]]:
            if word in similarWord.keys():
                similarWord[word] += 1
            else:
                similarWord[word] = 1
    word = ""
    count = 0
    #print(similarWord)
    for i in similarWord.keys():
        if similarWord[i]>count and similarWord[i]<2*len(queryWord):
            word = i
            count = similarWord[i]
    return word
        
    
if __name__ == "__main__":
    print(printSimilarWord("hsi"))