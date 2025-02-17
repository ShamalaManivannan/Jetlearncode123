class Queue():
    def __init__(self,size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size
    
    def enqueue(self,item):
        if self.available == 0:
            print("Queue overflow")
        else:
            self.queue[self.rear] = item    
            self.rear = (self.rear + 1)% self.size
            self.available -= 1
    
    def d_queue(self):
        if self.available == self.size:
            print("Queue underflow")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1)% self.size
            self.available += 1

    def peak(self):
        print(self.queue[self.front])          

    def get_rear(self):
        print(self.queue[self.rear])       

    def print_queue(self):
        print(self.queue)              

q1 = Queue(4)
q1.enqueue(10)
q1.peak()
q1.get_rear()
q1.enqueue(20)
q1.d_queue()
q1.peak()
q1.print_queue