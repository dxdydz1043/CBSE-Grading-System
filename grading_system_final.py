#modules imported

import csv
import mysql.connector as ms

#connecting mysql to python

mycon=ms.connect(host='localhost',\
                 user='root',\
                 password='susiram2003',\
                 database='grade_system')
crsr=mycon.cursor()
l=[]

#working with csv file

with open('C:\\VS Code projects\\grad_data.csv','r') as f:
    a=csv.reader(f,delimiter=',')
    for i in a :
        l+=[i]
l.pop(0)
l.pop(0)
l.pop(0)
l.pop(0)

#sql table creation and modifications

crsr.execute('drop table Stud_info')
crsr.execute('drop table eng')
crsr.execute('drop table lang')
crsr.execute('drop table mat')
crsr.execute('drop table sci')
crsr.execute('drop table soc')
crsr.execute('drop table eng1')
crsr.execute('drop table mat1')
crsr.execute('drop table lang1')
crsr.execute('drop table sci1')
crsr.execute('drop table soc1')

sql_cmd="""
CREATE TABLE Stud_info ( UNIQUE_ID INTEGER  
,NAME VARCHAR(60), ENGLISH INTEGER, ENG_GRADE 
VARCHAR(5),LANG INTEGER,LANG_GRADE VARCHAR(5),MATHS 
INTEGER,MAT_GRADE VARCHAR(5),SCIENCE INTEGER,SCI_GRADE 
VARCHAR(5),SOCIAL INTEGER,SOC_GRADE VARCHAR(5),TOTAL INTEGER)"""
crsr.execute(sql_cmd)
print('table created\n')

for i in range(0,40):
    cmd = """INSERT INTO Stud_info (UNIQUE_ID,NAME,
    ENGLISH,ENG_GRADE ,LANG ,LANG_GRADE ,MATHS,MAT_GRADE,
    SCIENCE ,SCI_GRADE ,SOCIAL ,SOC_GRADE ,TOTAL)
    VALUES("{UI}","{N}","{E}","{EG}","{L}","{LG}","{M}",
    "{MG}","{S}","{SG}","{ST}","{STG}","{TOT}")"""
    sql_cmd=cmd.format(UI=int(l[i][3]),N=l[i][4],E=int(l[i][5]),\
        EG=l[i][6],L=int(l[i][7]),LG=l[i][8],M=int(l[i][9]),MG=l[i][10],\
        S=int(l[i][11]),SG=l[i][12],ST=int(l[i][13]),STG=l[i][14],\
        TOT=int(l[i][15]))
    crsr.execute(sql_cmd)
print('records are successfully added\n')

sql_cmd1='''create table eng(unique_id INTEGER,eng INT,eng_grade VARCHAR(5))'''
sql_cmd2='''create table lang(unique_id INTEGER,lang INT,lan_grade VARCHAR(5))'''
sql_cmd3='''create table mat(unique_id INTEGER,mat INT,mat_grade VARCHAR(5))'''    
sql_cmd4='''create table sci(unique_id INTEGER,sci INT,sci_grade VARCHAR(5))'''
sql_cmd5='''create table soc(unique_id INTEGER,soc INT,soc_grade VARCHAR(5))'''

crsr.execute(sql_cmd1)
crsr.execute(sql_cmd2)
crsr.execute(sql_cmd3)
crsr.execute(sql_cmd4)
crsr.execute(sql_cmd5)

sql_cmd1= '''insert into eng select unique_id,english,NULL from stud_info'''
sql_cmd2='''insert into lang select unique_id,lang,NULL from stud_info'''
sql_cmd3='''insert into mat select unique_id,maths,NULL from stud_info'''
sql_cmd4= '''insert into sci select unique_id,science,NULL from stud_info'''
sql_cmd5=''' insert into soc select unique_id,social,NULL from stud_info'''

