def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        words = file_contents.split()
        wordcount = len(words)

        lowered_words = file_contents.lower()
        char_count = {}  
        for letter in lowered_words:
            if letter.isalpha():
                if letter not in char_count:
                    char_count[letter] = 1
                else:
                    char_count[letter] += 1

        char_count_list = [{"char": key, "num": value} for key, value in char_count.items()]
        
        def sort_on(d):
            return d["num"]
        char_count_list.sort(reverse=True, key=sort_on)
        
        print(f"""--- Begin report of books/frankenstein.txt ---\n{wordcount} words found in the document""")
        for item in char_count_list:
            char = item['char']
            num = item['num']
            print(f"The '{char}' character was found {num} times")
        
        print("--- End report ---")


if __name__ == "__main__":
    main()