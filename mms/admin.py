from django.contrib import admin
from .models import Company, MedicalDetails, Medicine, Employee, EmployeeBank, EmployeeSalary, CompanyAccount, CompanyBank, Customer, CustomerRequest, Bill, BillDetials
# Register your models here.
admin.site.register(Company)
admin.site.register(MedicalDetails)
admin.site.register(Medicine)
admin.site.register(Employee)
admin.site.register(EmployeeBank)
admin.site.register(EmployeeSalary)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(BillDetials)
admin.site.register(CustomerRequest)