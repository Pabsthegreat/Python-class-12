import csv
with open("diNero.csv") as f:
    csvr = csv.reader(f)
    year = input("Enter the year:")
    for i in csvr:
        if year ==  i[0][:4] :
            print(i)

    f.seek(0)
    csvr= csv.reader(f)
    for i in csvr:
        if i[2][:5] == ' "The':
            print(i)
    
    row  = [2015,61,' "The Intern"']
    csvw  = csv.writer(f)
    csvw.writerow(row)
            
        
