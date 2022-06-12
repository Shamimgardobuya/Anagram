#Request user for two words
#Create a function and pass in a parameter
#using sorted,sort the two strings
#if the two strings are equal,it is an anagram.
#End function
# from ast import Str


def subject(word):
    # word=str(input("Enter start"))
    a=str(input("Enter a word "))
    b=str(input("From your word,think of another word "))
    new_string=sorted(a)
    new_stringb=sorted(b)
    leprechaun=["top","opt"]
    if new_string==new_stringb and new_stringb in leprechaun:
        print("Yay,you have found the two anagrams")
    else:
        print("You can try again ")

subject(word=(str(input("Enter start"))))
#converting to list then sort the two list.
#request for 2 users input
#using list comprehension loop through each character.
#sort the two list and compare them 
#if equal are anagrams
#else try again,is there a way  can go back to looping.

#Not all words are anagram .
#Buuut when we sort all the letters rearrange themselvels in an equal way.if equal are anagrams.
#o even if i get to equal characters,not all word are anagram  
#store words somewhere compare by checking
                                                # word1=list(input("Enter a word "))
                                                # word4=list(input("Enter another  word "))
                                                # print(word1)



