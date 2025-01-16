def organizeShoes(shoes):
  result = []
  helper = {"I":[], "R":[]}

  for shoe in shoes:
    temp = helper.get(shoe.type)
    temp.append(shoe.size)
    helper[shoe.type] = temp

  list1 = sorted(helper.get("I"))
  list2 = sorted(helper.get("R"))

  for shoe in list1:
    if shoe in list2:
      index = list2.index(shoe)
      list2.pop(index)
      result.append(shoe)

  return result
