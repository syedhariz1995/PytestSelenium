
# # Q1. Diff between list and tuple

# # Ans : list is mutable, tuple is not mutable


# # List
# x = [1,2,3] 
# x.append(1)
# print(x)  # [1,2,3,1]

# x[1] = 100
# print(x) # [1,100.3.1]

# x.pop(1)
# print(x) # [1,3,1]



# # Tuple
# x = (1,2,3)
# x[0] = 100
# print(x)   # error





# #__________________________________________________________________________________________________





# # Q2. Python's buil-in data types

# x = 10    # int
# y = 3.13  # float
# d = {"name" : "Hariz"}  # Dictionary
# s = "Hello"  # string
# z = True   # boolean
# l = ["hey", 1, 45]   # list




# #__________________________________________________________________________________________________





# # Q3. How do you implement inheritance and super keyword in Python?

# class Parent:
#     def greet(self):
#         return "Hello from Parent"
    
# class Child(Parent):
#     def helloGreet(self):
#         # use super() to call the parent class method
#         return super().greet() + " and Hello from Child"

# c = Child()
# print(c.greet())       # Output: Hello from Parent
# print(c.helloGreet())  # Output: Hello from Parent and Hello from Child




# #__________________________________________________________________________________________________





# # Q4. What is init() in Python

# # The __init__() method is known as a constructor in object-oriented programming (OOP)
# # terminology. It is used to initialized an object's state when it is created . This method
# # is automatically called when a new instance of a class is instantiated.
# # To be use whn we need to send paramenters so all classes can access and use it.

# class Parent:
    
#     def greet(self):
#         return "Hello from Parent"
    
# class Child(Parent):
#     def __init__(self, title):
#         self.title = title
    
#     def helloGreet(self):
#         # use super() to call the parent class method
#         return super().greet() + " and Hello from Child" + self.title

# c = Child(" and goodbye to both")
# print(c.greet())       # Hello from Parent
# print(c.helloGreet())  # Hello from Parent and Hello from Child and goodbye to both




# #__________________________________________________________________________________________________





# # Q5. How to read and write files in python?

# # to write
# with open ("test.txt", "w") as f:
#     f.write("Hello World")

# # to read
# with open ("test.txt", "r") as f:
#     content = f.read()
#     print(content)





# #__________________________________________________________________________________________________





# # Q6. What are fictures in Pytest? When they are used?

# # Fixtures in Pytest are functions that setup test environments before a test runs and clean up afterwards
# # They help manage test dependencies, setup, teardown, and reusable data across multiple test cases
# # Key features of Pytest Fixtures : 

# # 1. Reusability - Define once, use multiple times
# # 2. Automatic setup and teardown - Handles pre-test and post-test actions
# # 3. Scope control - Fixtures can run per test , pre class, per module, or per session
# # 4. Dependencies injection - Pass fixtures as test function argument

# # example

# import pytest

# @pytest.fixture
# def sample_data():
#     print("Setup: Creating test data")   # Runs before the test
#     data = {"name" : "Alice", "Age" : 30}
#     return data   # Provides data to test

# def test_example(sample_data):
#     assert sample_data["name"] == "Alice"
#     assert sample_data["age"] == 30
#     print("Test executed successfully")





# #__________________________________________________________________________________________________





# # Q7. How do you use yield for WebDriver Setup and Tearddown in Pytest?

# import pytest

# @pytest.fixture
# def sample_data():
#     print("Setup: Creating test data")   # Runs before the test
#     data = {"name" : "Alice", "Age" : 30}
#     yield data   # will go to def test_example
#     print("cleaning up test data")

# def test_example(sample_data):
#     assert sample_data["name"] == "Alice"
#     assert sample_data["age"] == 30
#     print("Test executed successfully")





# #__________________________________________________________________________________________________





# # Q8. How do you create list of dictionaries in python?

# data = [{"name" : "Bob", "age" : 23},
#         {"name" : "Alice", "age" : 30}]

# print(data[1]["name"])  # Alice



# #__________________________________________________________________________________________________




# # Q9. What is Lambda in Python? and how is it applied to between map(), filter() functions?

