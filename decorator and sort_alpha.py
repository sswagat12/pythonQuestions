"""str1 = "Beautiful Code Is Better Than Ugly"

Write a python script to organize letters in words more reasonably(using above string) - in an alphabetical order?


Expected Output:

aBefiltuu Cdeo Is Beertt ahnT glUy
"""
# def alpha_sort(ip_str):
#     words = ip_str.split()
#     # sorting letters in each word
#     sorted_words = [''.join(sorted(word, key=lambda str:(str.lower()))) for word in words]
#     # joining sorted str
#     op  =' '.join(sorted_words)
#     return op

# test = alpha_sort('Beautiful Code Is Better Than Ugly')
# print(f"Output string is {test}")

    


"""def div(a,b):
	return a/b"""

def decorate(func):
	def wrapper(a, b):
		if a < b:
			a, b = b, a
		return func(a,b)
	return wrapper


@decorate
def div(a,b):
	return a//b


out = div(2,4)
print(f"out::::{out}")

"""Write a python program that uses inheritance to represent a hierarchy of shapes (Triangle, Rectangle etc.).
"""
# class Shapes():
#     def __init__(self):
#         pass


# class Triangle(Shapes):
#     def __init__(self) -> None:
#         pass

# class Rectangle(Shapes):
#     def __init__(self):
#         pass
