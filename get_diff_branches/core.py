#!/usr/bin/env python3
import requests
import json
import sys

url='https://rdb.altlinux.org/api/export/branch_binary_packages/'
branch_list = ['sisyphus', 'p10', 'p9']
branches_archs = {'sisyphus': ['ppc64le', 'i586', 'x86_64', 'noarch', 'aarch64', 'armh'], 
            'p10': ['i586', 'x86_64', 'ppc64le', 'armh', 'noarch'],
            'p9':['aarch64', 'ppc64le', 'x86_64', 'armh', 'noarch', 'i586']}
calc_methods = ['b1-b2','b2-b1','b2andb1']

def request():
    if len(sys.argv) < 4:
        print('Not enough arguments')

    elif len(sys.argv) > 5:
        print('Too many arguments')

    else:
        branch_1 = sys.argv[1]
        branch_2 = sys.argv[2]
        arch = sys.argv[3]
        method = ''
        if ((branch_1 and branch_2) not in branch_list):
            print('Bad branch')
            
        elif (arch not in (branches_archs[branch_1] and branches_archs[branch_2])):
            print('Bad arch for branches')

        else: 

            request_b1 = requests.get(url + branch_1 + '?arch='+ arch)
            request_b2 = requests.get(url + branch_2 + '?arch='+ arch)
            if (request_b1.status_code and request_b2.status_code) != 200:
                print('Bad request')
                
            else:
                if len(sys.argv) == 5:
                    method = sys.argv[4]
                package_list_b1 = (json.loads(request_b1.text))["packages"]
                package_list_b2 = (json.loads(request_b2.text))["packages"]

                short_package_list_b1 = list(map(lambda row: row['name'],package_list_b1))
                short_package_list_b2 = list(map(lambda row: row['name'],package_list_b2))

                result_list = []
                if method:
                    if method not in calc_methods:
                        print('Bad calc method')
                    if method == calc_methods[0]:
                        result_list = calc_diff_between_branches(short_package_list_b1, short_package_list_b2)

                    elif method == calc_methods[1]:
                        result_list = calc_diff_between_branches(short_package_list_b2, short_package_list_b1)

                    elif method == calc_methods[2]:
                        list_same_packs= calc_same_packages_between_branches(short_package_list_b1, short_package_list_b2)
                        package_dict_b1 = packing_list_of_dict_into_dict(package_list_b1)
                        package_dict_b2 = packing_list_of_dict_into_dict(package_list_b2)

                        for moduleName in list_same_packs:
                            if package_dict_b1[moduleName] > package_dict_b2[moduleName]:
                                result_list.append({'name':moduleName, 'version_b1':package_dict_b1[moduleName], 'version_b2':package_dict_b2[moduleName]})

                    print(str(dict(request_args=dict(arch=arch),length=len(result_list),packages=result_list)))
                else:

                    result_b1_b2 = calc_diff_between_branches(short_package_list_b1, short_package_list_b2)
                    result_b2_b1 = calc_diff_between_branches(short_package_list_b2, short_package_list_b1)

                    result_b1_and_b2 = []
                    list_same_packs= calc_same_packages_between_branches(short_package_list_b1, short_package_list_b2)
                    package_dict_b1 = packing_list_of_dict_into_dict(package_list_b1)
                    package_dict_b2 = packing_list_of_dict_into_dict(package_list_b2)

                    for moduleName in list_same_packs:
                        if package_dict_b1[moduleName] > package_dict_b2[moduleName]:
                            result_b1_and_b2.append({'name':moduleName, 'version_b1':package_dict_b1[moduleName], 'version_b2':package_dict_b2[moduleName]})

                    path_to_write = input("Select path to write result files: ")

                    if write_into_txt_file(path_to_write, calc_methods[0], dict(request_args=dict(arch=arch),length=len(result_b1_b2),packages=result_b1_b2)) is None:
                        if write_into_txt_file(path_to_write, calc_methods[1], dict(request_args=dict(arch=arch),length=len(result_b2_b1),packages=result_b2_b1)) is None:
                            write_into_txt_file(path_to_write, calc_methods[2], dict(request_args=dict(arch=arch),length=len(result_b1_and_b2),packages=result_b1_and_b2))

                
def calc_diff_between_branches(base_branch_list: list, subtract_branch_list: list):
    
    branch_difference=list(set(base_branch_list) - set(subtract_branch_list))

    received_package_list = []
    for package in (branch_difference):
        received_package_list.append({'name': package})
    return received_package_list


def calc_same_packages_between_branches(base_branch_list: list, subtract_branch_list: list):

    result_list_of_same_packages=list(set(base_branch_list) & set(subtract_branch_list))

    return result_list_of_same_packages


def packing_list_of_dict_into_dict(list_of_dicts: list):

    cur_dict={}

    for package in list_of_dicts:
        cur_dict[package['name']] = package['version']
    return(cur_dict)

def write_into_txt_file(path_to_write: str, method_calc: str, result_list: dict):

    with open(path_to_write+method_calc+'.txt', 'w') as file_n:
        file_n.write(str(result_list))
