numbers = [10,20,30,50] #list , dictionary, set, tuple are all iterable objects in python
it = iter(numbers) #iter() used to convert any iterable objects inot iterator
print(next(it))
print(next(it))
print(next(it)) 
print(next(it))
#iterators with string
name = "Nicky"
it = iter(name)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#iterators with for loop
numbers = [10,20,30,50]
for i in numbers:
    print(i)
#iterators with while loop
numbers = [325,542,956,157,756]
it = iter(numbers)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

my_list=[10,50,30]
iter(my_list)
print(iter(my_list))

#counting numbers using iterators
class count:
    def __init__(self, limit):
        self.limit = limit
        self.count = 1
    def __iter__(self):
            return self
    def __next__(self):
        if self.count <= self.limit:
                val = self.count
                self.count +=1
                return
            
        else:
            raise StopIteration
counter = count(5)
for i in counter:
    print(i)

#Custom iterator

class MyList:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

obj = MyList([100, 200, 300])

for item in obj:
    print(item)



