def checking_data(books, categories):
    if len(books) == 0: return ''
    elif len(categories) == 0: return ''
    else: return 'valid data'


def counting_data(books):
    data = {}
    for book in books:
        book_count = int(book.rsplit(' ', 1)[1])
        if book[0] not in data:
            data[book[0]] = book_count
        else:
            book_count += data[book[0]]
            data.update({book[0]: book_count})
    return data


def stock_list(books, categories):
    if checking_data(books, categories) == 'valid data':
        books_stock = counting_data(books)
        result = ''
        for category in categories:
            if len(result) != 0:
                result += ' - '
            if category in books_stock:
                result += f'({category} : {books_stock[category]})'
            else:
                result += f'({category} : {0})'
        return result
    else:
        return ''


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", 'W']
print(stock_list(b, c))
