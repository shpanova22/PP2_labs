with open(r'C:\Users\Lenovo\OneDrive\Documents\PP2_labs\LAB6\dir-and-files\text.txt',"r") as file1:
    with open("text_copy.txt","w") as file2:
        for line in file1:
            file2.write(line)