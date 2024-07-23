#Invoice Class
class Invoice:
    def __init__(self, part_number, part_description, quantity, price):
        self.part_number = part_number
        self.part_description = part_description
        self._quantity = quantity
        self._price = price

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print("Quantity can not be negative")
        else:
            self._quantity = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price can not be negative")
        else:
            self._price = value
    
    def get_invoice_amount(self):
        return self._quantity * self._price


def InvoiceTest():
    invoice = Invoice(3000, "T-shirts", 500, 3200)
    print(f"Part Number: {invoice.part_number}")
    print(f"Part Description: {invoice.part_description}")
    print(f"Quantity: {invoice.quantity}")
    print(f"Price per Item: {invoice.price}")
    print(f"Total Invoice Amount: {invoice.get_invoice_amount()}")

    #Trying to set negative values
    invoice.quantity = -5
    invoice.price = -20

    #Setting valid quantities
    invoice.quantity = 200
    invoice.price = 1200

print(InvoiceTest())




#Employee Class
class Employee:
    def __init__(self,firstname, lastname, monthly_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.monthly_salary = monthly_salary
    
    @property
    def monthlySalary(self):
        return self.monthly_salary
    
    @monthlySalary.setter
    def monthlySalary(self, value):
        if value < 0:
            print("Monthly salary cannot be negative")
        else:
            self.monthly_salary = value
    
    def yearlySalary(self):
        return self.monthly_salary * 12
    
    def giveRaise(self, percentage):
        self.monthly_salary += self.monthly_salary * (percentage / 100)
    
#Test App
def EmployeeTest():
    employee1 = Employee("John", "Doe", 30000)
    employee2 = Employee("Jane", "Smith", 25000)

    print(f"{employee1.firstname} {employee1.lastname}'s Yearly Salary: {employee1.yearlySalary()}")
    print(f"{employee2.firstname} {employee2.lastname}'s Yearly Salary: {employee2.yearlySalary()}")

    employee1.giveRaise(10)
    employee2.giveRaise(10)

    print(f"After 10% raise, {employee1.firstname} {employee1.lastname}'s Yearly Salary: {employee1.yearlySalary()}")
    print(f"After 10% raise, {employee2.firstname} {employee2.lastname}'s Yearly Salary: {employee2.yearlySalary()}")

print(EmployeeTest())