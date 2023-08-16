# with open('text_files/pi_digits.txt') as file_object:
#     # contents = file_object.read()
#     for line in file_object:
#         print(line.rstrip())

# print(contents)

file_path = "pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_str = ''
for line in lines:
    pi_str += line.strip()

# print(f"{pi_str[:500]}...")
# print(pi_str)
# print(len(pi_str))

birthday = input("Enter your birthday, in the from mmddyy: ")
if birthday in pi_str:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")