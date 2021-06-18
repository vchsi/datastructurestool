class ListNode:
	def __init__(self,val,next):
		self.val = val
		self.next = next

class TreeNode:
	def __init__(self,val,left,right):
		self.val = val
		self.left = left
		self.right = right

class Stack:
	def __init__(self,stackarr,top):
		self.stackarr = stackarr
		self.top = top

class Queue:
	def __init__(self,queuearr,front,back,size):
		self.queuearr = queuearr
		self.front = front
		self.back = back
		self.size = size

class Hashmap:
	def __init__(self,hashmapdict,size):
		self.hashmapdict = hashmapdict
		self.size = size