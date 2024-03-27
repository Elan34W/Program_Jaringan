

def farenheit_to_celcius(farenheit):
    return(farenheit - 32) * 5/9

def celsius_to_farenheit(celsius):
    return(celsius * 9/5) +32

pilihan = input("Masukkan angka 1 atau 2 : ")

if(pilihan == '1'):
    farenheit = float(input("Masukkan Suhu : "))
    celsius = farenheit_to_celcius(farenheit)
    print("{:.2f} farenheit = {:.2f} celsius".format(farenheit,celsius))

elif pilihan == '2':
    celsius = float(input("Masukkan Suhu : "))
    farenheit = celsius_to_farenheit(celsius)
    print("{:.2f} celsius = {:.2f} farenheit".format(celsius,farenheit))

else:
    print("Pilihan Tidak valid.")

