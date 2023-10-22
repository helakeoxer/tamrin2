nam=input("lotfan nam khod ra vared koni")
namkhanevadegi=input("lotfan nam khanevadegi khod ra vared konid")

a=int(input("lotfan nomre khod ra vared konid"))
b=int(input("lotfan nomre khod ra vared konid"))
c=int(input("lotfan nomre khod ra vared konid"))

averege=((a + b + c) / 3)

if averege >= 17:
    print("great")

if 17> averege >= 12:
    print("normal")
if averege < 12:
    print("fail")     
