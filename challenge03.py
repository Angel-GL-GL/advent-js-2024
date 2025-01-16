def organizeInventory(inventory):
  categories = {}

  for obj in inventory:
    if obj.category not in categories:
      temp = {}
      temp[obj.name] = obj.quantity
      categories[obj.category] = temp
    else:
      temp = categories.get(obj.category)
      temp[obj.name] = obj.quantity + temp.get(obj.name)
      categories[obj.category] = temp

  return categories
