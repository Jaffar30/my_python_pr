file = open("email_Sender/input/Names/invited_names.txt")

# names2 = file.readlines()
# print(names2)
content = file.read()
file.close()
names = []
name = ""



# ====== get names ===========
lines = content.splitlines()  # This gives us a list of lines from the file
# Loop through each line
for line in lines:
    # Remove spaces from the beginning and end of the line
    clean_name = line.strip()
    # If the cleaned name is not empty, add it to the names list
    if clean_name:
        names.append(clean_name)
# =======================

file = open("email_Sender/input/Letters/starting_letter.txt")
mail_template = file.read()
file.close()

for name in names:
    result = mail_template.replace("[name]",name)
    with open(f"email_Sender/output/ReadyToSend/letter_for_{name}.txt",mode="w") as file:
        file.write(result)


