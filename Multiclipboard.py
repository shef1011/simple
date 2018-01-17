import os
#Grammar=['ADJECTIVE','NOUN','ADVERB','VERB']
t=open('C:\\Users\\Admin\\Desktop\\para.txt')
k=t.read()
li=['ADJECTIVE','VERB','ADVERB','NOUN']
s=[]
for word in k.split():
    if word.strip('.|?|,|!') in li:
        print("Enter "+ str(word.strip('.|?|,|!')) +":\n")
        x=input()
        s.append(str(x))
    else:
        s.append(str(word))
p=open('C:\\Users\\Admin\\Desktop\\para.txt','w')
p.write(' '.join(s))
p.close()
