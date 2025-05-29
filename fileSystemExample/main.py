# file = open("fileSystemExample/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("fileSystemExample/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# modes r(read),w(write),a(append)

# with open("fileSystemExample/new_file.py",mode="a") as file:
#     file.write("print('hello python')")

with open("fileSystemExample/new_file.txt",mode="a") as file:
    file.write("\n New text.")
    