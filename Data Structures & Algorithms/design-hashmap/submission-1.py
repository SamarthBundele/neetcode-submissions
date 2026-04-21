class MyHashMap:

    def __init__(self):
        self.arr={}

    def put(self, key: int, value: int) -> None:
        if key in self.arr:
            self.arr[key]=value
        else:
            self.arr[key]=value

    def get(self, key: int) -> int:
        if key in self.arr:
            return self.arr[key]
        else:
            return -1
    
    def remove(self, key: int) -> None:
        if key in self.arr:
            self.arr.pop(key)  
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)