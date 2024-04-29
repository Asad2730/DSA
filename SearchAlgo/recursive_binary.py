
def recursive_binary(list,target):
      if len(list) == 0:
            return False
      else:
            mid = (len(list)) // 2
            if list[mid] == target:
                  return True 
            else:
                  if list[mid] < target:
                        return recursive_binary(list[mid+1:],target)
                  else:
                        return recursive_binary(list[:mid],target)