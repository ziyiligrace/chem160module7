import sys
from os import path
filename=input("Enter the name of the file:")
if not os.path.exists(filename):
        sys.exit("Cannot find file given")
file=open(filename,"r")
while 1:
    line=file.readline() #read next line from stdin into "line"
    print(line, end="")  #print line (end="" skips extra linefeed)
    if line=="":   #quit while loop if line is empty
        break
    word.extend(line.split())
words_lower=[]
for i in words:
    words_lower.append(i.lower())
words=words_lower
counts=Counter(words)
for i in count:
    print("%2d: %s"%(counts[i],i))