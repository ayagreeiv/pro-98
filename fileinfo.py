
def swapFileData():

    file1 = input("enter original file: ")
    file2 = input("enter the file to be swaped:")

    with open( file1, 'r') as a :
        data_a = a.read()
    
    with open( file1, 'r') as b :
        data_b = b.read()

swapFileData()