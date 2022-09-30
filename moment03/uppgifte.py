import termtables as tt
mytuple = [1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
result = []
print(f"Årsinkomst | Månadsinkomst | Total skatt | Netto / mån | komunals. | Landstingss | statlig s | Total skatt i%")
header = ["Årsinkomst", "Månadsinkomst"]


for x in mytuple:

    salary = x

    yearSalary = salary * 12
    kTax = 0
    lTax = 0
    sTax = 0
    vTax = 0

    if yearSalary >= 19247:
        kTax = ((yearSalary - 19247) * 0.2136) / 12
        lTax = ((yearSalary - 19247) * 0.1148) / 12
        if yearSalary >= 468700:
            sTax = ((yearSalary - 468700) * 0.2) / 12
            if yearSalary >= 675700:
                 vTax = ((yearSalary - 675700) * 0.05) / 12

    statligTax = sTax + vTax

    totalTax = kTax + lTax + sTax + vTax
    left = salary - totalTax
    percentageTax = (totalTax / salary) * 100
    if kTax == 0:
        percentageTax = 0

    result.append([round(salary * 12), round(salary)])



print(result)
