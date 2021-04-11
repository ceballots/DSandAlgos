class HashTableChaining(object):
    def __init__(self):
      self.MAX = 10
      self.arr = [[] for i in range(self.MAX)]

    def __get_hash(self, key):
      hash_value = 0
      for c in key:
        hash_value += ord(c)
      return hash_value % self.MAX

    def __getitem__(self, index):
      arr_index = self.__get_hash(index)
      for kv in self.arr[arr_index]:
        if kv[0] == index:
          return kv[1]

    def __setitem__(self, key, val):
      h = self.__get_hash(key)
      found = False
      for idx, element in enumerate(self.arr[h]):
        if len(element)==2 and element[0] == key:
            self.arr[h][idx] = (key,val)
            found = True
      if not found:
        self.arr[h].append((key,val))
