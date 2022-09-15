
salary = int(input("Vad är din bruttolön? "))
# räkna ut skatten
kTax = salary * 0.2136
lTax = salary * 0.1148
left = salary - kTax - lTax
print("Utskrift")
print("Månadslön", salary,'kr')

# Avrunda och skriv ut
print(f"Kommunal skatt, {kTax:.0f}kr")
print(f"Lanstingsskatt {lTax:.0f}kr")
print(f"Kvar efter skatt {left:.0f}kr")




