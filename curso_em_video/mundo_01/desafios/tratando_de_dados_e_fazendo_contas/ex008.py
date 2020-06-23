m = float(input('digite um valor em metros para conversão:'))

dam = (m / 10)
hm = (m/100)
km = (m/1000)

dm = (m * 10)
cm = (m * 100)
mm = (m * 1000)

print('o valor de {}m equivale \n '
      '{}dm \n '
      '{}cm \n '
      '{}mm'
      .format(m, dm, cm, mm))

print('também {}m equivalem \n '
      '{}dam \n '
      '{}hm \n '
      '{}km'
      .format(m, dam, hm, km))
