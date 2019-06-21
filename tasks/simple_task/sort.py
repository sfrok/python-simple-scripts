def unusual_sort(array):
    array1 = [] + array
    lc_list = []
    uc_list = []
    all_smb = {}
    for i in array:
        if ord(str(i)) > 96:
            lc_list.append(array1.pop(array1.index(i)))
        elif ord(str(i)) > 64:
            uc_list.append(array1.pop(array1.index(i)))
    for i in array1:
        all_smb.update({str(i): 0})
    for i in array1:
        if isinstance(i, int):
            all_smb.update({str(i): array1.count(i)})
    for i in range(0, len(array1)):
        array1[i] = str(array1[i])
    array1 = sorted(array1)
    for i in range(0, len(array1)):
        if all_smb[array1[i]] > 0:
            all_smb[array1[i]] -= 1
            array1[i] = int(array1[i])
    array = sorted(uc_list) + sorted(lc_list) + array1
    return array
