
# task 1
with open("input.txt", "w", encoding="utf-8") as file:
    file.write("""
               LIne 1
               line 2
               line 3
               line 4
               line 5
               """)


# task 2
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read()

    print(data)

    word_count = len(data.split())
    print(word_count)


uppercase_text = data.upper()
print(uppercase_text)



# Step 5: Write processed text and word count to output.txt
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(uppercase_text)
    file.write("\n\n")
    file.write(f"WORD COUNT: {word_count}")

# Step 6: Print success message
print("✅ Success! output.txt has been created and updated.")