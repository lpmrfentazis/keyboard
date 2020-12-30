from csv import writer

with open("statistics/{}.cvs".format(input("Enter sesion name: ")), "w", newline="") as f:
        csv = writer(f, dialect = 'excel')
        csv.writerow([input(), input()])
        csv.writerows([[input(),input()], ["12","33"], "3r"])
