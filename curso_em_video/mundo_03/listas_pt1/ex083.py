#EX083

formula = input()
contaParen = 0
for carac in formula:
 if '(' == carac:
  contaParen += 1
 elif ')' == carac:
    if contaParen == 0:
        contaParen -= 1
        break
    else:
        contaParen -= 1
        
if contaParen == 0:
 print('Fórmula aceita!')
else:
 print('Fórmula com erro!')