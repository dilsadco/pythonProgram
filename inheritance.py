#multilevel inheritance
class Sum:
  def sumof(self):
    print("Sum of two number :",10+20)

class Sub(Sum):
  def subof(self):
    print("Subtract of two number :",50-20)

class Multi(Sub):
  def multiof(self):
    print("Sum of two number :",10*20)

disp=Multi()
disp.sumof()
disp.subof()
disp.multiof()

#Multiple inheritance
class Sum:
  def sumof(self):
    print("Sum of two number :",10+20)

class Sub:
  def subof(self):
    print("Subtract of two number :",50-20)

class Multi(Sum,Sub):
  def multiof(self):
    print("Sum of two number :",10*20)

d=Multi()
d.sumof()
d.subof()
d.multiof()