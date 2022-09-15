
mytuple = (1500, 5000)
resultTuple = ()
print(f"Årsinkomst | Månadsinkomst | efter skatt | komunals | landstingss | statlig s | total skatt % |")

# for x in mytuple:

#     print(f"{x[0]:2d}         {x[1]:3d}")


for x in mytuple:

    salary = x

    yearSalary = salary * 12

    # räkna skattesattser per månad
    kTax = round(((yearSalary - 19247) * 0.2136) / 12)
    lTax = round(((yearSalary - 19247) * 0.1148) / 12)
    sTax = round(((yearSalary - 468700) * 0.2) / 12)
    vTax = round(((yearSalary - 675700) * 0.05) / 12)

    # minsta stadsskatt är 0
    if sTax < 0:
        sTax = 0
    if vTax < 0:
        vTax = 0
    statligTax = sTax + vTax

    # kvar efter saktt
    totalTax = round(kTax + lTax + sTax + vTax)
    left = salary - totalTax
    percentageTax = round((totalTax / salary) * 100)
    resultTuple
    # left = salary - kTax - lTax - vTax - sTax


    # print(f"månadslön {salary}kr (årslön {yearSalary}kr)")

    # printa ut de skatter man betalar
    # if yearSalary > 19247:
    #     print(f"Kommunal skatt, {kTax:.0f}kr")
    #     print(f"Lanstingsskatt {lTax:.0f}kr")
    #     if yearSalary > 468700:
    #         print(f"statlig skatt {statligTax:.0f}kr")

    # print(f"Kvar efter skatt {left:.0f}kr")
    # print(f"Total skatt {totalTax:.0f}kr")
    # print(f"Andel betald skatt {percentageTax:.2f}%")


    # if yearSalary < 19247:
    #     print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")
