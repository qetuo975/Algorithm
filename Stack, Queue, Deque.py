# Uçağın Sadece Ön Kapısından Yolcu Alıp İndirdiğini Düşünüyoruz.
# İlk Giren Son Çıkar Mantığı
# Son Giren İlk Çıkar Mantığı


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# stackObject = Stack()
# stackObject.push("Ankara")
# stackObject.push("İstanbul")
# stackObject.top()


# Listeye Önden Ekleriz Çıkartırkende En Sonuncu Karakteri Çıkarırız.
# İlk Giren İlk Çıkar Mantığı
# Enqueue İtem Eklemek, Dequeue İtem Çıkarmak
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def returns(self):
        return self.items


queueObject = Queue()


# queueObject.enqueue("Ankara")
# queueObject.enqueue("İstanbul")
# queueObject.returns()
# queueObject.size()
# queueObject.dequeue()


# Deuqe = Stack x Queue Birleşimidir
# Önden veya Arkadan Veri Ekleme ve Silme İşlemleri Gerçekleştirilir.
class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
