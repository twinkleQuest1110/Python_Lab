
import string

text = input("Enter a sentence: ")

# 1. Count words
words = text.split()
word_count = len(words)

# 2. Count vowels and digits
vowels = 0
digits = 0
special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isalnum() and not ch.isspace():
        special += 1

# 3. Find longest word
longest_word = max(words, key=len) if words else ""

# 4. Find repeated words (case-insensitive)
word_frequency = {}

for word in words:
    clean_word = word.lower().strip(string.punctuation)
    if clean_word:
        word_frequency[clean_word] = word_frequency.get(clean_word, 0) + 1

repeated_words = [
    word for word, count in word_frequency.items() if count > 1
]

# 5. Reverse each word
reversed_sentence = " ".join(word[::-1] for word in words)

# 6. Check palindrome after normalization
normalized = "".join(
    ch.lower() for ch in text if ch.isalnum()
)

is_palindrome = normalized == normalized[::-1]

# 7. Display report
print("\n===== TEXT ANALYSIS REPORT =====")
print("Total Words:", word_count)
print("Total Vowels:", vowels)
print("Total Digits:", digits)
print("Special Characters:", special)
print("Longest Word:", longest_word)
print("Repeated Words:", repeated_words)
print("Reversed Words:", reversed_sentence)
print("Palindrome:", "Yes" if is_palindrome else "No")