# # A lambda fucntion in Python is a small, anonymous function that can have multiple arguments 
# # but only one expression.
# # It is written in a single line. 
# # It is used where a short function is needed temporarily.
# # Don't use lambda if the function is complex-use def instead.

# # normal function
# def add(x,y):
#     return x + y

# # lambda function
# add = lambda x, y : x + y


# # map with lambda
# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x: x*2, numbers))
# print(squared_numbers)  # [2, 4, 6, 8, 10]

# # filter with lambda
# even_numbers = list(filter(lambda x :  x % 2 == 0, numbers))
# print(even_numbers) # [2, 4]



# #__________________________________________________________________________________________________



# # Q10. How do you sort a list in Python?

# num = [3,2,6,1]
# print(sorted(num))





# #__________________________________________________________________________________________________





# # Q11. Is Python Asynchronous or Synchournous? What is default type? and what is asyncio?

# # Python's default behavior : Synchronous execution
# # - Python execute code line-by-line in a blocking manner
# # - Each operation must complete before the next one starts
# # - This is how Python nornally works unless explicitly told to run asynchronously

# # Python supports Asynchronous Execution using asyncio
# # - Python can run non-blocking task using asyncio
# # - Instead of waiting for one task to finish, multiple task run concurrently. 

# # normal synchronous function

# import time

# def task(name):
#     print(f"starting {name}")
#     time.sleep()
#     print(f"finished {name}")
    
# task("Syed")
# task("Hariz")



# # Asynchronous function

# import asyncio

# async def task(name):
#     print(f"starting {name}")
#     await asyncio.sleep(2)
#     print(f"finished {name}")
    
# task("Syed")
# task("Hariz")


# async def main():
#     await asyncio.gather(task("Syed"), task("Hariz"))
    
    
# asyncio.run(main())





# #__________________________________________________________________________________________________




# # Q12. Why self convention used in Python? Explain with example

# # self is not a keyword, but a convetion in Python
# # It refers to the current instance of a class.
# # It must be the first parameter in instance methods,
# # though you don't need to pass  it explicitly when calling methods

# # Unlike some languages (Java, C++), Python doesn't have an explicit "this" keyword.
# # Instead, self is used to access instance variables and methods inside the class


# class Person:
#     def __init__(self, name, age):
#         self.name = name    # Instance variable
#         self.age = age
        
    
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old"
    
# person1 = Person("Alice", 30)
# print(person1.greet())






# #__________________________________________________________________________________________________




# # Q13. How do you reverse elements of a list?

# num = [1,2,3,4,5]
# print(num[::-1])  # [5, 4, 3, 2, 1]






# #__________________________________________________________________________________________________



# # Q14. Explain the difference between @classmethod and instance methods.

# class MyClass:
#     @classmethod
#     def class_method(cls):
#         return "Class"
    
#     def instance_method(self):
#         return "Instance"
    
# obj = MyClass()

# print(obj.instance_method())
# print(obj.class_method())






# #__________________________________________________________________________________________________






# Q15. What is the use of conftest.py in Pytest?

# conftest.py is used to define fixtures and hooks that are shared across multiple test files





# #__________________________________________________________________________________________________





# Q16. How do you execute only failed test cases in pytest

# pytest --last-failed





# #__________________________________________________________________________________________________





# Q17. How do you apply a custom marker to a test case in pytest

# import pytest

# @pytest.mark.sanity
# def test_example():
#     assert True
    
# pytest -m sanity





# #__________________________________________________________________________________________________





# # Q18. What is the "with" statement designed for?

# # The "with" statement is used for exception handling to make code cleaner and simpler.
# # It is generally used for the management of common resources like creating , editing, and saving a file.

# # Example:

# # Instead of writing multiple lines of "open" ,"try", "finally", and "close", you can create and write a text file 
# # using "with" statement. It is simple.

# with open('test/txt', 'w') as file:
#     file.write('Hello world!')  





# #__________________________________________________________________________________________________




# # Q19. How to handle exception in Python? Where "finally" keyword comes in play with exceptions?

# from typing import final


# try:
#     with open ('test.txt', "r") as f:
#         content = f.read()
#         print(content)
        
# except Exception as e:
#     print(e)
    
# finally:
#     print("close db connection , clean up resources") 