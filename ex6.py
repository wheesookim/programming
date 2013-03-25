def reverse(arr,n):
	for i in range(0,n+1):
		if(arr[i] == arr[n-i]):
			print 'same'
			break;
		else:
			print 'different'
			break;

x = raw_input ("input the string : ")
n=len(x)

reverse(x,n-1)