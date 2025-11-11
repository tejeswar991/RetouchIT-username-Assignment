v = "aeiou"
word = input("Enter a Word : ").lower()
vowel_count =0
consonant_count =0
for char in word:
    if char in v:
        vowel_count += 1
    else:
        consonant_count += 1
print(f"Total Vowels in {word} is : ",vowel_count)
print(f"Total Consonants in {word} is : ",consonant_count)

# Program to count vowels and consonents in given word
class Word_Count:
    def __init__(self, word):
        v = "aeiou"
        vowel_count = 0
        consonant_count = 0
        for char in word.lower():
            if char in v:
                vowel_count += 1
            else:
                consonant_count += 1

        print("Vowels:", vowel_count)
        print("Consonants:", consonant_count)
word = input("Enter a word : ")
obj = Word_Count(word)

