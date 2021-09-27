introString = input("enter your string:")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount + 1
    if (i==' '):
         wordCount = wordCount + 1
            
print("number of words in your screen:")
print(wordCount)
print("number of characters in your screen:")
print(characterCount)
