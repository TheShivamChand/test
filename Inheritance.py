""" Single Inheritance """


# class Person:
# 	def __init__(self, name, idnum):
# 		self.name = name
# 		self.idnum = idnum

# 	def display(self):
# 		print(self.name)
# 		print(self.idnum)

# class Employee(Person):
# 	def __init__(self, name, idnum, salary, post):
# 		self.salary = salary
# 		self.post = post
# 		Person.__init__(self, name, idnum)

# a = Person('Shivam', 7)
# a.display()



""" Multiple Inheritance """


# class Base1():
# 	def __init__(self):
# 		self.str1 = "Shivam"
# 		print("Base1")

# class Base2():
# 	def __init__(self):
# 		self.str2 = "Chand"
# 		print(" Base2")

# class derived(Base1, Base2):
# 	def __init__(self):
# 		Base1.__init__(self)
# 		Base2.__init__(self)
# 		print("Derived")

# 	def display(self):
# 		print(self.str1, self.str2)

# a= derived()
# a.display()


""" Multilevel Inheritance """


class Base:
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class Child(Base):
	def __init__(self, name, age):
		super().__init__(name)
		self.age = age

	def getAge(self):
		return self.age

class grandChild(Child):
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self.grade = grade

	def getGrade(self):
		return self.grade

g= grandChild("Shivam", 21, 'A')
print(g.getName(), g.getAge(), g.getGrade())