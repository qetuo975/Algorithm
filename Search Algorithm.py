# Sequential (Linear) Search With Unordered List

# Sequential Search Sıralı Arama Demektir.
# Unordered List Bir Listenin Değerleri Düzensiz Olduğu İfade Edilir.
# Listenin Başından Sırayla Taranır
# En İyi Durumda O(1) Listemin 0. İndeksi, Aradığımız Değer Bulunmazsa O(n)


def SequentialSearchUnorderedList(Array, Value):
    index = 0
    found = False

    while index < len(Array) and not found:

        if Array[index] == Value:
            found = True
        else:
            index += 1

    return (found, index)


# SequentialSearchUnorderedList([5,4,3,2,5,6],6)


# Sequential (Linear) Search With Ordered List

# Sequential Search Sıralı Arama Demektir.
# Ordered List Bir Listenin Değerleri Düzenli Olduğu İfade Edilir.
# Listenin Başından Sırayla Taranır
# En İyi Durumda O(1) Listemin 0. İndeksi, Aradığımız Değer Bulunmazsa O(n)


def SequentialSearchOrderedList(Array, Value):
    index = 0
    found = False
    stop = False

    while index < len(Array) and not found and not stop:

        if Array[index] == Value:
            found = True
        else:
            if Value < Array[index]:
                stop = True
            else:
                index += 1

    return (found, index)


# SequentialSearchOrderedList([3,4,5,6,7,8,9,11,12,13,14],10)


# Binary Search

# Sıralı Arama Yapmaz
# Binary Search Sıralı Listelerde Çok Avantajlıdır.
# Binary Search Aramaya Ortadan Başlar. Eğer Aradığı Değer Ortadaki Değerden-
# Büyük İse Sonraki Arama Adımını Listenin Upper Half Kısmında Yapar
# Binary Search Divide And Conquer ( Böl ve Fethet ) Mnatığı İle Çalışır.
# Binary Search Complexity of Algorithm Logarithmic Big O Yani O(Log n).


def BinarySearch(Array, Value):
    first_index = 0
    last_index = len(Array) - 1
    found = False

    while first_index <= last_index and not found:

        middle_index = int((first_index + last_index) / 2)

        if Array[middle_index] == Value:
            found = True

        else:
            # Lower Half
            if Value < Array[middle_index]:
                last_index = middle_index - 1
                print("Lower Half")

            # Upper Half
            else:
                first_index = middle_index + 1
                print("Upper Half")

    return found


# BinarySearch([3,6,11, 12 ,18,21,34], 18)


# Jump Search
# Jump Search Sıralı Listelerde Arama Yapmak İçin Kullanılır.
# Jump Search Arama Yaparken Belirtilen Step Doğrultusunda Atlayarak Arama Yapar
# Jump Search Big-O Linear Search O(n) ve Binary Search O(Log n) Arasındadır.

import math


def JumpSearch(Array, Value):
    n = len(Array)
    step = math.sqrt(n)
    prev = 0

    while Array[int(min(step, n) - 1)] < Value:
        prev = step
        step += math.sqrt(n)

        if prev >= n:
            return - 1

    while Array[int(prev)] < Value:
        prev += 1

        if prev == min(step, n):
            return - 1

        if Array[int(prev)] == Value:
            return int(prev)

    return -1


# JumpSearch([0,1,2,3,4,5,6,7,8,9,10],8)


# Hashing Algorithm
# O(1) Olan Bir Data Structer Elde Edebiliriz.
# Hash Table Değerlerinin Daha Sonra Kolay Bulunabilmesini Sağlayan Data Structer Yapısıdır.
# Hash Table Üzerindeki Her Bir Pozisyon Slots Olarak Adlandırılır. ( Boş Bir Liste Olarak Düşünülebilir)

# Hash Function : Slotlar ve Bu Slotlarda Ki İtemler Arasında Bağlantı(Mapping) Kurmaya Yarayan Fonksiyondur.
# Hash Fonksiyonu İtem Değerini Alır ve Bu İtem'in Hangi Slotta Olduğunu Return Eder
# Hash Function Remainder Method : İtem'i Hangi Slot'a Koyacağımızı Remeinder Yöntemi İle Bulmak.
# Collusion : Birden Fazla Linked Listing Bir Slot'a Bağlanması.
# Searching O(n) = n : Belli Bir Slotta Linked List Eleman Sayısı.


class HashTable(object):

    def __init__(self, Array, Value=None):

        """

        1 -) "Creating Hash Table"
        2 -) For Loop in Array Parameters
        3 -) Adding value of HashTable.
        4 -) __init__ Method Call in Class Method

        """

        self.SearchKey = Value
        self.HashTable = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: []
        }

        for i in Array:
            self.HashTable[i % 8] += [i]

    def __str__(self):
        print(self.HashTable, "\n")

    def SearchBinaryAlgorithm(self):
        
                
        """
        HashIndex = int(self.SearchKey) % 8
        
        # Base Case
        if len(self.HashTable[HashIndex]) == 0:
            return False
    
        # Recursive Case
        else:
            middleIndex = int(len(self.HashTable[HashIndex]) / 2)
        
            if self.HashTable[HashIndex][middleIndex] == self.SearchKey:
                return True
        
            else:
            
                # Lower
                if self.SearchKey < self.HashTable[HashIndex][middleIndex]:
                    return self.SearchBinaryAlgorithm(self.HashTable[HashIndex][:middleIndex], self.SearchKey)
            
                # Upper
                else:
                    return self.SearchBinaryAlgorithm(self.HashTable[HashIndex][middleIndex + 1:], self.SearchKey)
        """
        
        
        HashIndex = int(self.SearchKey) % 8

        first_index = 0
        last_index = len(self.HashTable[HashIndex]) - 1
        found = False

        while first_index <= last_index and not found:

            middle_index = int((first_index + last_index) / 2)

            if self.HashTable[HashIndex][middle_index] == self.SearchKey:
                found = True

            else:
                # Lower Half
                if self.SearchKey < self.HashTable[HashIndex][middle_index]:
                    last_index = middle_index - 1
                    print("Lower Half")

                # Upper Half
                else:
                    first_index = middle_index + 1
                    print("Upper Half")

        return (found, self.SearchKey)


Hashtable = HashTable([i for i in range(0, 10000)], 9096)
Hashtable.__str__()
Hashtable.SearchBinaryAlgorithm()
