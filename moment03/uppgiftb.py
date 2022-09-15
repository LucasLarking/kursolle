
salary = int(input("Vad är din bruttolön? "))
yearSalary = salary * 12

# räkna skattesattser per månad
kTax = ((yearSalary - 19247) * 0.2136) / 12
lTax = ((yearSalary - 19247) * 0.1148) / 12



# kvar efter saktt
left = salary - kTax - lTax


print(f"månadslön {salary}kr (årslön {yearSalary}kr)")

# printa ut de skatter man betalar
if yearSalary > 19247:
    print(f"Kommunal skatt, {kTax:.0f}kr")
    print(f"Lanstingsskatt {lTax:.0f}kr")
 
print(f"Kvar efter skatt {left:.0f}kr")

if yearSalary < 19247:
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")
