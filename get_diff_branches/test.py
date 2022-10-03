

def request(b1: str, a1:str, b2: str, a2: str):
    result_names = ['0ad', '0ad-debuginfo', '389-ds-base', '389-ds-base-debuginfo', '389-ds-base-devel', '389-ds-base-libs-debuginfo']
    result_list1 = [{'0ad': '0.0.26'}, {'0ad-debuginfo': '0.0.26'}, {'389-ds-base': '1.4.3.25'}, {'389-ds-base-debuginfo': '1.4.3.25'}, {'389-ds-base-devel': '1.4.3.25'}, {'389-ds-base-libs': '1.4.3.25'}, {'389-ds-base-libs-debuginfo': '1.4.3.25'}]
    result_list2 = [{'0ad': '0.0.25'}, {'0ad-debuginfo': '0.0.26'}, {'389-ds-base': '1.4.3.23'}, {'389-ds-base-debuginfo': '1.4.3.25'}, {'389-ds-base-devel': '1.4.3.28'}, {'389-ds-base-libs': '1.4.3.21'}, {'389-ds-base-libs-debuginfo': '1.4.3.16'}]
    answer = []

    for elem in result_names:
        VersionFrom_resultList1 = ""
        VersionFrom_resultList2 = ""

        for dict in result_list1:
            if elem in dict.keys():
                VersionFrom_resultList1 = dict[elem]
                break

        for dict in result_list2:
            if elem in dict.keys():
                VersionFrom_resultList2 = dict[elem]
                break

        if VersionFrom_resultList1 != "" and VersionFrom_resultList2 !="":
            if VersionFrom_resultList1 > VersionFrom_resultList2:
                answer.append({'name':elem, 'version_b1':VersionFrom_resultList1, 'version_b2':VersionFrom_resultList2})
    print(answer)
request('p10', 'x86_64', 'p9', 'x86_64') 