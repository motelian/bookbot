def get_book_text(path):
    with open(file=path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if c.lower() in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def generate_report(path):
    text = get_book_text(path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    report = f"--- Begin report of {path} ---\n"
    report += f"{num_words} words found in the document\n\n"
    sorted_chars_dict = dict(sorted(chars_dict.items(), key=lambda x: x[1], reverse=True))
    for k, v in sorted_chars_dict.items():
        if k.isalpha():
            report += f"The '{k}' character was found {v} times\n"
    report += "--- End report ---"
    return report

def main():
    book_path = "books/frankenstein.txt"
    report = generate_report(book_path)
    print(report)

if __name__ == "__main__":
    main()
