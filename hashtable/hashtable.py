class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.data = [None] * capacity
        self.count = 0


    def get_num_slots(self):
        # return number of slots
        return len(self.data)


    def get_load_factor(self):
        # get the load factor
        return self.count / self.capacity


    def fnv1(self, key):
        # fnv1
        fnv_prime = 1099511628211
        offset_basis =  14695981039346656037
        hash_value = offset_basis
        key_utf8 = key.encode()
        for byte in key_utf8:
            hash_value = hash_value ^ byte
            hash_value = hash_value * fnv_prime
        return hash_value


    # def djb2(self, key):
    #     # djb2
    #     hash_value = 5381
    #     for char in key:
    #         hash_value = (hash_value * 33) + ord(char)
    #     return hash_value


    def hash_index(self, key):
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

def put(self, key, value):
        index = self.hash_index(key)
        hst = HashTableEntry(key, value)
        node = self.data[index]
        if node is not None:
            self.data[index] = hst
            self.data[index].next = node
        else:
            self.data[index] = hst
            self.count += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        if key is key:
            self.put(key, None)
            self.count -= 1
        else:
            print("Key is not found.")


    def get(self, key):
        index = self.hash_index(key)
        node = self.data[index]
        if node is not None:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return node

    def resize(self, new_capacity):
        # make a new hashTable passing in the new capacity
        new_hashTable = HashTable(new_capacity)
        # for each entry in the data of the table
        for entry in self.data:
            # check if entry and if there is
            if entry:
                # we update the new hashTable using put, passing in the key/value
                new_hashTable.put(entry.key, entry.value)
                # check if there is a next entry
                if entry.next:
                    # if there is set the current var to be entry
                    current = entry
                    # while there is a next entry
                    while current.next:
                        # set current = current.next
                        current = current.next
                        # we use put to modify the new hashTable using key/value
                        new_hashTable.put(current.key, current.value)
        self.data = new_hashTable.data
        self.capacity = new_hashTable.capacity

if __name__ == "__main__":
    ht = HashTable(8)
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
