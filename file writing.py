txt_data = "I am Yeamin and I like pizza."
file_path = "Output.txt"

with open("file_path", "w") as file:
    file.write(txt_data)
    print(txt_data)