# queue1.py

queue1 = []

def enqueue(value):
    queue1.append(value)

def dequeue():
    if not is_empty():
        return queue1.pop(0)
    else:
        return None

def is_empty():
    return len(queue1) == 0

def display():
    print("Queue:", queue1)