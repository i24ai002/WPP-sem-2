def panagram(sen):
    sentence=sen
    char='a'
    sentence=sentence.lower()#lower case kia uniform banane ke lie
    sentence=sentence.replace(" ", "")#space hata dia
    sentence=set(sentence)#duplicates ko hata dia
    sentence=sorted(sentence)#set tha islie waapas sort kia
    sentence=''.join(sentence)#waapas string bana dia
    if len(sentence)<26:
        return False
    else:
        for letter in sentence:
            if letter.isdigit():
                continue
            if letter==char:
                char=chr(ord(char)+1)
                continue
            else:
                return False
        
    return True
        
        
sen=input("Enter a sentence to check if panagram or not: ")
sen.split()
result=panagram(sen)
if result==False:
    print("Not a panagram!!")
elif result==True:
    print("Panagram!!")