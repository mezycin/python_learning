prices = [57.8, 46.51, 97, 55.2, 22, 15.5, 5, 84, 99.9, 38.2, 15.4]
r = []
kk = []
for i in range(len(prices)):
    i = round(prices[i] * 100)
    rub = i // 100
    kop = i % 100
    print(f'{rub:02d} руб {kop:02d} коп', end = ', ')
print('-')

prices.sort()
print(id(prices))
prices2 = sorted(prices, reverse=True)
print(id(prices2))
for i in prices2[:5]:
    i = int(round(i * 100))
    rub = i // 100
    kop = i % 100
    print(f'{rub:02d} руб {kop:02d} коп', end=', ')
print('-')