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

            short_package_list_b1 = list(map(lambda row: row['name'],package_list_b1))
            short_package_list_b2 = list(map(lambda row: row['name'],package_list_b2))
            result_list_packages_1_wihout_2=list(set(short_package_list_b1) - set(short_package_list_b2))
            result_list_packages_2_wihout_1=list(set(short_package_list_b2) - set(short_package_list_b1))
            result_list_of_same_packages=list(set(short_package_list_b1) & set(short_package_list_b2))

            full_list_1 = []
            for package in (result_list_packages_1_wihout_2):
                full_list_1.append({'name': package})
            with open('./work_files/b1.txt', 'w') as file1:
                file1.write(str(dict(count=len(result_list_packages_1_wihout_2),packages=full_list_1)))

            full_list_2 = []
            for package in (result_list_packages_2_wihout_1):
                full_list_2.append({'name': package})
            with open('./work_files/b2.txt', 'w') as file2:
                file2.write(str(dict(count=len(result_list_packages_2_wihout_1),packages=full_list_2)))
            dict1={}
            for package in package_list_b1:
                dict1[package['name']] = package['version']

            dict2={}
            for package in package_list_b2:
                dict2[package['name']] = package['version']

            answer = []
            for moduleName in result_list_of_same_packages:
                if dict1[moduleName] > dict2[moduleName]:
                    answer.append({'name':moduleName, 'version_b1':dict1[moduleName], 'version_b2':dict2[moduleName]})

            with open('./work_files/result.txt', 'w') as file3:
                file3.write(str(dict(count=len(answer),packages=answer)))

request('p10', 'x86_64', 'p9', 'x86_64') 


                    

