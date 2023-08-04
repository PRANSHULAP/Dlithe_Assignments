def noOfWords(str):
    count = 1
    for i in range(1, len(str) - 1):
        if (str[i].isupper()):
            count=count+1
    return count
 str = input()
print(noOfWords(str))