#####SETUP#####
from collections import Counter
import random
#open and convert the sample text file into a  lowercase list
frequencyOfLettersInEnglish = list("etaoinsrhdlucmfywgpbvkxqjz")
sample = open("sample.txt", "r")
samlist = list(sample.read().lower())
#get a normal alphabet text set and make a scrambled one
alp = list("abcdefghijklmnopqrstuvwxyz")
alps = sorted(alp, key = lambda x: random.random())
scrambled = []
#use the two alphabet text sets to match and scramble the text, append to the "scrambled" array
for i in samlist:
    try:
        scrambled.append(alps[alp.index(i)])
    except ValueError:
        scrambled.append(i)
print("".join(scrambled))
###############
        
#####MAIN#####
scramsorted = []
c = Counter([i for i in scrambled if i in alp]).most_common(26)
for i in range(26):
    scramsorted.append(c[i][0])
for i in scrambled:
    try:
        i = frequencyOfLettersInEnglish[scramsorted.index(i)]
    except ValueError:
        pass
print("".join(scrambled))
print(c)
############### Decryption


