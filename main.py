print("\nWelcome!!")
print("Here are the available file operations services")
print("1. Counting of words in a file")
print("2. Searching through a file")
print("\nKindly attach the file to use to this folder or you can make sure of the 'text.txt' file available")

user_response = int(input("Enter response Here:"))
if user_response == 1:
    file_name = input("\nEnter the file name:")

    try:
        fhand = open(file_name)
    except:
        print("File cannot be opened.Please check the file")
        exit()

    word_count = 0
    for line in fhand:
        words = line.split()
        for word in words:
            word_count = word_count + 1
    print("\nNO OF WORDS IN FILE:", word_count)

elif user_response == 2:
    file_name2 = input("\nEnter the file name:")
    inputted_word = input("Enter word to look for:")

    try:
        fhand2 = open(file_name2)
    except:
        print("File cannot be opened.Please check the file")
        exit()

    word_index = 0
    line_index = 0
    for line in fhand2:
        line = line.rstrip()
        line_index += 1
        words = line.split()
        for word in words:
            if word == inputted_word:

                print("Word is found in line ", line_index, " at position ....")

            else:
                continue
            # print("Word not found!!!")
