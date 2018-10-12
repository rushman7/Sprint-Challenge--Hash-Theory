def get_indices_of_item_weights(weights, limit):
  ht = {} # hash table

  if len(weights) == 1: # if only one returns empty
    return ()

  if len(weights) == 2: # if 2 compares
    if (weights[0] + weights[1] == limit): # returns if values equal
      return (1, 0)
    else:
      return ()  # if values dont match return empty

  for i, weights in enumerate(weights): 
    ht[weights] = i

  for key in ht:  # iterate through hash table and check for weights that meet the limit
    try:
      keyTest = ht[limit-key]
      if (keyTest):
        return (ht[limit-key], ht[key])
    except KeyError:
      print('Error!')

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 