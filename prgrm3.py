def count_words(text):
    words = text.split()
    return len(words)
user_input=input("Enter a sentence or paragragh")
total_words=count_words(user_input)
print(f"total words:{total_words}")