import wtforms

contents =  dir(wtforms)


for i in contents:
    print i, type(i)
