file_path = 'alice.txt'

try:
    with open(file_path, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist.")
else:
    # 计算该文件大致包含多少单词。
    words = contents.split()
    num_words = len(words)
    print(f"the file {file_path} has about {num_words} words.")