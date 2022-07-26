names =["John","Ana",'Andres',"Albert","Mary","Dean"]
lower =[name.lower() for name in names if name[-1] != "n"]

print(lower)

lower_ = []
for name in names:
    if name[-1] != "n":
        lower_.append(name.lower())

print(lower_)



