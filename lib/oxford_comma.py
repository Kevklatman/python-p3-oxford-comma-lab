def oxford_comma(items):
    last_item = items[-1]
    items.insert(-1, 'and')
    new_items = [', '.join(items[:-1])]
    string = ''.join(new_items) + ' ' + last_item
    return string

print(oxford_comma(['tree', 'bush', 'house']))