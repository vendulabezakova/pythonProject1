class Employee:
  def getNetSalary(self):
    tax = self.grossSalary * 0.15 - self.children * 1500
    return self.grossSalary - tax

  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."

  def __init__(self, name, position, grossSalary, children):
    self.name = name
    self.position = position
    self.grossSalary = grossSalary
    self.children = children

zam1 = Employee("Petr Havlík", "vědecký pracovník", 45000, 2)
print(zam1.getNetSalary())