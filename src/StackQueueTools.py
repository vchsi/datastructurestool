from datastructures import Stack
from datastructures import Queue
#stack functions
def ListAsStack(arr):
	if(not arr):
		print("Empty List")
	return_val = Stack(arr,None)
	return_val.top = arr[-1]
	return return_val

def push(val,new_stack):
	new_stack.stackarr.append(val)
	new_stack.top = val
	
def pop(new_stack):
	if(not new_stack.stackarr):
		print("Its already empty")
		return
	top = new_stack.stackarr[-1]
	new_stack.stackarr.pop(-1)
	try:
		new_stack.top = new_stack.stackarr[-1]
	except IndexError:
		new_stack.top = None
	return top
def stackAsList(new_stack):
	return new_stack.stackarr

def stackSize(new_stack):
	return len(stackAsList(new_stack))

def top(new_stack):
	return new_stack.top

def emptyStack(new_stack):
	new_stack.stackarr = []
	new_stack.top = None

def queueAsStack(new_queue):
	return Stack(new_queue.queuearr,new_queue.front)

def isEmptyStack(new_stack):
	if(not new_stack.stackarr):
		return True
	else:
		return False
#queue function

def listAsQueue(new_list,size):
	if(not new_list):
		print("Invalid or empty list")
		return
	return Queue(new_list,new_list[-1],new_list[0],size)
def stackAsQueue(new_stack,size):
	if(not new_stack.stackarr):
		return
	return Queue(new_stack.stackarr,new_stack.top,new_stack.stackarr[0],size)
def queueAsList(new_queue):
	return new_queue.queuearr

def enqueue(item,new_queue):
	if(len(new_queue.queuearr) > new_queue.size):
		print("The queue is too big! Remove one to add one!")
		return
	new_queue.queuearr.insert(0,item)
	new_queue.back = item
	if(new_queue.front == None):
		new_queue.front = item

def dequeue(new_queue):
	if(not new_queue.queuearr):
		print("Its already empty")
		return
	return_val = new_queue.queuearr[-1]
	try:
		new_queue.queuearr.pop(-1)
		new_queue.front = new_queue.queuearr[-1]
	except IndexError:
		new_queue.front = None
	if(not new_queue.queuearr):
		new_queue.back = None
	return return_val

def peek(new_queue):
	return new_queue.front

def lengthOfQueue(new_queue):
	return len(new_queue.queuearr)

def empty(new_queue):
	new_queue.queuearr = []
	new_queue.front = None
	new_queue.back = None

def isEmpty(new_queue):
	if(not new_queue.queuearr):
		return True
	else:
		return False

def moveToBack(new_queue):
	if(not new_queue.queuearr):
		return
	returnval = new_queue.queuearr[-1]
	new_queue.queuearr.pop(-1)
	new_queue.queuearr.insert(0,returnval)
	new_queue.front = new_queue.queuearr[-1]
	new_queue.back = new_queue.queuearr[0]

