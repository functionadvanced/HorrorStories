import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
a = open(os.path.join(dir_path,"horror_stories.txt"), 'r', encoding="utf-8")
lines = a.readlines()
curr = 1
poss = [". ", "、 ", "、", ".", "。"]
title_no_meaning = ["\n", " ", "《", "》", "\"", "「", "」"]
temp = []
title = []
content = ""
answer_flag = False
for i in range(len(lines)):
    if str(curr) in lines[i][:2]:
        for k in poss:
            if k in lines[i][:4]:
                # print(lines[i][:-1])
                # print(lines[i][:4].index(k))
                temp.append(content)
                si = lines[i][:4].index(k)
                content = lines[i][si+len(k):]
                if content[0] == ' ':
                    print(lines[i])
                if not answer_flag:
                    for kk in title_no_meaning:
                        content = content.replace(kk, '')
                    title.append(content)
                    content = ""
                curr += 1
                if curr == 82:
                    answer_flag = True
                    curr = 1
                break
    else:
        content += lines[i]
temp.append(content)
temp.pop(0)
# print(len(temp))
# print(temp[0])
# print(temp[81])
# for i in range(len(title)):
#     print(str(i) + ". "+title[i])
# print(title)

all_data = []
for i in range(81):
    o = {'title': title[i], 'content': temp[i].replace("这些惊悚推理故事出自“意味がわかると怖い话”，答案都为网络上无数网友共同推导得出 所以没有绝对的答案\n下面给出答案\n", ''), 'answer': temp[i+81]}
    all_data.append(o)

# print(all_data[0])
# print(all_data[1])

import json
with open(os.path.join(dir_path,"horror_stories.json"), 'w') as output_file:
    json.dump(all_data, output_file)