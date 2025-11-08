# Dictionary App CSV

## Overview

This is a simple Python-based Dictionary Application that allows users to **search**, **add**, and **remove** words along with their meanings.
All data is stored in a **CSV file** (`dictionary.csv`) for easy access and modification.

## Features

* Search for a word and view its meaning
* Add new words with meanings
* Remove existing words
* Automatically creates a CSV file if it doesn’t exist

## Requirements

* Python 3.x
* No external libraries (only uses the built-in `csv` module)

## How to Run

1. Make sure you have Python installed on your system.
2. Place the `dictionary.py` file and `dictionary.csv` (if available) in the same folder.
3. Open a terminal or command prompt in that folder.
4. Run the script:

   ```
   python dictionary.py
   ```

## CSV File Format

The program uses a CSV file named `dictionary.csv` with the following structure:

```
word,meaning
python,a high-level programming language
humble,not proud or arrogant; modest
galaxy,a system of millions or billions of stars
```

If the file does not exist, it will be created automatically.

## Menu Options

When you run the program, you’ll see the following menu:

```
==== DICTIONARY MENU ====
1. Search for a word
2. Add a new word
3. Remove a word
4. Exit
```

Choose an option by entering the corresponding number.

## Example

```
Enter your choice (1-4): 1
Enter a word to search: python

Python: a high-level programming language
```

## Author

Created by Arav Upadhyay
