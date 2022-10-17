# Nama  : Ketrin Vani Andini
# NIM   : 20210801348
# PBO pertemuan 5


class Product:

    # class attribute
    mart = "Product"

    # instance attribute
    def __init__(self, Id_Product, Nama, Harga, Jumlah):
        self.Id_Product = Id_Product
        self.Nama = Nama
        self.Harga = Harga
        self.Jumlah = Jumlah

# instantiate Product class
a = Product("123456", "Sabun", "Rp.20.000", 2)
b = Product("1234567", "Sikat Gigi", "Rp.10.000", 5)
c = Product("12345678", "Shampoo", "Rp.30.000", 4)


# access the class attributes
print("A tergabung dalam {}".format(a.__class__.mart))

# access the instance attributes
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)

