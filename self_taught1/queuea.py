import time
import random
#a queue is a data structure and is FIFO
#ex line of people first person gets ticket

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time): #2 integers as params time to start and longest time to purchase
        pq = Queue() #simulates line
        tix_sold = []

        for i in range(100):
            pq.enqueue("person" + str(i)) #add person to pq

        t_end = time.time() + till_show #time returns float of #of seconds since epoch and adds current time to movies
        now = time.time() #holds current time integer
        print(now)
        while now < t_end and not pq.is_empty(): #continues until now > t-end or queue is empty
            now = time.time()
            r = random.randint(0, max_time) #randome number to buy tickets
            time.sleep(r) #stops for certain amount of time pass in random number
            person = pq.dequeue() #remove person
            print(person)
            tix_sold.append(person) #add them to tix sold

        return tix_sold

queue = Queue()
sold = queue.simulate_line(20,2)
print(sold)