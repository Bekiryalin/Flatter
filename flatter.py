"""Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]"""


def flat_gen(nd_list):
    if type(nd_list) is list:
        for i in nd_list:
            yield from flat_gen(i)
    else:
        yield nd_list

def flatten(nd_list):
    return list(flat_gen(nd_list))

nd_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = flatten(nd_list)
print(flat_list)
answer = [1,'a','cat',2,3,'dog',4,5]
print(flat_list == answer)

"""

Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]"""
b=[1, 'a', 'cat', 2, 3, 'dog', 4, 5]
b.reverse()
print(b)