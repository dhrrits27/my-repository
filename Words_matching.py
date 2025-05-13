def match_words(words):
    ctr=0
    lst=[]

    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

            print("list of word with the same first and last character: ",lst)
    return ctr

count=match_words(['abd','dsd','pdp','rse','yhg'])
print("no of words having the same first and last character are: ",count)