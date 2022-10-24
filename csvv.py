import csv
def create():
    F=open("STUD.csv","w")
    CSVFile=csv.writer(F)
    for i in range(3):
        name=input("enter the name")
        marks=int(input("enter the marks"))
        roll=int(input("enter the roll no"))
        U=[name,marks,roll]
        CSVFile.writerow(U)
    F.close()
def display():
    F=open("STUD.csv","r")
    CSVReader=csv.reader(F)
    for i in CSVReader():
        print(i)
    F.close()
display()
