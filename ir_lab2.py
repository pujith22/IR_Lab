#for finding similarity of documents using vector product
import nltk
from nltk.corpus import stopwords
from math import sqrt
text1 ="""is the collective name for two late-15th-century portrait panels by the
German painter Albrecht Dürer. They show his parents, Barbara Holper and Albrecht
Dürer the Elder, when she was around 39 and he was 63, and are among four paintings
or drawings Dürer made of the couple. The portraits are unflinching records of the 
physical and emotional effects of ageing, which Dürer may have intended either to display
his skill to his parents or as keepsakes while he travelled as a journeyman painter. 
His father's panel is considered the superior work and has been described as one of Dürer's
most exact and honest portraits. The Dürer family was close, and his later writings 
show the love and respect he felt toward his parents. The panels, separated
since at least 1628, were reunited in the """
text2 = """Thanks to a hands-on guide introducing programming fundamentals alongside
topics in computational linguistics, plus comprehensive API documentation, NLTK is
suitable for linguists, engineers, students, educators, researchers, and industry
users alike. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free,
open source, community-driven project."""

list1 = nltk.word_tokenize(text1)
list2 = nltk.word_tokenize(text2)
dict1 = {}
dict2 = {}
stopwords = list(stopwords.words('english'))
for i in list1:
    if i not in dict1.keys():
            dict1[i]=1
    else:
        dict1[i]=dict1[i]+1
for i in list2:
    if i not in dict2.keys():
        dict2[i]=1
    else:
        dict2[i]=dict2[i]+1
dotproduct = 0
for i in dict1.keys():
    if i in dict2.keys():
        dotproduct = dotproduct + dict1[i]*dict2[i]
        
magnitudeSquared1 = 0
magnitudeSquared2 = 0
        
for i in dict1.values():
    magnitudeSquared1= magnitudeSquared1 + i*i

for i in dict2.values():
    magnitudeSquared2 = magnitudeSquared2 + i*i
    
print(dotproduct/(sqrt(magnitudeSquared1)*sqrt(magnitudeSquared2)))