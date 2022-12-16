# Single Linked List

# Her Bir Node: Veri Depolar ayrıca diğer node ulaşmak için Referans Pointer Tutar.
# Head -> Linked list ilk Node
# Tail -> Linked List son Node
# Linked list içerisinde Dolaşmaya 'traversing' Denir.


# 1-) Başına Eleman Eklemek
# - Yeni Node Yarat
# - Node İçerisindeki Veriyi Belirle
# - Nodun Pointerini Önceki Head Olarak Belirle
# - Yaratılan Yeni Node'u Head Olarak Tanımla


# 2-) Sonuna Eleman Eklemek
# - Yeni Node Yarat
# - Next Referansı None Olarak Ayarla
# - Tail'in Next Referans'ını Bu Yeni Node Olarak Ayarla
# - Yeni Eklenen Node'u Tail Olarak Ayarla


# 3-) Baştan Eleman Çıkarmak
# - Çıkartacağımız Node'dan Sonraki Node'u Head Referans Yaparız.


# 4-) Sondan Eleman Çıkarmak
# - Doubly Linked List Alanına Bakınız.


class SingleLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def setNextNode(self, node):
        self.nextnode = node

    def getNextNode(self):
        return self.nextnode

    def getNodeValue(self):
        return self.value


ankara = SingleLinkedList("06")
istanbul = SingleLinkedList("34")
bolu = SingleLinkedList("14")

ankara.setNextNode(bolu)
bolu.setNextNode(istanbul)

print(ankara.getNextNode().getNextNode().getNodeValue())


# Doubly Linked List

# Her Bir Node: kendinden önceki ve sonraki node'un adresini tutar.
# Bir Önceki Node Referansı İçin 'prev keyword' Kullanılır.
# Header -> Listenin Başında Bulunan Sentinel Diye Bilinen Node'dur
# Tailer -> Listenin Başında Bulunan Sentinel Diye Bilinen Node'dur
# Linked list içerisinde Dolaşmaya 'traversing' Denir.


class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

    # Sonraki Node Ayarla
    def setNextNode(self, node):
        self.nextnode = node

    # Önceki Node Ayarla
    def setPrevNode(self, node):
        self.prevnode = node

    # Sonraki Node Döndür
    def getNextNode(self):
        return self.nextnode

    # Önceki Node Döndür
    def getPrevNode(self):
        return self.prevnode

    # Node Değeri Döndür
    def getNodeValue(self):
        return self.value


ankara = DoublyLinkedList("06")
istanbul = DoublyLinkedList("34")
bolu = DoublyLinkedList("14")

ankara.setNextNode(bolu)
bolu.setPrevNode(ankara)

bolu.setNextNode(istanbul)
istanbul.setPrevNode(bolu)

print(bolu.getPrevNode().getNodeValue())
print(ankara.getNextNode().getNodeValue())

print(istanbul.getPrevNode().getPrevNode().getNodeValue())