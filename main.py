print("\nWelcome!!")
print("Here are the available file operations services")
print("1. Counting of words in a file")
print("\nKindly attach the file to use to this folder or you can make sure of the 'text.txt' file available")

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
