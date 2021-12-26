what_to_print = "hello world!"
list_of_names = ["hen", "michael", "noam", "lior", "amichai"]
amount_of_print = 4

print(list(range(9, 2, -1)))

for i in range(1, amount_of_print):
    print(str(1) + ")" + what_to_print)

for i in range(len(list_of_names)):
    print(list_of_names[1])

for name in list_of_names:
    if name == "hen":
        # break
        continue
    print(name)
a = 0
while a < 10:
    print(a)
    a = a + 1

for num in range(0, 101):
    # if num % 7 == 0 or "7" in str(num):
    #     continue
    if num % 7 != 0 and "7" not in str(num):
        print(num)

# a = 0
# while a < 10:
#     print(a)
#     a = a + 1
a = "a"
while a != "q":
    a = input("enter q or not:")


else:
    print("finished successfully")
