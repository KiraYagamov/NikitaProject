russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
chars = {}
file = open("Text.txt", "r", encoding="utf-8")
all_count = 0

line = file.read()

for i in line:
    i = i.lower()
    if i not in russian:
        continue
    if i in chars.keys():
        chars[i] += 1
    else:
        chars[i] = 1
    all_count += 1

file.close()

for key in sorted(chars.keys()):
    print(f"{key}: {chars[key] / all_count}")
