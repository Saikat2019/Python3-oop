class Employee:			#class
	def __init__(self, first, second,pay):   #constructor
		self.first = first	# self passes the instance of the class
		self.second = second #first,sceond,pay,email are attributes of the class
		self.pay = pay
		self.email = first + '.' + second + '@gmail.com'
#each method in a class automatically takes the instance as 1st variable
#here it's self,you can name it anything 
	def fullname(self):
		return '{} {}'.format(self.first,self.second)

emp_1 = Employee('corey','schafer',20000)  #instance of the class
emp_2 = Employee('saikat','mondal',10000)

#emp_1.email = 'saikat'

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname()) # need thi '()' as it's a method
print(Employee.fullname(emp_1)) #this is what goes in background when 
								#the previous line runs