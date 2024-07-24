from random import randint
strings = "しかのこのこのここしたんたん＊"
str_list = []
str_list.extend(strings)

#最悪この回数見つからなかったらループ終了↓
#負の値にしたら無限に見つけるまでやる
MAX_COUNT = -1

main_dict = {}

for single_str in str_list:
    if not single_str in main_dict.keys():
        temp_list = []
        for next_str_ind in range(len(str_list)):
            next_str = str_list[next_str_ind]
            if next_str == single_str:
                append_ind = next_str_ind + 1
                if append_ind < len(str_list):
                    temp_list.append(str_list[append_ind])
                else:
                    temp_list.append(str_list[0])
        main_dict[single_str] = temp_list

count = 0
while True:
    output_list = ["し"]
    for loops in range(len(strings)-1):
        keys = output_list[-1]
        nexts = main_dict[keys]
        rnd = randint(0, len(nexts)-1)
        output_list.append(nexts[rnd])

    else:
        output_str = ""
        for i in output_list:
            output_str += i

        print(output_str)
        if output_str == strings:
            print(count, "回目の挑戦でしかのこ出た。")
            break
        else:
            count += 1
        
        if MAX_COUNT>0 and count>=MAX_COUNT:
            print(count, "回挑戦しましたがダメでした。")
            break
