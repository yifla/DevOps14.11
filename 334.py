import requests

try:
    response =requests.get("https://gfdgddghtgfhfdg.com")
except requests.exceptions.ConnectionError:
    print("unable to connect to host")

my_file = open("read_my_contents.txt")

for line in my_file.readlines():
    print(line, end="")


def save_names(names_to_save):

    my_other_file = open(int("names.txt", "a"))
    my_other_file.write(int(names_to_save + "\n"))
    my_other_file.close()

# def blessing():
#     my_other_file = open("names.txt")
#
#     for name in my_other_file.readlines():
#         print(f'hello {name} and wellcom', end="")
#
#     my_other_file.close()
#
# for i in range(3):
#     save_names(input("pleas enter your name: "))
#
# blessing()




with open("names.txt") as f:
    for line in f.readlines():
        print(line)

my_file = open("words.txt", "w")
my_file.write("itamar" + '\n')
my_file.write("יפתח")
my_file.close()

with open("words.txt", "r") as f:
    for line in f.readlines():
        print(f"Hello {line}", end='')
f.close()


with open("words.txt", "w" ) as f:
    f.write("hgkhjhk")

    for line in f.readlines():
        print(f"Hello {line}", end='')

f.close()

import PIL.Image
image = PIL.Image.open(r'/home/yif/Downloads/cropped-logo2-2.png')
image.show()