with open (r'C:\Users\Lenovo\OneDrive\Documents\PP2_labs\LAB6\dir-and-files\text.txt', 'r') as file:
        x = len(file.readlines())
        print("Number of lines:", x)