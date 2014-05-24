class OpenAddressedHashArray:
    def __init__(self, length):
        self.list = list()
        for _ in range(0, length):
            self.list.append((None, None))
        
        self.sets = 0
        self.gets = 0

    def __len__(self):
        return len(self.list)

    def __getitem__(self, i):
        return self.list[i]
        
        self.gets = self.gets + 1

    def __setitem__(self, i, v):
        self.list[i] = v
        
        self.sets = self.sets + 1
        
    def __str__(self):
        return str(self.list)

    def reset_counters(self):
        self.sets = 0
        self.gets = 0
        # other statistics

    def predict_hash_type(self):
        return "this is done on ALG, and you don't get to see how it happens."