crsr.execute(sql_cmd1)
crsr.execute(sql_cmd2)
crsr.execute(sql_cmd3)
crsr.execute(sql_cmd4)
crsr.execute(sql_cmd5)

print('values added\n')

#working with dictionaries

deng={}
dlang={}
dmat={}
dsci={}
dsoc={}

for i in ['eng','lang','mat','sci','soc']:
    crsr.execute('SELECT * FROM '+i)
    rec=crsr.fetchall()
    if i=='eng':
        for j in range(len(rec)) :
            deng[rec[j][0]]={}
            deng[rec[j][0]][rec[j][1]]=rec[j][2]
    elif i=='lang':
        for j in range(len(rec)) :
            dlang[rec[j][0]]={}
            dlang[rec[j][0]][rec[j][1]]=rec[j][2]
    elif i=='mat':
        for j in range(len(rec)) :
            dmat[rec[j][0]]={}
            dmat[rec[j][0]][rec[j][1]]=rec[j][2]
    elif i=='sci':
        for j in range(len(rec)) :
            dsci[rec[j][0]]={}
            dsci[rec[j][0]][rec[j][1]]=rec[j][2]
    elif i=='soc':
        for j in range(len(rec)) :
            dsoc[rec[j][0]]={}
            dsoc[rec[j][0]][rec[j][1]]=rec[j][2]

leng,llang,lmat,lsci,lsoc=[],[],[],[],[]

for i in deng.values():
    leng.extend(list(i.keys()))
for i in dlang.values():
    llang.extend(list(i.keys()))
for i in dmat.values():
    lmat.extend(list(i.keys()))
for i in dsci.values():
    lsci.extend(list(i.keys()))
for i in dsoc.values():
    lsoc.extend(list(i.keys()))

for i in [leng,llang,lmat,lsci,lsoc]:
     i.sort()

leng1,llang1,lmat1,lsci1,lsoc1=[],[],[],[],[]
for i in range(8):
     l1=[]
     for j in range(5):
          l1.append(leng.pop())
     leng1+=[l1]
for i in range(8):
     l1=[]
     for j in range(5):
          l1.append(llang.pop())
     llang1+=[l1]
for i in range(8):
     l1=[]
     for j in range(5):
          l1.append(lmat.pop())
     lmat1+=[l1]
for i in range(8):
     l1=[]
     for j in range(5):
          l1.append(lsci.pop())
     lsci1+=[l1]
for i in range(8):
     l1=[]
     for j in range(5):
          l1.append(lsoc.pop())
     lsoc1+=[l1]

#sorting of marks

for i in [leng1,llang1,lmat1,lsci1,lsoc1]:
    for j in range(0,len(i)-1):
        a=i[j][-1]
        b=i[j+1][0]
        Ca=i[j].count(a)
        Cb=i[j+1].count(b)
        if a==b:
            if Ca<Cb:
                    for z in range(Ca):
                        i[j+1].insert(0,a)
                        i[j].pop()
            elif Ca>Cb:
                    for z in range(Cb):
                        i[j].insert(-1,b)
                        i[j+1].pop(0)
            elif Ca==Cb:
                    for z in range(Cb):
                        i[j].insert(-1,b)
                        i[j+1].pop(0)

#assigning the grades

