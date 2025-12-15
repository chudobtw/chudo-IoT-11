class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PrintQueue:
    def __init__(self):
        self.front = None   
        self.rear = None   

    def enqueue(self, document):
        new_node = Node(document)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"\t\t\tДокумент '{document}' додано в чергу.")

    def dequeue(self):
        if self.front is None:
            print("Черга порожня, друкувати нема чого.")
        else:
            document = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(f"\t\t\tДокумент '{document}' надруковано.")

    def display(self):
        if self.front is None:
            print("Черга порожня.")
            return
        current = self.front
        print("\n Документи в черзі:")
        while current:
            print(f"- {current.data}")
            current = current.next

if __name__ == "__main__":
    printer_queue = PrintQueue()
    
    printer_queue.enqueue("Курсова робота")
    printer_queue.enqueue("Звіт з лаби фізика")
    printer_queue.enqueue("Сімейне дерево")

    printer_queue.display()

    printer_queue.dequeue()
    printer_queue.dequeue()
    printer_queue.dequeue()

    printer_queue.dequeue()
