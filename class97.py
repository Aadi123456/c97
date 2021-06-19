 introstring = input('Enter your introduction')
 print(introstring)
 characterCount=0
 wordCount=1
 for a in introstring:
     characterCount=characterCount+1
     print(characterCount)
     if (a==' '):
        (wordCount=wordCount+1)
print('Number of words in string')
print (wordCount)
print('Number of characters in string')
print (characterCount)