for i in [deng,dlang,dmat,dsci,dsoc]:
    for j in i:
        for k in i.get(j):
            if i==deng:
                    if k in leng1[0]:
                        i[j][k]='A1'
                    if k in leng1[1]:
                        i[j][k]='A2'
                    if k in leng1[2]:
                        i[j][k]='B1'
                    if k in leng1[3]:
                        i[j][k]='B2'
                    if k in leng1[4]:
                        i[j][k]='C1'
                    if k in leng1[5]:
                        i[j][k]='C2'
                    if k in leng1[6]:
                        i[j][k]='D'
                    if k in leng1[7]:
                        i[j][k]='E'
            if i==dlang:
                    if k in llang1[0]:
                        i[j][k]='A1'
                    if k in llang1[1]:
                        i[j][k]='A2'
                    if k in llang1[2]:
                        i[j][k]='B1'
                    if k in llang1[3]:
                        i[j][k]='B2'
                    if k in llang1[4]:
                        i[j][k]='C1'
                    if k in llang1[5]:
                        i[j][k]='C2'
                    if k in llang1[6]:
                        i[j][k]='D'
                    if k in llang1[7]:
                        i[j][k]='E'
            if i==dmat:
                    if k in lmat1[0]:
                        i[j][k]='A1'
                    if k in lmat1[1]:
                        i[j][k]='A2'
                    if k in lmat1[2]:
                        i[j][k]='B1'
                    if k in lmat1[3]:
                        i[j][k]='B2'
                    if k in lmat1[4]:
                        i[j][k]='C1'
                    if k in lmat1[5]:
                        i[j][k]='C2'
                    if k in lmat1[6]:
                        i[j][k]='D'
                    if k in lmat1[7]:
                        i[j][k]='E'
            if i==dsci:
                    if k in lsci1[0]:
                        i[j][k]='A1'
                    if k in lsci1[1]:
                        i[j][k]='A2'
                    if k in lsci1[2]:
                        i[j][k]='B1'
                    if k in lsci1[3]:
                        i[j][k]='B2'
                    if k in lsci1[4]:
                        i[j][k]='C1'
                    if k in lsci1[5]:
                        i[j][k]='C2'
                    if k in lsci1[6]:
                        i[j][k]='D'
                    if k in lsci1[7]:
                        i[j][k]='E'
            if i==dsoc:
                    if k in lsoc1[0]:
                        i[j][k]='A1'
                    if k in lsoc1[1]:
                        i[j][k]='A2'
                    if k in lsoc1[2]:
                        i[j][k]='B1'
                    if k in lsoc1[3]:
                        i[j][k]='B2'
                    if k in lsoc1[4]:
                        i[j][k]='C1'
                    if k in lsoc1[5]:
                        i[j][k]='C2'
                    if k in lsoc1[6]:
                        i[j][k]='D'
                    if k in lsoc1[7]:
                        i[j][k]='E'       

for i in [deng,dlang,dmat,dsci,dsoc]:
    if i==deng:
      te=tuple()
      te1=tuple()
      for j in i:
        for k in i.get(j):
            te1+=((j,k,i[j][k]),)
      te+=(te1)
    
    if i==dlang:
      tl=tuple()
      tl1=()
      for j in i:
        for k in i.get(j):
            tl1+=((j,k,i[j][k]),)
      tl+=(tl1)
    
    if i==dmat:
      tm=tuple()
      tm1=()
      for j in i:
        for k in i.get(j):
            tm1+=((j,k,i[j][k]),)
      tm+=(tm1)
    
    if i==dsci:
      ts=tuple()
      ts1=()
      for j in i:
        for k in i.get(j):
            ts1+=((j,k,i[j][k]),)
      ts+=(ts1)
    
    if i==dsoc:
      tso=tuple()
      tso1=()
      for j in i:
        for k in i.get(j):
            tso1+=((j,k,i[j][k]),)
      tso+=(tso1)

sql_cmd1='''create table eng1(unique_id INTEGER,eng INT,eng_grade VARCHAR(5))'''
sql_cmd2='''create table lang1(unique_id INTEGER,lang INT,lang_grade VARCHAR(5))'''
sql_cmd3='''create table mat1(unique_id INTEGER,mat INT,mat_grade VARCHAR(5))'''    
sql_cmd4='''create table sci1(unique_id INTEGER,sci INT,sci_grade VARCHAR(5))'''
sql_cmd5='''create table soc1(unique_id INTEGER,soc INT,soc_grade VARCHAR(5))'''
crsr.execute(sql_cmd1)
crsr.execute(sql_cmd2)
crsr.execute(sql_cmd3)
crsr.execute(sql_cmd4)
crsr.execute(sql_cmd5)

