R1 = {"name": "CKV1","IP":"1.1.1.1", "OS": "Cisco"}
R2 = {"name": "CKV2","IP":"2.1.1.1", "OS": "Juniper"}
R3 = {"name": "CKV3","IP":"3.1.1.1", "OS": "Cisco"}
R4 = {"name": "CKV4","IP":"4.1.1.1", "OS": "Juniper"}
R5 = {"name": "CKV5","IP":"5.1.1.1", "OS": "Cisco"}
R_lst = [R1,R2,R3,R4,R5]
def sch(ds,name):
    for i in ds:
        if name == i["name"]:
            for row in i:
                print(row + ':' + i[row])
                
      



sch(R_lst,"CKV2")
