from datastructures import ListNode
from itertools import permutations
from datastructures import TreeNode
import random

def createEmptyMatrix(row,column,val):
	final = []
	for k in range(row):
		temp = []
		for l in range(column):
			temp.append(val)
		final.append(temp)
	return final

def removeDuplicates(cur_list):
	seen = []
	for i in range(len(cur_list)):
		if(cur_list[i] not in seen):
			seen.append(cur_list[i])
	return seen

def getDuplicates(cur_list):
	seen = []
	dupes = []
	for i in range(len(cur_list)):
		if(cur_list[i] in seen and cur_list[i] not in dupes):
			dupes.append(cur_list[i])
		elif(cur_list[i] not in seen):
			seen.append(cur_list[i])
	return dupes

def linkedToList(head):
	final = []
	while(head):
		final.append(head.val)
		head=head.next
	return final

def findCombinations(cur_list,combination_size):
	if(combination_size>len(cur_list)):
		return "List too small!"
	new = list(permutations(cur_list,combination_size))
	return new

def productOfList(cur_list):
	if(not cur_list):
		return 0
	elif(len(cur_list)<2):
		return cur_list[0]
	num = cur_list[0]
	for i in range(1,len(cur_list)):
		num *= cur_list[i]
	return num

def generateRandomListRange(length, min, max):
	return [random.randint(min,max) for i in range(length)]

def preorder(root,list_write):
	if(not root):
		return
	list_write.append(root.val)
	preorder(root.left,list_write)
	preorder(root.right,list_write)

def postorder(root,list_write):
	if(not root):
		return
	postorder(root.left,list_write)
	postorder(root.right,list_write)
	list_write.append(root.val)
def inorder(root,list_write):
	if(not root):
		return
	inorder(root.left,list_write)
	list_write.append(root.val)
	inorder(root.right,list_write)
def sortedArrayToBST(arr): 
    arr.sort()
    if not arr: 
        return None
    mid = (len(arr)) // 2
    root = TreeNode(arr[mid],None,None) 
    root.left = sortedArrayToBST(arr[:mid])  
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 

	#operation_list: [['*','3'],['+','8'],['-','10']]

def listOperatorAll(new_list,operation_list):
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
	return new_list


def createRandomMatrix(row,column,min,max):
	final = []
	for i in range(row):
		final.append(generateRandomListRange(column,min,max))
	return final

def intlisttoint(intlist):
	try:
		for k in range(len(intlist)):
			intlist[k] = str(intlist[k])
		return int("".join(intlist))
	except TypeError:
		print("Invalid Call!")
		return

def twoDArrayToList(arr):
	final = []
	for k in range(len(arr)):
		for i in range(len(arr[k])):
			final.append(arr[k][i])
	return final