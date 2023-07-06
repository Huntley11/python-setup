def hello():
    print("Greetings user") 

hello()  

def pack(x, y, z):
    pack_items = [x, y, z]
    print(pack_items)
pack(1, 2, 3)

foods = ["Apple", "Banana", "Pear"]

def eat_lunch(foods):
    print("First I eat " + foods[0])
    for food in foods[1:]:
        print("Next I eat " + food)
    
eat_lunch(foods)