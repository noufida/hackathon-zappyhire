#APPROACH 2
#user enters the ctc
#loop through columnA and checks whether there is such a column which is the most independent one. 
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
            print(basic_salary)

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


base_salary=(int(input("enter ctc")))
for x in range(9,20):
    if ws['A'+str(x)].value == 'base_salary':
        ws['B'+str(x)].value=base_salary
        a=x
print(a,"base")
wb.save("test.xlsx")
basic_salary()
hra()
# base_salary=ws['B14'].value

# for x in range(9,14):
#     for y in range(1,3):
#         char = chr(65+y)
#         temp=char+str(x)
#         if 'B14' in ws[temp].value:
#             print('yes')
        