# main.py

from addition import Addition
from subtraction import Subtraction
from multiply_divide import MultiplyDivide

def main():
    addition = Addition()
    subtraction = Subtraction()
    multiply_divide = MultiplyDivide()

    while True:
        print("\n=== Kalkulator Modular ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        choice = input("Pilih operasi (1-5): ")

        if choice == "5":
            print("Terima kasih! Keluar program.")
            break

        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))

            if choice == "1":
                result = addition.add(a, b)
                print(f"Hasil penjumlahan: {result}")
            elif choice == "2":
                result = subtraction.subtract(a, b)
                print(f"Hasil pengurangan: {result}")
            elif choice == "3":
                result = multiply_divide.multiply(a, b)
                print(f"Hasil perkalian: {result}")
            elif choice == "4":
                result = multiply_divide.divide(a, b)
                print(f"Hasil pembagian: {result}")
            else:
                print("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
