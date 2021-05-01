def DumbWays():
    obj = ['=','*']
    string = ['D','U','M','B','W','A','Y','S']
    row = obj*int(len(string)/2)
    for i in range(7):

            if i != 3:
                for i in range(0,len(row)):
                    if i != 7:
                        print(row[i],'', end = '')
                    else:
                        print(row[i])
            else:
                for i in range(0,len(string)):
                    if i != 7:
                        print(string[i],'', end = '')
                    else:
                        print(string[i])       
DumbWays()   
   
