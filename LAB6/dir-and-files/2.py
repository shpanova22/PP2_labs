import os

name = r'C:\Users\Lenovo\OneDrive\Documents\PP2_labs\LAB6\dir-and-files'

print(os.access(name, os.F_OK)) # Existence
print(os.access(name, os.R_OK)) # Readability
print(os.access(name, os.W_OK)) # Writeability
print(os.access(name, os.X_OK)) # Executeability