#Take user input 
a = input("Enter a word: ")
#program to check break keyword
for i in a: #literate for loop
    if (i == 'a'): #condition 1
        #display result
        print ("A is found")
        break #break statement
    else:
        #display result
        print("A is not found")