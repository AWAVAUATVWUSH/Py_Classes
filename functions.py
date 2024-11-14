def print_menu(inlist):
    i:int=0
    iMax:int = len(inlist)
    while(i<iMax):
        print(f"{inlist[i].name}____{inlist[i].cost}")
        i+=1

def get_foods_average_cost(inlist):
    i:int=0
    iMax:int = len(inlist)
    temp:int = 0
    while(i<iMax):
        temp += inlist[i].cost
        i+=1
    return temp/iMax

def get_most_expensive_food_name(inlist):
    i:int=0
    iMax:int = len(inlist)
    temp:int = 0
    while(i<iMax):
        if(inlist[i].cost>inlist[temp].cost):
            temp = i
        i+=1
    return inlist[temp].name

def get_pay_sum(inlist):
    i:int = 0
    iMax:int = len(inlist)
    numToRet:int = 0
    while (i<iMax):
        numToRet += inlist[i].pay
        i+=1
    return numToRet

def get_oldest_worker_name(inlist):
    i:int=0
    iMax:int = len(inlist)
    temp:int = 0
    while(i<iMax):
        if(inlist[i].age>inlist[temp].age):
            temp = i
        i+=1
    return inlist[temp].name

def get_number_of_beosztott(inlist):
    i:int = 0
    iMax:int = len(inlist)
    numToRet:int = 0
    while (i<iMax):
        if(inlist[i].pos == "beosztott"):
            numToRet += 1
        i+=1
    return numToRet

def get_name_of_smallest_payed(inlist):
    i:int=0
    iMax:int = len(inlist)
    temp:int = 0
    while(i<iMax):
        if(inlist[i].pay<inlist[temp].pay):
            temp = i
        i+=1
    return temp