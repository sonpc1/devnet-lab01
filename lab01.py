ds = []
for i in range (0,5):
    ten = 'A' + str(i)
    tuoi = 25
    donvi = 'Viettel'
    temp = [ten, tuoi, donvi]
    ds.append(temp)

for row in ds:
    print('-----------------')
    for a in row:
        print(a)
    
