def main():
# Open and read the file contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        # Count words
        words = file_contents.split()
        wordcount = len(words)

        # Count characters (case-insensitive)
        lowered_words = file_contents.lower()
        char_count = {}  # Initialize empty dictionary
        for letter in lowered_words:
            if letter.isalpha():
                if letter not in char_count:
                    char_count[letter] = 1
                else:
                    char_count[letter] += 1

        # Convert dictionary into a list of dictionaries
        char_count_list = [{"char": key, "num": value} for key, value in char_count.items()]
        
        # Sort list by "num" in descending order
        def sort_on(d):
            return d["num"]
        char_count_list.sort(reverse=True, key=sort_on)
        
        # Print report
        print(f"""--- Begin report of books/frankenstein.txt ---\n{wordcount} words found in the document""")
        for item in char_count_list:
            char = item['char']
            num = item['num']
            print(f"tThe '{char}' character was found {num} times")
        
        print("--- End report ---")


if __name__ == "__main__":
    main()