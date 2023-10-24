# Create an empty list to represent the queue
my_queue = []

# Enqueue (add) items to the back of the list
my_queue.append("item1")
my_queue.append("item2")
my_queue.append("item3")

# Dequeue (remove and get) items from the front of the list
if my_queue:
    item1 = my_queue.pop(0)
else:
    item1 = None

if my_queue:
    item2 = my_queue.pop(0)
else:
    item2 = None

if my_queue:
    item3 = my_queue.pop(0)
else:
    item3 = None

# Print the dequeued items
print("Dequeued items:")
print(item1)
print(item2)
print(item3)
