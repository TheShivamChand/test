def decorator_function(original_function):
	def wrapper_function(*args,**kwargs):
		return original_function(*args,**kwargs)
	return wrapper_function

class decorator_class(object):
	def __init__(self,original_function):
		self.original_function=original_function

	def __call__(self,*args,**kwargs):
		print('call method executed this before {}'.format(self.original_function.__name__))
		return self.original_function(*args,**kwargs)


@decorator_function
def display():
	print('display function ran')
display()

@decorator_function
def display_info(name,age):
	print('display_info ran with arguments ({}, {})'.format(name,age))
display_info('Shivam',21)

@decorator_class
def display():
	print('display function ran with class too')
display()

@decorator_class
def display_info(name,age):
	print('display_info ran with arguments ({}, {})'.format(name,age))
display_info('Satyam',19)