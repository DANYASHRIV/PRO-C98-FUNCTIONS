def swapfiledata():
    sample1=input("enter the file name")
    sample2=input("enter the file names")
    
    with open (sample1.txt,'r') as a:
        data_a = a.read()
    with open (sample1, 'w')as a:
        a.write (data_b)

    with open (sample2.txt,'r') as a:
        data_b=a.read()
    with open (sample2, 'w')as a:
        a.write (data_a)
swapfiledata()