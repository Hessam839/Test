
'''
this is a multy line comment
for use them
'''

class test2:

	def __init__(self,x,y):
		self.x=x
		self.y=y

	def print(self):
		print("X is",self.x)
		print("Y is",self.y)

	def sum(self,first,*second):
		return sum(first,*second)


test=test2(2,3)
test.print()
print(test.sum(2,[3,4,5]))