#Request user for two words
#Create a function and pass in a parameter
#using sorted,sort the two strings
#if the two strings are equal,it is an anagram.
#End function
def subject(word):
    word=str(input("Enter start"))
    a=str(input("Enter a word "))
    b=str(input("From your word,think of another word "))
    new_string=sorted(a)
    new_stringb=sorted(b)
    if new_string==new_stringb:
        print("Yay,you have found the two anagrams")
    else:
        print("You can try again ")


