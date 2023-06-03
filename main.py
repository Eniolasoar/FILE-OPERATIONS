import string

print("\nWelcome!!")
print("Here are the available file operations services")
print("1. Total word count")
print("2. Word search")
# edit file like grammarly
# ask for "are you searching for aline"
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
    print("What would you like to do:")
    print("1. Look for a word")
    print("2. Run a full word count analysis of the file")
    user_response2=input("Enter Response Here:")

    if user_response2==1:
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

                    print("\nWord is found in line ", line_index, " at position ....")

                else:
                    continue
                # print("Word not found!!!")

    else:


        file = input("Enter File name:")
        try:
            file_handle = open(file)
        except:
            print("File can't be opened")

        word_dict = dict()
        for line in file_handle:
            # removing all punctuation to prevent comparison error
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.lower()
            word_split = line.split()
            for word in word_split:
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1

        print("A FULL ANALYSIS OF THE WORDS AND THEIR NO OF COUNT:\n")
        for word_list in word_dict:
            print(word_list + ":", word_dict[word_list])
