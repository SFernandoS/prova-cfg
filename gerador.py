import random
import string

def NUMBER():
    return str(random.randint(1, 100))

def random_example() -> str:
    return fizz()

def fizzbuzz() -> str:
    aux:string = NUMBER() + ", "
    if random.random() < 0.5:
        aux += fizzbuzz()
        
    return aux

def fizz() -> str:
    str:string = ""

    if(random.choice(["x", "z"]) == "x"):
        str += "fizz"
    else:
        str += "fizz(" + fizz()
        if random.random() < 0.8:
            str += ", " + buzz()
        str += ")"

    return str

def buzz() -> str:
    str:string = ""

    if(random.choice(["x", "z"]) == "x"):
        str += "buzz"
    else:
        str += "buzz(" + fizzbuzz() + buzz() + ")"

    return str

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"{i}) {random_example()}")