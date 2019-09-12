import nltk
from math import sqrt,log
from nltk.corpus import stopwords

stop_words = list(stopwords.words('english'))

corpus = [text1,text2,text3]

def idf_matrix(corpus):
    word_list = []
    frequency_of_words_in_each_document = [{}]
    for document_number in range(len(corpus)):
        tempList = list(nltk.word_tokenize(corpus[document_number]))
        frequency_of_words_in_each_document.append({})
        for word in tempList:
            if word not in stop_words:
                if word not in word_list:
                    word_list.append(word)
                if word not in frequency_of_words_in_each_document[document_number].keys():
                    frequency_of_words_in_each_document[document_number][word] = 1
                else:
                    frequency_of_words_in_each_document[document_number][word]+=1
    matrix = [[]]
    for word_number in range(len(word_list)):
        matrix.append([])                                     #for initializing empty list
        for document_number in range(len(corpus)):
            if word_list[word_number] in frequency_of_words_in_each_document[document_number].keys():
                matrix[word_number].append(frequency_of_words_in_each_document[document_number][word_list[word_number]])
            else:
                matrix[word_number].append(0)
    del(matrix[len(matrix)-1])
    word_occurence_list = []
    for i in range(len(matrix)):
        word_occurence_list.append(0)
        for j in range(len(matrix[i])):
            if matrix[i][j]!=0:
                word_occurence_list[i]+=1
    for i in range(len(word_occurence_list)):
        for j in range(len(corpus)):
            if matrix[i][j]!=0:
                matrix[i][j] *= log(word_occurence_list[i]/len(corpus),2)
                
    return matrix
if __name__ == "__main__":
    matrix = idf_matrix(corpus)
    for i in range(len(matrix)):
        print()
        for j in range(len(matrix[i])):
            print(round(matrix[i][j],2),end="\t")