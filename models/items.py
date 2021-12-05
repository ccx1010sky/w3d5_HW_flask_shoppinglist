from models.item import Item

item1 = Item("watermelon","2.00",1,True)
item2 = Item("sandwich","3.00",2,True)
item3 = Item("coke","1.00",6,False)

items = [item1,item2,item3]


def add_new_item(item):
    items.append(item)
    
def delete_item(name_of_item):
    item_delete = None
    for item in items:
        if item.name_of_item == name_of_item:
            item_delete= item
            break

    items.remove(item_delete)
