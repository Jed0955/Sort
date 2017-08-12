def insert_sort(lst):
	'''插入排序，将list中的元素按从小到大排序
	'''修改
	for i in range(1,len(lst)):
		x = lst[i]
		j = i
		while j > 0 and lst[j-1] > x:
			lst[j] = lst[j-1]
			j -= 1
		lst[j] = x

def insert_sort_binary(lst):
	'''二分插入排序，将list中的元素按从小到大排序
	'''
	for i in range(1,len(lst)):
		x = lst[i]
		left = 0
		right = i - 1
		#以下while循环不成立时
		#1、此种情况必定是由left与right位于同一位置时进行比较
		#（1.1）左移了right(x小于移动right之前的mid位置的元素)
		#（1.2）或右移了left（x大于移动left之前的mid位置元素）
		#2、left与right重合，必然有（1）left和right开始就重合或（2）右left与right前后相邻得到
		#（2.1）为进行序列为1的元素的插入排序情况,此时i=1,left=right=1
		#（2.1.1）对于1.1/1.2的情况，x应该放于left处
		#（2.2）从相邻到重合
		#（2.2.1）x大于等于此时的left位置的元素
		#（2.2.1.1）1.1情况，x应放于left处
		#（2.2.1.2）1.2情况
		#（2.2.2）或小于此时right处的元素
		while left <= right:
			mid = int((right + left) / 2)
			if lst[mid] > x:
				right = mid - 1
			else:
				left = mid + 1
		j = i
		while j > left:
			lst[j] = lst[j-1]
			j -= 1
		lst[left] = x

def select_sort(lst):
	'''选择排序，将list中的元素按从小到大排序
	'''
	for i in range(len(lst)-1):
		k = i
		for j in range(i+1,len(lst)):
			if lst[k] > lst[j]:
				k = j
		if k != i:
			lst[i],lst[k] = lst[k],lst[i]

def bubble_sort(lst):
	'''冒泡排序，将list中的元素按从小到大排序
	'''
	for i in range(len(lst)-1):
		for j in range(len(lst)-1-i):
			found = False
			if lst[j] > lst[j+1]:
				lst[j],lst[j+1] = lst[j+1],lst[j]
				found = True
			if not found:
				break

def corss_bubble_sort(lst):
	'''交错起泡，将list中的元素按从小到大排序
	'''
	pass

def quick_sort(lst):
	'''快速排序主函数，将list中的元素按从小到大排序
	'''
	def qsort_rec(lst,l,r):
		'''快速排序递归函数
		'''
		if l >= r:return#分段中无记录或只有一个记录
		i = l
		j = r
		pivot = lst[i]
		while i<j:
			while i<j and lst[j] >= pivot:
				j -= 1
			if i<j:
				lst[i] = lst[j]
				i += 1
			while  i<j and lst[i] <= pivot:
				i += 1
			if i<j:
				lst[j] = lst[i]
				j -= 1
		lst[i] = pivot
		qsort_rec(lst,l,i-1)
		qsort_rec(lst,i+1,r)

	qsort_rec(lst,0,len(lst)-1)

def quick_sort1(lst):
	'''快速排序实现1
	'''
	def qsort_rec(lst,start,end):
		if start >= end:return
		i = start
		j = start + 1
		pivot = lst[start]
		while i <= end and j <= end:
			pass


def radix_sort(lst,d):
	'''基数排序
	'''
	rlists = [[] for i in range(10)]
	llen = len(lst)
	for m in range(-1,-d-1,-1):#一定要是从低位到高位进行
		for j in range(llen):
			index = int(lst[j][m])
			rlists[index].append(lst[j])
		j = 0
		for i in range(10):
			tmp = rlists[i]
			for k in range(len(tmp)):
				lst[j] = tmp[k]
				print(j,lst[j])
				j += 1
			rlists[i].clear()



	