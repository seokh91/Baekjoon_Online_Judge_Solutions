grade=input()
temp_list=list(grade)

dic_gra={'A':{'+':4.3,'0':4.0,'-':3.7}, 'B':{'+':3.3,'0':3.0,'-':2.7}, 'C':{'+':2.3,'0':2.0,'-':1.7}, 'D':{'+':1.3,'0':1.0,'-':0.7}}

if grade=='F': print(0.0)
else : print(dic_gra[temp_list[0]][temp_list[1]])
