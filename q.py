class Queue():
    def __init__(self,size):
        self.queue = [None]*size
        self.front = 0  #tracks the front point of the queue
        self.rear = 0  #tracks the next empty position in the queue
        self.size = size  #tracks the size of the queue
        self.available = size #tracks the availability of the queue
    
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
            self.front = (self.front + 1)% self.size  #moving the front point forwars, as you are using a circular motion
            self.available += 1

    def peek(self):  #check the front value
        print(self.queue[self.front])     

    def get_rear(self): #display next empty position of value in the queue
        print(self.queue[self.rear])       

    def print_queue(self):  #display current and entire list
        print(self.queue)              

q1 = Queue(4)
q1.enqueue(10)
q1.peek()
q1.get_rear()
q1.enqueue(20)
q1.peek()
q1.enqueue(30)
q1.enqueue(40)
q1.print_queue()
q1.get_rear()