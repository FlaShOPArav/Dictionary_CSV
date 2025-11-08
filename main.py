import csv

FILENAME = "dictionary.csv"

def load_dictionary():
    dictionary = {}
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dictionary[row['word'].strip().lower()] = row['meaning'].strip()
    except FileNotFoundError:
        print("⚠️ CSV file not found. Creating a new one...")
        with open(FILENAME, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["word", "meaning"])
    return dictionary

def save_dictionary(dictionary):
    with open(FILENAME, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["word", "meaning"])
        for word, meaning in dictionary.items():
            writer.writerow([word, meaning])

def search_word(dictionary):
    word = input("Enter a word to search: ").strip().lower()
    if word in dictionary:
        print(f"\n📘 {word.capitalize()}: {dictionary[word]}")
    else:
        print("❌ Word not found in dictionary!")

def add_word(dictionary):
    word = input("Enter a new word: ").strip().lower()
    if word in dictionary:
        print("⚠️ Word already exists!")
    else:
        meaning = input("Enter its meaning: ").strip()
        dictionary[word] = meaning
        save_dictionary(dictionary)
        print("✅ Word added successfully!")

def remove_word(dictionary):
    word = input("Enter the word to remove: ").strip().lower()
    if word in dictionary:
        del dictionary[word]
        save_dictionary(dictionary)
        print("🗑️ Word removed successfully!")
    else:
        print("❌ Word not found!")

def main():
    dictionary = load_dictionary()
    while True:
        print("\n==== 📖 DICTIONARY MENU ====")
        print("1️⃣ Search for a word")
        print("2️⃣ Add a new word")
        print("3️⃣ Remove a word")
        print("4️⃣ Exit")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == '1':
            search_word(dictionary)
        elif choice == '2':
            add_word(dictionary)
        elif choice == '3':
            remove_word(dictionary)
        elif choice == '4':
            print("\nGoodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
