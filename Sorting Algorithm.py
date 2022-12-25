# Bubble Sort

# Bir Listede Birbirine Ardışık Duran İki Değeri Sıralama Yapar -
# ve Bu Süreci Tüm Liste Sıralı Hale Gelene Kadar Devam Eder.

def BubbleSortAlgorithm(Array):
    for i in range(len(Array) - 1, 0, -1):

        for j in range(i):

            if Array[j] > Array[j + 1]:
                temp = Array[j]
                Array[j] = Array[j + 1]
                Array[j + 1] = temp

    return Array


BubbleSortAlgorithm([42, 213, 25, 256, 3263, 26])


# Merge Sort

# Recursive Algoritmadır.
# Bir Dizi Boyutları 2 Olacak Şekilde Sub Arraylere Bölene Kadar Bölmeye Başlar.
# Daha Sonra En Küçük Sub Array'den Sıralamaya Başlayarak Birleştirir.
# Splits List in A Half.

def MergeSort(arr):
    
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        
        # 1 İndeks Kalana Kadar Parçalamak
        MergeSort(lefthalf)
        MergeSort(righthalf)
        
        
        i = 0
        j = 0
        k = 0
        
        # Küçükten Büyüğe Doğru Sıralamak
        while i < len(lefthalf) and j < len(righthalf):
            
            
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
                
            else:
                arr[k] = righthalf[j]
                j += 1
            
            k += 1
            
        
        # Tekrardan oluşturmak
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
            
            
    return arr
            
        

#MergeSort([4,7,1,23,99,44,223,6236,323])


# Sub List Kullanır.
# İlk Value Bir Sub List Elemanıdır ve Zaten Tek Bir Değere Sahip Olduğu İçin Sıralıdır.
# Bir Sub Listenin İçerisine Kalan Değerler Karşılaştırılarak Eklenir.

def InsertionSort(Array):
    for i in range(1, len(Array)):
        currentValue = Array[i]  # 23
        position = i  # 1

        # sublist
        while position > 0 and Array[position - 1] > currentValue:
            Array[position] = Array[position - 1]
            position -= 1

        Array[position] = currentValue
    return Array


# InsertionSort([1,23,46,2,3,55,621,525])


# Listenin En Küçük Değerini Bulup İndex 0' a Atıyoruz.
# Daha Sonra Bir Sonraki En Küçük Değeri Bularak Arama Devam Ediyor.

def SelectionSort(Array):
    for i in range(len(Array) - 1, 0, -1):
        positionOfMax = 0

        for locasion in range(1, i + 1):
            if Array[locasion] > Array[positionOfMax]:
                positionOfMax = locasion

        temp = Array[i]
        Array[i] = Array[positionOfMax]
        Array[positionOfMax] = temp
    return Array


# SelectionSort([3,52,32,44,721,23])


def CountingSort(Array, MaxVal):
    n = len(Array)
    m = MaxVal + 1
    count = [0] * m

    for i in Array:
        count[i] += 1

    i = 0

    for a in range(m):

        for b in range(count[a]):
            Array[i] = a
            i += 1

    return Array


# CountingSort([2,5,1,3,7,2,9,12,15,16], 16)


# Quick Sort

# Böl ve Fethet Mantığı Kullanılır.
# Pivot Value Listeyi İkiye Böler.
# Pivot Value'dan Küçük Değerler Listenin Sol Kısmını,
# Büyük Değerler İse Sağ Kısmını Oluşturur.
# Recursion Kullanılır.


def Quick_Sort_Recursion(arr, first, last):
    if first < last:
        splitPoint = Partition(arr, first, last)

        # left right
        Quick_Sort_Recursion(arr, first, splitPoint - 1)
        Quick_Sort_Recursion(arr, splitPoint + 1, last)


def Partition(arr, first, last):
    # pivot Value = İlk Eleman
    pivotValue = arr[first]
    left = first + 1
    right = last

    done = False

    while not done:

        while left <= right and arr[left] <= pivotValue:
            left = left + 1

        while arr[right] >= pivotValue and right >= left:
            right = right - 1

        if right < left:
            done = True

        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp

    return right

    # end Point


def QuickSort(arr):
    Quick_Sort_Recursion(arr, 0, len(arr) - 1)
    return arr

# QuickSort([2,3,5,6,1,4,8,2])




