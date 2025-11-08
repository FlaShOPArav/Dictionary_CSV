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
        with open(FILENAME, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["word", "meaning"])
    return dictionary

def search_word(dictionary):
    word = input("Enter a word to search: ").strip().lower()
    if word in dictionary:
        print(f"\n{word.capitalize()}: {dictionary[word]}")
    else:
        print("Word not found in dictionary.")

def main():
    dictionary = load_dictionary()
    while True:
        print("\n==== DICTIONARY ====")
        print("1. Search for a word")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ").strip()
        if choice == '1':
            search_word(dictionary)
        elif choice == '2':
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
