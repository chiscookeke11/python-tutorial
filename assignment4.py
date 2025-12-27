


with open("output.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)

try:
    with open("modified.txt", "w", encoding="utf-8") as file:
     file.write("Modified text:")
     file.write(data.lower())

except FileNotFoundError:
    print("File not found!")

finally:
    file.close()
