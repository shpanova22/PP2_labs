import re

text = "WeLoveKazakhstan"

# Add a space before each uppercase letter (except the first one)
result = re.sub(r"(?<!^)(?=[A-Z])", " ", text)

print(result)
