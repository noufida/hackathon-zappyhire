#APPROACH 2
#user enters the ctc
#loop through columnA of salary structure  and checks whether there is such a column which is the most independent one. 
#if found, change the value of column to the entered ctc
#call the functionsvone by one which is having formulas to update the data in cells which are dependent on this ctc

#LIMITATION:this method wont work with a differnt salary structure.

import openpyxl
 
wb = openpyxl.load_workbook("test.xlsx",data_only=True)
 
ws = wb.active
a=0
basic_salary=0
def basic_salary():
    for x in range(9,20):
        if ws['A'+str(x)].value == 'basic_salary':
            ws['B'+str(x)].value=ws['B'+str(a)].value*0.5
            ws['C'+str(x)].value=(ws['B'+str(a)].value*0.5)/12
            wb.save("test.xlsx")
            basic_salary=ws['C'+str(x)].value
            print("monthly basic salary =",basic_salary)
            print("annual basic salary =", ws['B'+str(x)].value)

def hra():
    for x in range(9,20):
        if ws['A'+str(x)].value == 'HRA':
            ws['B'+str(x)].value=ws['B'+str(x-1)].value*0.5
            ws['C'+str(x)].value=(ws['B'+str(x)].value)/12
            wb.save("test.xlsx")
            monthly_hra=ws['C'+str(x)].value
            annual_hra=ws['B'+str(x)].value
            print("annual hra=",annual_hra)
            print("monthly hra=",monthly_hra)

def employer_esi():
    for x in range(9,20):
        if ws['A'+str(x)].value == 'Employer_ESI':
            if ws['B'+str(x+1)].value<252001:
                ws['B'+str(x)].value=ws['B'+str(x+1)].value*0.0325
                ws['C'+str(x)].value=(ws['B'+str(x)].value)/12
            else:
                ws['B'+str(x)].value=0
                ws['C'+str(x)].value=(ws['B'+str(x)].value)/12
            wb.save("test.xlsx")
            monthly_ESI=ws['C'+str(x)].value
            annual_ESI=ws['B'+str(x)].value
            print("annual ESI=",annual_ESI)
            print("monthly ESI=",monthly_ESI)


base_salary=(int(input("enter ctc")))
for x in range(9,20):
    if ws['A'+str(x)].value == 'base_salary':
        ws['B'+str(x)].value=base_salary
        a=x
        
# print(a,"base")
wb.save("test.xlsx")

basic_salary()
hra()
employer_esi()
# base_salary=ws['B14'].value

