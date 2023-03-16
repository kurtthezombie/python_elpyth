from emplist import payroll_list
filename:str = "payroll.csv"
def savelist(payroll_list:list)->None:
    f = open(filename, 'w')
    for employee in payroll_list:
        f.write(employee.strip())
        f.write("\n")
    f.close()

def loadlist()->list:
    f = open("payroll.csv", "r")
    mlist: list = []
    for item in f:
        if item.strip()=="": pass
        else:
            myitem:list = item.split(",")
            mlist.append(payroll_list)
    return mlist