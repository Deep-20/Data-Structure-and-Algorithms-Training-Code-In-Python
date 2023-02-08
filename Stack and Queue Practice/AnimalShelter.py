class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeueAny(self):
        if not self.queue:
            return "Shelter is empty!!"
        else:
            popped = self.queue.pop(0)
            return popped + " provided from index 0"
    
    def dequeueDog(self):
        if not self.queue:
            return "Shelter is empty!!"
        else:
            for i in range(len(self.queue)):
                if self.queue[i] == "Dog":
                    popped = self.queue.pop(i)

                    return "Dog provided from index " + str(i)
            return "No Dogs Available!!"

    def dequeueCat(self):
        if not self.queue:
            return "Shelter is empty!!"
        else:
            for i in range(len(self.queue)):
                if self.queue[i] == "Cat":
                    popped = self.queue.pop(i)

                    return "Cat provided from index " + str(i)
            return "No Cats Available!!"

    def printQueue(self):
        for value in self.queue:
            print(value, end = " ")


customQueue = Queue()

customQueue.enqueue("Dog")
customQueue.enqueue("Dog")
customQueue.enqueue("Cat")
customQueue.enqueue("Dog")
customQueue.enqueue("Cat")
customQueue.enqueue("Cat")

customQueue.printQueue()
print()

print(customQueue.dequeueAny())
print(customQueue.dequeueCat())
        
