import requests
import json
import re

cur_query = ''
api_key = ''
url = ''


headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

data = {
    "inputs": {},
    "query": f"{cur_query}",
    "response_mode": "streaming",
    "user": "abc-123",
    "files": []
}

response = requests.post(url, json=data, headers=headers)

# reader = response.content.read()
# data = b''
# while reader:
#     data += reader
#     reader = response.content.read()

# if response.status_code == 200:
#     # 打开文件并写入响应文本
#     with open('E:\\intern\\response.txt', 'w', encoding='utf-8') as f:
#         f.write(response.text)

# with open('E:\\intern\\response.txt', 'r', encoding='utf-8') as f:
#     file_content = f.readlines()
# ans = ''
# for line in file_content:
#     if line.strip() != '':
#         line = line.replace('data:', '')
#         try:
#             file_json = json.loads(line)
#             print(file_json)
#             if file_json['event'] == 'message_end':
#                 break
#             decoded_ans = file_json['answer']
#             ans += decoded_ans
#             print(decoded_ans)
#         except json.JSONDecodeError as e:
#             pass
# print(ans)

ans = ''
for line in response.iter_lines(delimiter=b"\n\n"):
    if line:
        print(line)
        line = re.sub(rb'^data:', b'', line)
        try:
            file_json = json.loads(line)
            print(file_json)
            if file_json['event'] == 'message_end':
                break
            decoded_ans = file_json['answer']
            ans += decoded_ans
            print(decoded_ans)
        except json.JSONDecodeError as e:
            print('json出错')

print(ans)
