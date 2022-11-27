date1=list(input('enter the date1:').split('/'))
date2=list(input('enter the date2:').split('/'))
s=[]
b=[]
if int(date1[0])<=31 and int(date2[0])<=31:
    if int(date1[1])<=12 and int(date2[1])<=12:
        if int(date1[2])<int(date2[2]):
            for i in range(int(date1[2]),int(date2[2])+1):
                if i %4==0:
                    if i%100!=0:
                        s.append(i)
                    elif i%100==0:
                        if i%400==0:
                            s.append(i)
                        else:
                            b.append(i)
                else:
                    b.append(i)
            print('leap year:',s)
            print('Non leap year:',b)
        else:
            print('Enter the valid Date')
    else:
       print('Enter the Valid Date')
else:
    print('Enter the valid Date') 
       
                            
                           
