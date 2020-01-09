1. 创建SchoolMem类，该类中包含三种属性：姓名、性别、年龄以及针对每个属性的get和set方法；
2. 创建Student类，继承自SchoolMem类，添加额外三个属性：班级、学号和数量统计。
3. 创建Teacher类，继承自SchoolMem类，添加额外三个属性：科室、工号和数量统计。
4. 要求在Student类和Teacher类中分别实现printInfo方法，该方法打印对象的多有属性信息。
(1)代码如下：
class SchoolMem(object) :
    def __init__(self, name ='', sex = 'man', age = 20) :
        self.setName(name)
        self.setSex(sex)
        self.setAge(age)
    def getName(self) :
        return self.name
    def getSex(self) :
        return self.sex
    def getAge(self) :
        return self.age
    def setName(self,name) :
        if not isinstance(name,str) :
            print('name must be string.')
            return
        self.name = name
    def setSex(self,sex) :
        if sex != 'man' and sex != 'woman':
            print('sex must be "man" or "woman" ')
            return
        self.sex = sex
    def setAge(self,age) :
        if not isinstance(age,int) :
            print('age must be integer.')
            return
        self.age = age
    def printInfo(self) :
        print ('name:', self.getName())
        print ('sex:', self.getSex())
        print ('age:', self.getAge())

class Student(SchoolMem) :
    def __init__(self, name ='', sex = 'man', age = 20, Sclass = 1702, Snumber = 1740, Scount = 1) :
        super(Student,self).__init__(name,sex,age)
        self.setSclass(Sclass)
        self.setSnumber(Snumber)
        self.setScount(Scount)
    def setSclass(self, Sclass) :
        if not isinstance(Sclass,int) :
            print('Sclass must be integer.')
            return
        self.Sclass = Sclass
    def setSnumber(self, Snumber) :
        if not isinstance(Snumber,int) :
            print('Snumber must be integer.')
            return
        self.Snumber = Snumber
    def setScount(self, Scount) :
        if not isinstance(Scount,int) :
            print('Scount must be integer.')
            return
        self.Scount = Scount
    def printInfo(self):
        super (Student,self).printInfo()
        print ('Sclass:',self.Sclass)
        print ('Snumber',self.Snumber)
        print ('Scount',self.Scount)

class Teacher(SchoolMem) :
    def __init__(self, name ='', sex = 'man', age = 40, Tclass = 1, Tnumber = 100, Tcount = 1) :
        super(Teacher,self).__init__(name, sex, age)
        self.setTclass(Tclass)
        self.setTnumber(Tnumber)
        self.setTcount(Tcount)
    def setTclass(self, Tclass) :
        if not isinstance(Tclass,int) :
            print('Tclass must be integer.')
            return
        self.Tclass = Tclass
    def setTnumber(self, Tnumber) :
        if not isinstance(Tnumber,int) :
            print('Tnumber must be integer.')
            return
        self.Tnumber = Tnumber
    def setTcount(self, Tcount) :
        if not isinstance(Tcount,int) :
            print('Tcount must be integer.')
            return
        self.Tcount = Tcount
    def printInfo(self):
        super (Teacher,self).printInfo()
        print ('Tclass:',self.Tclass)
        print ('Tnumber',self.Tnumber)
        print ('Tcount',self.Tcount)

if __name__=='__main__' :
    zhangsan = SchoolMem('zhangsan','man', 20)
    zhangsan.printInfo()
    lisi = Student('lisi','man',20,1702,1741,1)
    lisi.printInfo()
    wangwu = Teacher('wangwu','woman',41,2,101,1)
wangwu.printInfo()
