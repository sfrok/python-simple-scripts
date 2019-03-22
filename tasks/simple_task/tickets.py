# this code need refactoring, cuz removing from list is not best practices :)
def tickets(people):
    balance = []
    for customer in people:
        if customer == 25:
            balance.append(customer)
            continue
        elif customer == 50:
            change_25 = balance.count(25)
            if change_25 >= 1:
                balance.append(50)
                balance.remove(25)
                continue
            else:
                return "NO"
        elif customer == 100:
            count_25 = balance.count(25)
            count_50 = balance.count(50)
            if count_50 >= 1 and count_25 >= 1:
                balance.append(100)
                balance.remove(50)
                balance.remove(25)
                continue
            elif count_25 >= 3:
                balance.append(100)
                balance.remove(25)
                balance.remove(25)
                balance.remove(25)
                continue

            else:
                return "NO"
    return 'YES'


print(tickets([25, 100, 25, 25, 50, 50]))

