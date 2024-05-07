year = int(input("masukan tahun: "))

if year % 400 == 0:
    print(year, "tahun merupakan tahun kabista.")

elif year % 4 == 0 and year % 100 != 0:
    print(year, "tahun kabisat.")

else:
    print(year, "bukan tahun kabisat.")