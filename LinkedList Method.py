
class Node(object):

    def __init__(self, Value):
        self.value = Value
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def push(self, new_data):
        # Node Yarat ve İçerisindeki Veriyi Belirle
        # Yeni Node Kendisinden Sonra Gelen Node'u İşaret Ediyor
        # Head Yeni Node'u İşarete Etsin.

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        # Sonuna Node Eklemek
        # Yeni Node Yarat Daha Sonra new_data Verisini Depola
        # Eğer LinkedList Boş İse Yeni Eklenen Node Head Olucak.
        # Linked List'in Head'inden Başla Sonuna Kadar Git.
        # Last.next None. Onun Yerine new_node ekle

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_data
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def deleteNode(self, Key):
        # İstenilen Key'e Göre Node Sil
        # Eğer Tek bir node varsa ve bu node istenilen değere sahipse
        # Node'u Silmek İçin Key Parametresini Ara
        # Node'u Sil

        temp = self.head

        if temp is not None:
            if temp.value == Key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.value == Key:
                break

            prev_node = temp
            temp = temp.next

        prev_node.next = temp.next
        temp = None

    def insertAfter(self, prev_node, new_data):
        # Prev_node Varmı Yokmu Kontrol Edilir.
        # Yeni Node Yarat ve İçerisine Veri Koy.
        # New_node Next'ini Prev_node Next'i Yap.
        # Prev_node Next'i New_node Yap.

        if prev_node is None:
            print("Böyle Bir Node Yok.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printLinkedList(self):
        temp = self.head
        print("Linked List : ")
        while temp:
            print(temp.value)
            temp = temp.next


linked_list = LinkedList()
linked_list.push("Son Eleman")
linked_list.push(15)
linked_list.push(20)
linked_list.push("İlk Eleman")
linked_list.insertAfter(linked_list.head.next, 100)
linked_list.append("Sona Eklenen Eleman")
linked_list.deleteNode(20)
linked_list.deleteNode("Son Eleman")
linked_list.printLinkedList()