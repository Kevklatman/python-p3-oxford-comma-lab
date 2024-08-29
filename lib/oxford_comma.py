def oxford_comma(items):
    items.insert(-1, 'and')
    ', '.join(items)
    return items
print(oxford_comma(['tree', 'bush', 'house']))