class Calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    return self.num1 + self.num2

  def subtract(self):
    return self.num1 - self.num2

  def multiply(self):
    return self.num1 * self.num2

  def divide(self):
    if self.num2 == 0:
      return "Division by zero error"
    else:
      return self.num1 / self.num2

# Create calculator objects
calc1 = Calculator(10, 5)
calc2 = Calculator(20, 4)

# Perform calculations
print(calc1.add())  # Output: 15
print(calc2.subtract())  # Output: 16
print(calc1.multiply())  # Output: 50
print(calc2.divide())  # Output: 5.0
