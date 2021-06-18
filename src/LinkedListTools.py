from datastructures import ListNode
from listTools import linkedToList
from listTools import sortedArrayToBST

def listToLinked(new_linked):
	linked = ListNode(-1,None)
	linked2 = linked
	linked.next = linked2
	for i in range(len(new_linked)):
		temp = ListNode(new_linked[i],None)
		linked2.next = temp
		linked2 = linked2.next
	return linked.next


def linkedLength(new_linked):
	returnval = 0
	while(new_linked):
		returnval+=1
		new_linked=new_linked.next
	return returnval


def removeElement(new_linked,indices):
	if(linkedLength(new_linked) < indices):
		return "Linked List too small"
	new_ll = ListNode(-1,None)
	new_ll2 = new_ll
	new_ll.next = new_ll2
	array = []
	counter = 0
	while(new_linked):
		counter+=1
		if(counter != indices):
			array.append(new_linked.val)
		new_linked=new_linked.next
	for k in range(len(array)):
		temp = ListNode(array[k],None)
		new_ll2.next = temp
		new_ll2 = new_ll2.next
	return new_ll.next

def getElement(head,index):
	counter = 0
	while(head):
		counter+=1
		if(counter==index):
			return head.val
		head=head.next
	return "Position at index N not found"

def addElement(head, index, val):
	list1 = []
	new_ll = ListNode(-1,None)
	new_ll2 = new_ll
	new_ll.next = new_ll2
	while(head):
		list1.append(head.val)
		head=head.next
	if(len(list1)-1<index):
		list1.append(val)
	else:
		list1.insert(index-1,val)
	for i in range(len(list1)):
		temp = ListNode(list1[i],None)
		new_ll2.next = temp
		new_ll2=new_ll2.next
	return new_ll.next

def printLinkedList(linked_list):
	while(linked_list):
		print(linked_list.val)
		linked_list=linked_list.next

def basicToLinkedList(basic):
	if(str(basic).isnumeric()):
		n = True
	else:
		n = False

	basic_list = list(str(basic))
	if(n==True):
		for k in range(len(basic_list)):
			basic_list[k] = int(basic_list[k])
	return listToLinked(basic_list)

def sortLinked(head,rev):
	return listToLinked(sorted(linkedToList(head),reverse=rev))

def sumLinked(head):
	return sum(linkedToList(head))

def operatorAll(head,operation_list):
	#operation_list: [['*','3'],['+','8'],['-','10']]
	new_list = linkedToList(head)
	if(len(operation_list)!=len(new_list)):
		return "Invalid Call! Errorcode: 1"
	for i in range(len(new_list)):
		try:
			first_val = operation_list[i][1]
			second_val = operation_list[i][0]
			if(first_val == '+'):
				new_list[i] += second_val
			elif(first_val == '-'):
				new_list[i] -= second_val
			elif(first_val == '*'):
				new_list[i] *= second_val
			elif(first_val == '/'):
				try:
					new_list[i] = new_list[i] / second_val
				except ZeroDivisionError:
					print("Can not divide by zero! Skipping this operation! Errorcode:2. Current Index:", i+1)
			else:
				print("Unknown Operation! Skipping this Operation! Errorcode: 3. Current Index:", i+1)
		except IndexError:
			return "Invalid 'operation_list' array! Errorcode: 4"
	return listToLinked(new_list)

def linkedToBST(new_list):
	return sortedArrayToBST(linkedToList(new_list))