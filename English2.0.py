import os # import the os module to access functionality of the underlying operating system
import sys # import the sys module to have access to some system-specific variables and functions
import webbrowser # import the webbrowser module to open the browser

# function to clear the terminal
def clear():
    os.system('cls' if os.name == "nt" else "clear") # clear the terminal window
clear()
# ask for the password
password = input('Enter the password: ')

if password == "aassddff": # check if the password entered by the user is correct
    clear()

    # ask the user for the word or statement to look up
    key_word = input("Enter the word or statement: ")
    words = key_word.split() # split the input into individual words
    if not 0 < len(words) <= 4:
        print("The maximum number of words is 4.")
        sys.exit("bye")

    # checking the length and making the link
    dictionary_url = f"https://dictionary.cambridge.org/dictionary/english-arabic/{'-'.join(words)}"
    youglish_url = f"https://youglish.com/pronounce/{'%20'.join(words)}/english?"

    # print the links to the user
    print("Here are the links: ")
    print(dictionary_url)
    print(youglish_url)

    # ask if the user wants to open the links in the browser
    is_redirected = input("Do you want me to redirect you to the website? Enter Y/N: ")
    max_count = 5
    for count in range(1, max_count+1):
        if is_redirected.lower().startswith("y"):
             webbrowser.open(dictionary_url)
             webbrowser.open(youglish_url) 
             break
        elif is_redirected.lower().startswith("n"):
             sys.exit("Goodbye!") 
        else:
            is_redirected = input("Do you want me to redirect you to the website? Enter Y/N: ")
            
    else:
        sys.exit("Maximum number of attempts exceeded. Exiting program.")
             
else:
    print("Wrong password.")