def merge_strings_alternatively(word1,word2):
    merged=[]
    min_length=min(len(word1),len(word2))
    for i in range(min_length):
        merged.append(word1[i])
        merged.append(word2[i])
    
    if len(word1)>min_length:
        merged.extend(word1[min_length:])
    elif len(word2)>min_length:
        merged.extend(word1[min_length:])

    result=''.join(merged)

    return result           



if __name__=="__main__":
    print(merge_strings_alternatively("abcd","de"))
