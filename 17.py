#check if the entered character is vowel or not!

a = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
char = input("Enter a character : ")
if char in a:
    print(char, "is a vowel!")
else :
    print(char, "is a consonant")
