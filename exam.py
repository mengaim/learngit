###阶梯电价
##cost=0
##a=eval(input())
##if a<0:
##    print("Invalid Value!")
##elif a<=50:
##    cost =0.53*a
##    print("cost = {:.2f}".format(cost))
##else:
##    cost =26.5 + (a-50)*0.58
##    print("cost = {:.2f}".format(cost))
##

###摄氏温度转华氏温度
##c=eval(input())
##f= c * 1.8 + 32
##print(f)


####多说几遍我爱你
##str=input()
##
##name=str.split(" ")
##strout=name[0]+"我爱你"*eval(name[1])
##print(strout)


####jmu-Java&Python-统计文字中的单词数量并按出现次数排序
from operator import itemgetter, attrgetter
result=""
while 1:
    a = input()
    if(a=="!!!!!"):
        break
    else:
        result += ' '
        result += a
result=result.lower()
for ch in '!.,:*?':
    result=result.replace(ch," ")
words=result.split()
counts={}
countsum=0
for word in words:
    counts[word]=counts.get(word,0)+1
for di in counts:
    countsum +=counts[word]    
print(countsum)
items=list(counts.items())
items.sort(key=lambda item:(-item[1],item[0]))

for i in range(10):
    word,count=items[i]
    print("{}={}".format(word,count))


#jmu-python-涨工资
##lisa=[]
##gz=input()
##lis=gz.split()
##for ls in lis:
##    ls1=eval(ls)
##    if ls1<5000:
##        zgz=ls1*1.5
##        lisa.append(zgz)
##    else:
##        lisa.append(ls1)
##print(" ".join(map(str,lisa)))


##inputThings = []
##a = input()
##while a != '!!!!!':
##    inputThings += [' ']
##    inputThings += a
##    a = input()
##wordCount = []
##inputThingsCount = len(inputThings)
##inputThingsCountMinusOne = int(inputThingsCount) - 1
##wordStartSpace = 0
##wordEndPlace = 0
##inputThings.insert(0, " ")
##inputThings.insert(len(inputThings), " ")
##flag = 0
##for whichLetter in range(len(inputThings)):
##    if inputThings[whichLetter - 1] == ' ' and inputThings[whichLetter] != ' ':
##        flag += 1
##        wordStartSpace = whichLetter
##    if inputThings[whichLetter] != ' ' and inputThings[whichLetter + 1] == ' ':
##        flag += 1
##        wordEndPlace = whichLetter
##    if flag == 2:
##        sub = inputThings[wordStartSpace:wordEndPlace + 1]
##        sub = "".join(sub)
##        flag = 0
##        if sub not in wordCount:
##            wordCount += [sub]
##print(len(wordCount))
##wordCount.sort() 
##if len(wordCount) > 10:
##    for whichOne in range(10):
##        print(wordCount[whichOne])
##else:
##    for whichOne in range(len(wordCount)):
##        print(wordCount[whichOne])
