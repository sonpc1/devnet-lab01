
hs1 = {"ten":"A", "tuoi":"25", "donvi": "VIETTEL"}
hs2 = {"ten":"B", "tuoi":"26", "donvi": "VIETTEL"}    
hs3 = {"ten":"C", "tuoi":"27", "donvi": "VIETTEL"}
hs4 = {"ten":"D", "tuoi":"25", "donvi": "VIETTEL"}
hs5 = {"ten":"E", "tuoi":"25", "donvi": "VIETTEL"}
ds = [hs1,hs2,hs3,hs4,hs5]
for row in ds:
    print("-----------------------------")
    for i in row:
        print(i + ':' + row[i])
