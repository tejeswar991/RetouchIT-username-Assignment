# The Diamond Problem: 
# Multiple Inheritence :
#      A (Grandparent)
#     / \
#    B   C (Parents)
#     \ /
#      D (Child)

class A:
    def __init__(self):
        print("initializing A")
    
    def foo(self):
        pass

class B(A):
    def __init__(self):
        super().__init__() 
        print("initializing B")
    
    def foo(self):
        return "Implementation of B"

class C(A):
    def __init__(self):
        super().__init__()
        print("initializing C")
    
    def foo(self):
        return "Implementation of C"

class D(B, C):
    def __init__(self):
        # Starts the chain reaction. Python follows the order: D -> B -> C -> A
        super().__init__() 
        print("initialising D") # 
    
    def foo(self): # Override foo to resolve ambiguity
        res_b = B.foo(self) # Call B foo
        res_c = C.foo(self) # Call C foo
        return f"D resolves diamond by using: [{res_b}] AND [{res_c}]"

d = D() # Create the object 
print(d.foo()) # Call the method