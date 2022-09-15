Lucas Larking Tk20 Moment02

################## Moment 02A ################################


import math
radius = int(input("Enter radius of circle in a whole number "))

area = 3.14*radius**2
omkrats = 2*3.14*radius
print("Radien är", radius)
print("Omkretsen på cirkeln är", "{:.2f}".format(omkrats))
print("Arean på cirkeln är", "{:.2f}".format(area))

################## FörDjupning ################################
radius = float(input("Enter radius of circle in a whole number "))
if radius.is_integer():
    nRadius = int(radius)
    print('aspdokaspäok')
else:
    nRadius = radius

area = math.pi*nRadius**2
omkrats = 2*math.pi*nRadius
print("Radien är", nRadius)
print("Omkretsen på cirkeln är", "{:.2f}".format(omkrats))
print("Arean på cirkeln är", "{:.2f}".format(area))


################## Moment 02B ################################


# Ta in variabler och rätt rätt värde
sekonds = int(input("Hur många sekunder ska konverteras? "))
hour = int(sekonds / 3600)
sekonds -= hour * 3600
minutes = int(sekonds / 60)
sekonds -= minutes * 60
#skriv ut
print(f"{hour}h{minutes}m{sekonds}s")


######################## FÖRDJUPNING #########################


##### Fördjupning 1 ###########
print('###### Fördjupning 1 ###########')
# Ta in variabler och rätt rätt värde
sekonds = int(input("Hur många sekunder ska konverteras? "))
hour = int(sekonds / 3600)
sekonds -= hour * 3600
minutes = int(sekonds / 60)
sekonds -= minutes * 60

#skriv ut
print(f"{hour:02d}h{minutes:02d}m{sekonds:02d}s")

##### Fördjupning 2 ###########
print('###### Fördjupning 2 ###########')
sekonds = int(input("Hur många sekunder? "))
minutes = int(input("Hur många minuter? "))
hour = int(input("Hur många timmar? "))


totalSekonds = sekonds + (minutes * 60) + (hour * 3600)
print(f"Totalt är detta {totalSekonds}s")


###### Fördjupning 3 ###########
print('###### Fördjupning 3 ###########')
biggerNum = None
smallerNum = None
diff = None
sekonds1 = int(input("Hur många sekunder vid första tiden? "))
minutes1 = int(input("Hur många minuter vid första tiden? "))
hour1 = int(input("Hur många timmar vid första tiden? "))
total1 = sekonds1 + (minutes1 * 60) + (hour1 * 3600)


sekonds2 = int(input("Hur många sekunder vid andra tiden? "))
minutes2 = int(input("Hur många minuter vid andra tiden? "))
hour2 = int(input("Hur många timmar vid andra tiden? "))
total2 = sekonds2 + (minutes2 * 60) + (hour2 * 3600)

# Ta reda på vilket de större talet är
if total1 == total2:
    print('Ingen skillnad mellan tiderna')
elif total1 > total2:
    biggerNum = total1
    smallerNum = total2
else:
    biggerNum = total2
    smallerNum = total1

diff = biggerNum - smallerNum


diffHour = int(diff / 3600)
diff -= diffHour * 3600
diffMinutes = int(diff / 60)
diff -= diffMinutes * 60
print(f"{diffHour:02d}h{diffMinutes:02d}m{diff:02d}s")
