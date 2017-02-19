class Student:
    __name = ""
    def __init__(self,name):
        self.__name__=name
    def getName(self):
        return  self.__name

if __name__ == "__main__":
    print 'Hello World'
    student=Student("guxh")
    print student.getName()