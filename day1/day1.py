'''#q1
x=3
y='3.0'
print(int(x+float(y)))

print("")

#q2
a=3
A=4
print(a+3+7)

print("")

#q3
x=3
print(3+True)

print("")

#q4
name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
if(name=='Abijith'):
    print("My name is",name,"and my age is",age)
else:
    print("Name is invalid!!")
    
print("")

#q5
def main():
    name=[]
    age=[]
    for i in range(0,2,1):
        x=str(input("Enter your name: "))
        y=int(input("Enter your age: "))
        name.append(x)
        age.append(y)
        print("")
    name.sort()
    age.sort()
    length=len(name)
    prnt(name,age,length)
    
def prnt(n,a,l):
    print("My name is",n[l-1],"and my age is",a[l-1])
main()

print("")

#q6
hm=[]
subj=int(input("Number of subjects: "))
maxm=int(input("Enter max marks per subject: "))
print("")
add=0
hmp=[]
for i in range(0,subj,1):
    x=int(input("Enter marks for subject: "))
    hm.append(x)
for i in range(0,subj,1):
    add+=hm[i]
avg=add/subj
perc=(add/(subj*maxm))*100
print("")
print("Highest marks obtained is:",max(hm))
print("Average marks obtained is:",avg)
print("Percentile obtained for all subjects is:",perc,"%")
'''

#q7
num=[]
lim=int(input("List size: "))
mid=lim//2
print("")
for i in range(0,lim,1):
    x=input("Enter values: ")
    num.append(x)
print("")
print("Middle value is:", num[mid])


