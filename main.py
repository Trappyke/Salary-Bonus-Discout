#printsenter salary amount
salary= float(input ("Enter your salary: "))

#prints enter no of years 
years= int(input ("Enter your years of service: "))

if years >10:
    bonus = 0.12 * salary
    net_salary = bonus + salary
    print("Bonus: ", bonus)
    print ("net salary: ",net_salary)
elif years >=6 and years <=10:
    bonus=0.1*salary
    net_salary=bonus+salary
    print("Bonus: ", bonus)
    print ("net salary: ",net_salary)
elif years <6:
    bonus=0.08*salary
    net_salary=bonus+salary
    print("Bonus: ", bonus)
    print ("net salary: ",net_salary)
else:
    print("Try Again")