def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ('alice.txt', 'siddhartha0.txt', 'moby_dick.txt', 'little_women.txt')
for filename in filenames:
    count_words(filename)
