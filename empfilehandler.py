
filename:str = "payroll.csv"

def savelist(payroll_list:list)->None:
    f = open(filename, "w")
    for employee in payroll_list:
        emp = " ".join(employee)
        f.write(emp+"\n")
    f.close()

def loadlist()->list:
    f = open("payroll.csv", "r")
    mlist: list = []
    for item in f:
        if item.strip()=="": pass
        else:
            item_list = item.strip().split(' ')
            mlist.append(item_list)
    f.close()
    return mlist