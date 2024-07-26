import random

main_string = "しかのこのこのここしたんたん＊"
letter_set = set(main_string)
letter_list = list(main_string)

main_dict = {}

for letter in letter_set:
    main_dict[letter] = []

for i in range(len(letter_list)-1):
    temp = main_dict[letter_list[i]]
    temp.append(letter_list[i+1])

temp = main_dict["＊"]
temp.append("し")

start_key = "し"
count = 0
MAX_COUNT = 0  #1以上にしたら、その数までいったら強制終了
while True:
    count += 1
    temp_str = "し"
    for i in range(len(main_string)-1):
        temp_list = main_dict[start_key]
        rnd_val = random.randrange(0,len(temp_list))
        next_key = temp_list[rnd_val]
        temp_str += next_key
        start_key = next_key
    print(temp_str)
    if temp_str == main_string:
        print(f"{count}回目ででた")
        break
    elif count>=MAX_COUNT and MAX_COUNT > 0:
        print(f"{count}回やったけど出んかった")
        break
