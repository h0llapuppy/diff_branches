#!/usr/bin/env python3
import requests
import json
import sys

url='https://rdb.altlinux.org/api/export/branch_binary_packages/'
branch_list = ['sisyphus', 'p10', 'p9']
branches_archs = {'sisyphus': ['ppc64le', 'i586', 'x86_64', 'noarch', 'aarch64', 'armh'], 
            'p10': ['i586', 'x86_64', 'ppc64le', 'armh', 'noarch'],
            'p9':['aarch64', 'ppc64le', 'x86_64', 'armh', 'noarch', 'i586']}


def request():
    if len(sys.argv) < 5:
        print('Not enough arguments')
    elif len(sys.argv) > 5:
        print('Too many arguments')
    else:
        b1 = sys.argv[1]
        a1 = sys.argv[2]
        b2 = sys.argv[3]
        a2 = sys.argv[4]
        if ((b1 and b2) not in branch_list) and ((a1 not in branches_archs[b1]) and (a2 not in branches_archs[b2])):
            print('Bad branch or arch for branch')
        else: 

            request_b1 = requests.get(url + b1 + '?arch='+ a1)
            request_b2 = requests.get(url + b2 + '?arch='+ a2)
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

                full_list_2 = []
                for package in (result_list_packages_2_wihout_1):
                    full_list_2.append({'name': package})

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
                path_to_frite = input("Select path to write result files: ")
                with open(path_to_frite+'b1-b2.txt', 'w') as file1:
                    file1.write(str(dict(request_args=dict(arch=a1),length=len(result_list_packages_1_wihout_2),packages=full_list_1)))

                with open(path_to_frite+'b2-b1.txt', 'w') as file2:
                    file2.write(str(dict(request_args=dict(arch=a2),length=len(result_list_packages_2_wihout_1),packages=full_list_2)))

                with open(path_to_frite+'same_pack_v1_more_v2.txt', 'w') as file3:
                    file3.write(str(dict(request_args=dict(arch=a1),length=len(answer),packages=answer)))


                    

