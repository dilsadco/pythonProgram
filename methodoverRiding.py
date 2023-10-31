class A:
  def Show(self):
    print("Akash chhamiya hai")

class B(A):
  def Show(self):
    super().Show()
    print("Abhimanyu abhi hai")

obj=B()
obj.Show()