import requests
import json

def request(b1: str, a1:str, b2: str, a2: str):
    url='https://rdb.altlinux.org/api/export/branch_binary_packages/'
    branch_list = ['sisyphus', 'sisyphus_e2k', 'sisyphus_mipsel', 'sisyphus_riscv64', 'p10', 'p10_e2k', 'p9', 'p9_e2k', 'p9_mipsel', 'p8', 'c9f2', 'c7']

    if (b1 and b2) not in branch_list:
        print('Bad branch')
    else: 
        request_b1 = requests.get(url + b1 + '?arch='+ a1)
        request_b2 = requests.get(url + b2 + '?arch='+ a1)

        if (request_b1.status_code and request_b2.status_code) != 200:
            print('Bad request')
        else:
            package_list_b1 = (json.loads(request_b1.text))["packages"]
            package_list_b2 = (json.loads(request_b2.text))["packages"]
            
            short_package_list_1 = list(map(lambda row: row['name'],package_list_b1))
            short_package_list_2 = list(map(lambda row: row['name'],package_list_b2))

            package_list_diff_b1 = [x for x in short_package_list_1 if x not in short_package_list_2]
            # with open('./work_files/b1.txt', 'w') as file1:
            #      file1.write(str(dict(qount=len(package_list_diff_b1),packages=package_list_diff_b1)))
            
            package_list_diff_b2 = [x for x in short_package_list_2 if x not in short_package_list_1]
            # with open('./work_files/b2.txt', 'w') as file2:
            #      file2.write(str(dict(qount=len(package_list_diff_b2),packages=package_list_diff_b2)))

            short_package_list_1_v = list(map(lambda row: dict(name=row['name'], version=row['version']),package_list_b1))
            short_package_list_2_v = list(map(lambda row: dict(name=row['name'], version=row['version']),package_list_b2))

            # package_list_same_b1 = [x for x in short_package_list_1_v['name'] if x in short_package_list_2_v['name']]
            # with open('./work_files/result.txt', 'w') as file2:
            #     file2.write(str(package_list_same_b1))

request('p10', 'x86_64', 'p9', 'x86_64') 


                    

