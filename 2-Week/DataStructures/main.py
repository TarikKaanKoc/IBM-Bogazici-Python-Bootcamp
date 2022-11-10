###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################

# - Veri Yapılarına Giriş
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
##############################################

# Sayılar - Integer - int | Int

# tam sayılar
x = 45
type(x)

# Sayılar: float - ondalıklı sayılar
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String - karakter dizileri | str
x = "Merhaba dünya"
type(x)
x = 'Merhaba dünya'

# Boolean | bool
True | False
type(True)
5 == 4
3 != 2

1 == 1

type(3==2)

# List - array

x = ["Bitcoin","ETH","CHZ"]
type(x)

# Sözlük (dictionary) | dict | key-value
x = {"name": "Peter", "Age": 36}
type(x)


# Tuple (Demet)
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

###############################################
# Sayılar (Numbers): int, float, complex
###############################################

a = 5
b = 10.5

# matematiksel operatörler

a * 3
a / 8

a * b / 2

a ** 2

#######################
# Tipleri değiştirmek (Casting)
#######################

a
a = float(a)
type(a)

b

int(b)

a * b / 2
int(a * b / 2)

c = a * b / 2
c
int(c)

###############################################
# Karakter Dizileri (Strings)
###############################################

print("compec")
print('compec')
'compec'

community_name = 'compec'
community_name = "compec"

name = "John"


#######################
# Çok Satırlı Karakter Dizileri
#######################


long_str = """"Veri Yapılarına Giriş, Sayılar (Numbers): int, float, 
complex Karakter Dizileri (Strings): str Boolean (TRUE-FALSE): bool Liste (List)
Sözlük (Dictionary), Demet (Tuple), Set 
"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek | index ile erişim işlemi
#######################

name
name[0]
name[3]
name[2]
name[1]
name[-1]
name[-2]

#######################
# Karakter Dizilerinde Slice İşlemi | Dilimleme işlemi
#######################

# John
name[0:3] # [Başlangıç Değer: Bitiş Değer (Dahil değildir!)]

long_str[0:40:2] # [Başlangıç Değer: Bitiş Değer (Dahil değildir!) : Adım sayısı]

# fancy index  - Numpy kütüphanesinde görülecektir.

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str

"veri" in long_str

"Veri" in long_str


###############################################
# String (Karakter Dizisi) Metodları
###############################################


dir(str)

###############################################
# length - len() | uzunluk anlamına gelir.
###############################################

name = "Nazlı Yeniay"
type(name)
type(len)
int()
len(name)

dir(str)

###############################################
# upper() & lower() : küçük - büyük dönüşümleri
###############################################
"Bogazici University".upper()
"Bogazici University".lower()

#######################
# replace: karakter değiştirir
#######################

hi = "Hello py bootcamp"
hi.replace("l","p")

#######################
# capitalize: ilk harfi büyütür
#######################

"hiii".capitalize()

dir("foo")
"foo".startswith("l")

#######################
# List - Array
#######################

# 1. Değiştirilebilir
# 2. Sıralıdır. Index işlemleri yapılabilir
# 3. kapsayıcıdır

# List - array

x = ["Bitcoin","ETH","CHZ",True,1,1.5] # kapsayıcıdır
x
type(x)

x[0]
x[-1]

# slice

coin = x[0:3] # [Başlangıç Değer: Bitiş Değer (Dahil değildir!)]
coin

type(coin)
type(coin[0])


names = ["Ahmet","Ali","Mehmet","Veli",1,3,2,True,[1.4,1.5,1.2]]
names[-1]
names[-1][1]

names[0] = "Tarık Kaan"

###############################################
# Liste Metodları (List Methods)
###############################################
# Guido van - python

# index sayımı sıfırdan başlar
# eleman sayımı 1'den başlar
dir(names)

###############################################
# len: builtin python fonksiyonu, boyut bilgisi verir. | yani eleman bilgisi sorgular ve sonucu döndürür.
###############################################

len(names)

###############################################
# append: eleman ekleme
###############################################

names
names.append(100)
names.append(False)


###############################################
# pop: indexe göre siler
###############################################
names.pop(3)
names

###############################################
# insert: eleman ekleme | indexe göre sağlar (index, value)
###############################################
names
names.insert(0,"Ezgi")



###############################################
# SÖZLÜK : DİCT (dictionary)
###############################################

# 1. Değiştirilebilir
# 2. Sırasız | Dikkat! py 3.7 versiyonundan sonra sıralı durumda.
# 3. Kapsayıcıdır


# key - value | anahtar ve değer çiftlerinden oluşurlar
# Sözlük (dictionary) | dict | key-value
x = {"name": "Peter", "Age": 36}
type(x)

dictionary = {"REG": ["RMSE", 10], # KEY - VALUE
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["LOG"][1]

dictionary.get("LOG")
###############################################
# KEY SORGULAMA
###############################################

"LOSS" in dictionary
"LOG" in dictionary

###############################################
# Değiştirilebilir özelliği : değer değiştirmek
###############################################
dictionary["REG"] = ["LOSS",2]

###############################################
# TÜM KEY'LERE ERİŞMEK
###############################################

dictionary.keys()

###############################################
# TÜM VALUE'LEARA ERİŞMEK
###############################################
dictionary.values()

###############################################
# tüm çifleri çağırmak, key - value olarak tuple içerisinde temsil etmek
###############################################

dictionary.items()

###############################################
# UPDATE Fonksiyonu
###############################################
dictionary.update({"REG": 32})

dictionary.update({"Random Forest Algorithm": ["Acc",35]})




###############################################
# TUPLE: (Demet)
###############################################

# 1. Değiştirilemez
# 2. Sıralıdır
# 3. Kapsayıcıdır

# Tuple (Demet)
x = ("python", "ml", "ds",True,12)
type(x)

x[-1]

x[-1] = "Data engineer" # hata tuple  değiştirilemez bir veri yapısıdır. Assignment işlemini desteklememktedir.

# eleman değiştirime yolu :
x = list(x)
type(x)

x[-1] = "Data engineer" # list değiştirilebilir özelliğe sahip

x

x = tuple(x)
x
type(x)

dir(x)


###############################################
# SET
###############################################

# 1. Değiştirilebilir
# 2. Sırasız + Eşsiz
# 3. Kapsayıcıdır

# Set
x = {"python", "ml", "ds",True,12}
type(x)

dir(x)

###############################################
# difference
###############################################

first_set = set([1,2,3,4])
second_set = set([1,2,5,6])

# set2'de olup set1'de olmayanları gönder bana
second_set.difference(first_set) # Result: {5, 6}

# set1'de olup set2'de olmayanları gönder bana
first_set.difference(second_set) # Result: {3, 4}

###############################################
# symmetric_difference
###############################################

# İki kümede de birbirlerine göre olmayanlar
second_set.symmetric_difference(first_set)

first_set.symmetric_difference(second_set)


###############################################
# UNİON: İki kümenin birleşimi
###############################################
first_set.union(second_set)
second_set.union(first_set)







