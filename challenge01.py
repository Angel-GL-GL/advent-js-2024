def prepare_gifts(gifts):
  if not gifts:
    return []

  result = sorted(dict.fromkeys(gifts));

  return result
