# Problem 1

"""

1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

"""

# Çözüm 1

# Bu fonksiyon, verilen listeyi birden fazla katmanlı listelerden ve non-scalar verilere sahip bir listeyi düzleştirir. Yani, iç içe geçmiş alt listelerdeki tüm öğeleri tek bir liste halinde toplar.

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):             # Eğer öğe bir listeyse, recursive olarak flatten yap
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)             # Eğer öğe liste değilse, direk ekle
    return flat_list

# test 1

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten(input_list)
print(output) 

# Problem 2

"""

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

"""

# Çözüm 2

# Bu fonksiyon, verilen listenin elemanlarını tersine çevirir. Eğer liste elemanları da liste içeriyorsa, o alt listelerin elemanlarını da tersine çevirir.

def reverse_elements(lst):
    reversed_list = []

    for item in lst:
        if isinstance(item, list):                          # Eğer öğe bir listeyse, alt listeyi tersine çevir
            reversed_list.append(reverse_elements(item))
        else:
            reversed_list.append(item)                      # Eğer öğe liste değilse, onu olduğu gibi ekle

    return reversed_list[::-1]                              # Listeyi tersine çevir

# test 2

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_elements(input_list)
print(output)
