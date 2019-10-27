 def selection_sort(list_of_nums):
	for i in range(0, len(list_of_nums)): #0,1,2,3,4
		low_tmp = i
		for j in range(i+1, len(list_of_nums)):
			if list_of_nums[j] < list_of_nums[low_tmp]:
				low_tmp = j
		if list_of_nums[i] != list_of_nums[low_tmp]:
			temp = list_of_nums[i]
			list_of_nums[i] = list_of_nums[low_tmp]
			list_of_nums[low_tmp] = temp