import re


def request(b1: str, a1:str, b2: str, a2: str):
    result_list = [{'name': '0ab', 'version': '0.0.23b'}, {'name': '0ad', 'version': '0.0.25b'}, {'name': '0ad-debuginfo', 'version': '0.0.21b'}, {'name': '389-ds-base', 'version': '1.4.1.19'}]
    result_list2 = [{'name': '0ad', 'version': '0.0.23b'}, {'name': '0ad-debuginfo', 'version': '0.0.21b'}, {'name': '389-ds-base', 'version': '1.4.1.18'}]
    for i in result_list:
        for j in result_list2:
            if i['name'] == j['name'] and i['version'] > j['version']:
                print(i)



request('p10', 'x86_64', 'p9', 'x86_64') 