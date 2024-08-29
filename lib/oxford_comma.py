def oxford_comma(items):
    items.insert(-1, 'and')
    new_items= ', '.join(items[:-1])
    
    return new_items
print(oxford_comma(['tree', 'bush', 'house']))