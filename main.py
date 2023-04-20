with open('1.txt', encoding='utf-8') as file_1:
    result_1 = file_1.readlines()
    text_1 = ''.join(result_1)
    count_1 = 0
    for i in result_1:
        count_1 += 1
    file_1_list = [file_1.name, str(count_1), text_1]

with open('2.txt', encoding='utf-8') as file_2:
    result_2 = file_2.readlines()
    text_2 = ''.join(result_2)
    count_2 = 0
    for n in result_2:
        count_2 += 1
    file_2_list = [file_2.name, str(count_2), text_2]

with open('3.txt', encoding='utf-8') as file_3:
    result_3 = file_3.readlines()
    text_3 = ''.join(result_3)
    count_3 = 0
    for _ in result_3:
        count_3 += 1
    file_3_list = [file_3.name, str(count_3), text_3]

with open('result.txt', 'w', encoding='utf-8') as file_res:
    all_file_list = [file_1_list, file_2_list, file_3_list]
    all_file_list = sorted(all_file_list, key=lambda x: x[1])
    all_files = []
    for m in all_file_list:
        all_files += m
    file_res.writelines('\n'.join(all_files))
