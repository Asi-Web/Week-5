## Asiwome Agbleze
## CMSC 111
## Spring 2026
## Week 6 Assignment

## This function counts how many times a substring appears in a string
def count_substring(text, sub):
    return text.count(sub)

## This function replaces one word or phrase with another
def replace_text(text, old, new):
    return text.replace(old, new)

## Try runs the program normally. Except catches errors if somehting goes wrong.
try:
    text1 = "This is a simple test"
    substring = "is"

## Check to make sure the string and substring are not empty
    if text == or substring == "":
        print("Error: text and substring cannot be empty.")
else:
    ## Call the function and store the result in count
    count = count_substring(text1, substring)
    ## Print the result in a clear sentence 
    print(f' The substring "{substring}" appears {count} times.')

## Word we want to replace and new word that will replace the old word
text2 = "This is an old example."
old_word = "old"
new_word = "new"

## Check to make sure none of the values are empty
if text2 == ""or old_word == "" or new_word == "":
    print("Error: text, old word, and new word, and new word cannot be empty.")
else:
    ## Call the replace function and save the new string
    updated_text = replace_text(text2, old_word, new_word)
    ## Print the updated string
    print(updated_text)

## If there is an error, this message will be shown
except Exception as e:
    print("An error occurred:", e)
    


