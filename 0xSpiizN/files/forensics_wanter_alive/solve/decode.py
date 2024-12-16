import urllib.parse

# Ouvrir le fichier
with open("../wanted.hta", mode="r") as f:
    encoded_string = f.read()

# Décoder les caractères %??
decoded_string = encoded_string
for i in range(10):
    decoded_string = urllib.parse.unquote(decoded_string)

print(decoded_string)