
#define function
def functionname():
    print('This is a function,the name is : functionname')
    a = 1+2
    print(a)

def Afunction(a,b):
	c = a+b
	print("this sum is :",c) 

#call function
functionname()
Afunction(1,2)
Afunction(a=2,b=4)

#************************************************
#变长参数,*grades
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)

report("nightmare",1,2,3,4,5,6)

#**********************************************
#关键字参数 
def portrait(name, **kw):
    print('*********************name is:', name)
    for k,v in kw.items():
        print(k, v)

portrait('nightmare',age=12,firstname="vivian",company="Net")