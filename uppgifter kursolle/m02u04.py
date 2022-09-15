pCost = int(input("Vad är styckpriset för pennorna? "))
pAmount = int(input("Hur många pennor vill du köpa? "))
pSentence = f"Penna, {pAmount}st a {pCost}kr"
pTotal = str(pAmount * pCost)
pTotalAlign = pTotal.rjust(50 - len(pSentence))



aCost = int(input("Vad är kilopriset för äpplen? "))
aWeight = int(input("Vad är den totala kilovikten på äpplena du vill köpa?"))
aSentence = f"Äpplen, {aWeight/1000}g a {aCost}kr"
aTotal = str(aWeight * aCost)
aTotalAlign = aTotal.rjust(50 - len(aSentence))

sSentence = f"Summa "
sTotal = str(int(aTotal) + int(pTotal))
sTotalAlign = sTotal.rjust(50 - len(sSentence))

print(pSentence, pTotalAlign,'kr')
print(aSentence, aTotalAlign,'kr')
print('------------------------------------------------------')
print(sSentence, sTotalAlign,'kr')