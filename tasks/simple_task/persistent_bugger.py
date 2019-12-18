def data_processing(number):  # O(n)
    return [int(i) for i in str(number)]


def persistence(number_set, counter=0):  # O(n)
    if len(str(number_set)) == 1:
        return counter
    else:
        counter += 1
        result = 1
        data_list = data_processing(number_set)
        for i in range(len(data_list)):
            result = result * data_list[i]
        return persistence(result, counter)


print(persistence(39))