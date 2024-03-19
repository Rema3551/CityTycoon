import pickle
 
class MyClass():
    def __init__(self, param):
        self.param = param
 
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 
obj = MyClass(10)
save_object(obj)

import pickle
 
class MyClass():
    def __init__(self, param):
        self.param = param
 
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
 
obj = load_object("data.pickle")
 
print(obj.param)
print(isinstance(obj, MyClass))