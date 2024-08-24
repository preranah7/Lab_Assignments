# Write a Python program to compute following operations on Strings
# a)To display word with the longest length
# b)To determine the frequency of occurence of particular character in the String
# c)Check whether given string is palindrome or not
# d)To display index of first apperance of a substring
# e)To count the occurences of each word in a given string.


def longest_word_inThe_string():
    sentence = input("enter a sentence")
    longest_word = ''
    longest_length = 0
    current_word = ""
    current_length = 0
    for char in sentence:
        if char == ' ':
            if current_length > longest_length:
                longest_length = current_length
                longest_word = current_word

            current_length = 0
            current_word = ""
        else:
            current_length += 1
            current_word += char
            
    if current_length > longest_length:
       longest_length = current_length
       longest_word = current_word

    print(longest_word)



def char_occur_count():
  input_string = input("Enter a string: ")
  target_character = input("Enter a character to count: ")
  char_count = 0
  for char in input_string:
    if char == target_character:
        char_count += 1
  print(f"The character '{target_character}' appears {char_count} times in the string.")


def palindrome_check():
 word = input("Enter a word ")
 reverse_word = ""
 for char in word:
    reverse_word = char + reverse_word
    
 print(reverse_word)
    
 if(word == reverse_word):
       print(word," is palindrome")
 else:
       print(word,"is not palindrome")


def first_appearance_of_substring():
    def find_substring_index(main_string, substring):
     len_main = len(main_string)
     len_sub = len(substring)

     for i in range(len_main - len_sub + 1):
        if main_string[i:i + len_sub] == substring:
            return i

     return -1

    main_string = input("enter a string ")
    substring = input("enter substring ")
    index = find_substring_index(main_string, substring)

    if index != -1:
       print(f"The substring '{substring}' first appears at index {index}.")
    else:
      print(f"The substring '{substring}' is not found in the main string.") 


def repeated_word_count():
 input_string = input("Enter a string: ")
 word_count = {}
 current_word = ""
 for char in input_string:
    
    if char == ' ' or char == ',' or char == '.' or char == '!':
        
        if current_word != "":
            if current_word in word_count:
                word_count[current_word] += 1
            else:
                word_count[current_word] = 1
            
            current_word = ""
    else:
       
        current_word += char

# Add the last word if the string doesn't end with a separator
 if current_word != "":
    if current_word in word_count:
        word_count[current_word] += 1
    else:
        word_count[current_word] = 1

# Print the word counts
 for word in word_count:
    print(word + ": " + str(word_count[word]))


while True:
   print("1)To display word with the longest length")
   print("2)To determine the frequency of occurence of particular character in the string")
   print("3)Check whether given string is palindrome or not")
   print("4)To display index of first apperance of a substring")
   print("5)To count the occurences of each word in a given string.")

   choice = input("Enter your choice ")

   if choice == '1':
      longest_word_inThe_string()
   elif choice == '2':
      char_occur_count()
   elif choice == '3':
      palindrome_check()
   elif choice == '4':
      first_appearance_of_substring()
   elif choice == '5':
      repeated_word_count()
   else:
      print("Invalid input")