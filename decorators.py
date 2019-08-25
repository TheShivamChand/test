def decorator_function(original_function):
	def wrapper_function(*args,**kwargs):
		return original_function(*args,**kwargs)
	return wrapper_function


@decorator_function
def display():
	print('display function ran')
display()

@decorator_function
def display_info(name,age):
	print('display_info ran with arguments ({}, {})'.format(name,age))
display_info('Shivam',21)