for i in range(len(te)):
    cmd='''insert into eng1 values("{u}","{m}","{g}")'''
    sql_cmd=cmd.format(u=te[i][0],m=te[i][1],g=te[i][2])
    crsr.execute(sql_cmd)
for i in range(len(tl)):
    cmd='''insert into lang1 values("{u}","{m}","{g}")'''
    sql_cmd=cmd.format(u=tl[i][0],m=tl[i][1],g=tl[i][2])
    crsr.execute(sql_cmd)
for i in range(len(tm)):
    cmd='''insert into mat1 values("{u}","{m}","{g}")'''
    sql_cmd=cmd.format(u=tm[i][0],m=tm[i][1],g=tm[i][2])
    crsr.execute(sql_cmd)
for i in range(len(ts)):
    cmd='''insert into sci1 values("{u}","{m}","{g}")'''
    sql_cmd=cmd.format(u=ts[i][0],m=ts[i][1],g=ts[i][2])
    crsr.execute(sql_cmd)
for i in range(len(tso)):
    cmd='''insert into soc1 values("{u}","{m}","{g}")'''
    sql_cmd=cmd.format(u=tso[i][0],m=tso[i][1],g=tso[i][2])
    crsr.execute(sql_cmd)

print("table created and records added successfully\n")

f=tuple()
for i in range(len(te)):
    a1=tuple()
    a=int(l[i][3])
    n=l[i][4]
    if a==te[i][0] and a==tl[i][0] and a==tm[i][0]and\
    a==ts[i][0] and a==tso[i][0]:
        a1+=((a,n,te[i][1],te[i][2],tl[i][1],tl[i][2],\
            tm[i][1],tm[i][2],ts[i][1],ts[i][2],tso[i][1],\
            tso[i][2]),)
    f+=(a1)

print('\t\t\t*****GRADE ANALYSIS*****')
print('\t\t\t\t1.SHOW ENTIRE CLASS')
print('\t\t\t\t2.SHOW EACH SUBJECT SCORE')

#interacting with the user

ch=int(input("enter your choice from the menu:"))
if ch==2:
        sub=input("enter the subject(eng/lang/mat/sci/soc):")
        print("%10s"%"unique_id","%30s"%"name","%10s"%"mark","%10s"%"grade")
        print("==================================================================")
        for i in ['eng','lang','mat','sci','soc']:
            if sub==i:
                sql_cmd="select stud_info.unique_id,stud_info.NAME,\
                "+i+'1'+'.'+i+','+i+'1'+'.'+i+'_grade from stud_info,\
                '+i+'1 where stud_info.unique_id='+i+'1'+'.unique_id' 
                crsr.execute(sql_cmd)
                a=crsr.fetchall()
                for z in a:
                   print("%10s"%z[0],"%30s"%z[1],"%10s"%z[2],"%10s"%z[3])
                print("================================================\
                      ==================")
                print('Thank you!!')
                break
elif ch==1:
        print("%10s"%"unique_id","%30s"%"name","%10s"%"Eng",\
            "%10s"%"Eng_grade","%10s"%"Lang","%10s"%"Lang_grade",\
            "%10s"%"Mat","%10s"%"Mat_grade","%10s"%"Sci",\
            "%10s"%" Sci_grade""%10s"%"Soc","%10s"%" Soc_grade")
        print("==================================================\
              =====================================================\
              =============================================================")
        for z in f:
            print("%10s"%z[0],"%30s"%z[1],"%10s"%z[2],"%10s"%z[3],"%10s"%z[4],\
                "%10s"%z[5],"%10s"%z[6],"%10s"%z[7],"%10s"%z[8],"%10s"%z[9],\
                "%10s"%z[10],"%10s"%z[11])
        print("==============================================================\
              ==============================================================\
              ==========================================")
        print("Thank you")

mycon.commit()
mycon.close()

