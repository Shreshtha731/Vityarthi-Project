import pandas as pd 
import numpy as np 
from datetime import date 
from datetime import datetime 
import time 
 
     
def menu(): 
     
    while True: 
        print("           HOTEL  MANAGEMENT SYSTEM") 
        print("          H O T E L   H Y A T T   R E G E N C Y") 
        print("         ***************************************") 
        print() 
        print("           1- ROOMS") 
        print("           2- CUSTOMERS") 
        print("           3- CHECK-IN/CHECK-OUT") 
        print("           4- VISUALIZATION") 
        print("           5- ANALYTICS/QUERY") 
     
    print("           6- E X I T") 
        ch=int(input("       Enter your choice [1-6] :")) 
        if ch==1: 
            rooms_entry() 
        elif ch==2: 
            customers() 
        elif ch==3: 
            booking() 
        elif ch==4: 
            visualization() 
        elif ch==5: 
            analytics() 
        else:             
            str="THANK YOU VERY MUCH FOR USING HOTEL MANAGEMENT SYSTEM. 
EXITING....." 
            for k in str: 
                print(k,end='') 
                time.sleep(0.1) 
            break 
 
         
#******************************************************************* 
def rooms_entry(): 
    while True: 
        print("           R O O M S   M E N U") 
        print("          **********************") 
        print() 
        print("           1- Add New Rooms") 
        print("           2- Delete old Rooms") 
        print("           3- Edit detail of the Rooms") 
        print("           4- B A C K") 
        ch=int(input("       Enter your choice [1-4] :")) 
        if ch==1: 
            add_rooms() 
        elif ch==2: 
            del_rooms() 
        elif ch==3: 
            edit_rooms() 
        else: 
            print("Going back to Main Menu") 
            break 
 
#******************************************************************* 
def customers(): 
    while True: 
        print("           C U S T O M E R   M E N U") 
        print("          ***************************") 
        print() 
        print("           1- Add Customers") 
        print("           2- Delete Customers") 
        print("           3- Edit detail of the Customer") 
        print("           4- B A C K") 
        ch=int(input("       Enter your choice [1-4] :")) 
        if ch==1: 
            add_customer() 
        elif ch==2: 
            del_customer() 
        elif ch==3: 
            edit_customer() 
        else: 
            print("Going back to Main Menu") 
            break 
 
 
#******************************************************************* 
def booking(): 
    dftrans=pd.read_csv("transaction.csv") 
    print(dftrans) 
    while True: 
        print("           B O O K I N G    M E N U") 
        print("          ***************************") 
        print() 
        print("           1- Check-in a Room") 
        print("           2- Check-out and Bills") 
        print("           3- B A C K") 
        ch=int(input("       Enter your choice [1-3] :")) 
        if ch==1: 
            book_room() 
        elif ch==2: 
            check_out() 
        else: 
            print("Going back to Main Menu") 
            break 
 
 
#************************************************* 
def add_rooms(): 
    dfrooms=pd.read_csv("rooms.csv") 
    ans='y' 
    rno=0 
    while ans=='y' or ans=='Y': 
        rno=int(input("Enter Room no :")) 
        flno=int(input("Enter Floor no :")) 
        typ=input("Enter Room Type :") 
        chrg=float(input("Enter Charge :")) 
        facil=input("Enter Facilities :") 
        stat=input("Enter Status ( V-Vacant, O-Occupied):") 
        data=[rno,flno,typ,chrg,facil,stat] 
        dfrooms.loc[len(dfrooms)]=data 
        dfrooms.to_csv("rooms.csv",index=False) 
        print("A New Room's data added Successfully....") 
        ans=input("Do you want to add more Rooms?") 
    print(dfrooms) 
         
 
#**************************************** 
def del_rooms(): 
    dfrooms=pd.read_csv("rooms.csv") 
    ans='y' 
    rno=0 
    while ans=='y' or ans=='Y': 
        rno=int(input("Enter Room no :")) 
        if rno in dfrooms['roomno'].values: 
            response=input("Do you really want to remove this Room's 
data(Y/N)?") 
            if response=='y' or response=='Y':  
                
dfrooms.drop(dfrooms[dfrooms['roomno']==rno].index,inplace=True) 
                print("Room No -",rno,"has been deleted 
successfully...") 
        else: 
            print("Room is not found...") 
             
        dfrooms.to_csv("rooms.csv",index=False) 
        ans=input("Do you want to delete more rooms?") 
    print(dfrooms)  
 
 
def edit_rooms(): 
    dfrooms=pd.read_csv("rooms.csv") 
    print(dfrooms) 
    ans='y' 
    rno=0 
    while ans=='y' or ans=='Y': 
        rno=int(input("Enter Room No :")) 
        if rno in dfrooms['roomno'].values: 
            nm=input("Enter the column name to change: ") 
            val1=eval(input("Enter it's value: if string in quotes(''): 
")) 
            dfrooms.loc[(dfrooms['roomno'] == rno),nm]=val1 
            print("Room -",rno,"has been updated successfully...") 
            print(dfrooms.loc[dfrooms['roomno']==rno]) 
             
        else: 
            print("Room number not found...") 
             
        dfrooms.to_csv("rooms.csv",index=False) 
        ans=input("Do you want to edit more room's detail?") 
    print(dfrooms)  
 
 
#************************************************* 
def add_customer(): 
    dfcust=pd.read_csv("customer.csv") 
    ans='y' 
    cid=0 
    while ans=='y' or ans=='Y': 
        df=dfcust.sort_values(by='cust_id') 
        df=df.tail(1) 
        cid=df.iloc[0,0]+1 
        print("New Customer id : ",cid) 
        cst_nam=input("Enter Customer Name :") 
        age=int(input("Enter Age :")) 
        phno=int(input("Enter Contact :")) 
        addr=input("Enter Address :") 
        data=[cid,cst_nam,age,phno,addr] 
        dfcust.loc[len(dfcust)]=data 
        dfcust.to_csv("customer.csv",index=False) 
        print("A New Customer added Successfully....") 
        ans=input("Do you want to add more Customers?") 
    print(dfcust) 
 
 
 
def del_customer(): 
    dfcust=pd.read_csv("customer.csv") 
    ans='y' 
    cid=0 
    while ans=='y' or ans=='Y': 
        cid=int(input("Enter customer id :")) 
        if cid in dfcust['cust_id'].values: 
            print(dfcust.loc[dfcust.cust_id==cid,['cust_name','Age']]) 
            ans=input("Do you want to really delete it(Y/N)") 
            if ans=='y' or ans=='Y':    
                
dfcust.drop(dfcust[dfcust['cust_id']==cid].index,inplace=True) 
                print("Customer id -",cid,"has been deleted 
successfully...") 
        else: 
            print("Customer is not found...") 
             
        dfcust.to_csv("customer.csv",index=False) 
        ans=input("Do you want to delete more customer?") 
    print(dfcust) 
 
 
#********************************************************* 
def edit_customer(): 
    dfcust=pd.read_csv("customer.csv") 
    print(dfcust) 
    ans='y' 
    cid=0 
    while ans=='y' or ans=='Y': 
        cid=int(input("Enter Customer id :")) 
        if cid in dfcust['cust_id'].values: 
            nm=input("Enter the column name to change: ") 
            val1=eval(input("Enter it's value: if string in quotes(''): 
")) 
            dfcust.loc[(dfcust['cust_id'] == cid),nm]=val1 
            print("Customer id -",cid,"has been updated 
successfully...") 
            print(dfcust.loc[dfcust['cust_id']==cid]) 
             
        else: 
            print("Customer is not found...") 
             
        dfcust.to_csv("customer.csv",index=False) 
        ans=input("Do you want to edit more Customers?") 
    print(dfcust) 
 
#********************************************************** 
def book_room(): 
    dfrooms=pd.read_csv("rooms.csv") 
    dfcust=pd.read_csv("customer.csv") 
    dftrans=pd.read_csv("transaction.csv") 
    ans='y' 
    while ans=='y' or ans=='Y': 
        cid=int(input("Enter Customer id: ")) 
        rno=int(input("Enter Room No: ")) 
        if cid in dfcust['cust_id'].values: 
            print(dfcust.loc[dfcust.cust_id==cid,['cust_name','Age']]) 
            if rno in dfrooms['roomno'].values: 
                stat=dfrooms.loc[dfrooms['roomno'] == rno, 
'status'].values[0] 
                if (stat=='V'): 
                    ans=input("Do you want to check-in (y/n)?") 
                    dt_bk=input("Please Enter date of booking/check
in(dd/mm/yyyy): ") 
                    if ans.upper()=='Y': 
                        dt_chkin=dt_bk 
                        
dfrooms.loc[dfrooms['roomno']==rno,'status']='O' 
                        
data=[rno,cid,dt_bk,dt_chkin,np.NaN,np.NaN,np.NaN] 
                        dftrans.loc[len(dftrans)]=data 
                        print("Room booked/checked-in Successfully...")     
                else: 
                    print("Room not Vacant...") 
            else: 
                print("This Room no is not found...") 
        else: 
            print("This Customer does not exists...") 
            
        dftrans.to_csv("transaction.csv",index=False) 
        dfrooms.to_csv("rooms.csv",index=False) 
        dfcust.to_csv("customer.csv",index=False) 
        ans=input("Do you want to do more booking?") 
    print(dftrans) 
 
 
#********************************************************** 
def check_out(): 
    dfrooms=pd.read_csv("rooms.csv") 
    dfcust=pd.read_csv("customer.csv") 
    dftrans=pd.read_csv("transaction.csv") 
    ans='y' 
    while ans=='y' or ans=='Y': 
        cid=int(input("Enter Customer id: ")) 
        rno=int(input("Enter Room number doing check-out:")) 
        cond1=((dftrans.cust_id==cid) & (dftrans.roomno==rno) & 
(dftrans.dt_checkout.isnull())) 
        cond2=((dfrooms.roomno==rno) & (dfrooms.status=='O')) 
        if cond1.any() and cond2.any(): 
            dt_out=input("Please Enter date of check-out(dd/mm/yyyy): 
") 
            dftrans.loc[(dftrans['cust_id'] == cid) & 
(dftrans['roomno'] == rno) & (dftrans['dt_checkout'].isnull()), 
'dt_checkout']=dt_out 
            dfrooms.loc[dfrooms.roomno == rno, 'status']='V' 
            chrg=dfrooms.loc[dfrooms.roomno==rno,'charge'].values[0] 
            dt_in=dftrans.loc[(dftrans['cust_id'] == cid) & 
(dftrans['roomno'] == rno), 'dt_checkin'].values[0] 
 
            # Calculating Fine 
            date_dt1 = datetime.strptime(dt_in, '%d/%m/%Y') 
            date_dt2 = datetime.strptime(dt_out, '%d/%m/%Y') 
            ndays=date_dt2-date_dt1 
 
            n_days=ndays.days 
             
            mbill=n_days*chrg 
            dftrans.loc[(dftrans['cust_id'] == cid) & 
(dftrans['roomno'] == rno), 'days']=n_days 
            dftrans.loc[(dftrans['cust_id'] == cid) & 
(dftrans['roomno'] == rno), 'bill']=mbill 
             
            print("Total Bill Rs.",mbill) 
            print("Check out done Successfully...") 
 
            dftrans.to_csv("transaction.csv",index=False) 
            dfrooms.to_csv("rooms.csv",index=False) 
            dfcust.to_csv("customer.csv",index=False) 
         
        else: 
            print("Room is already Vacant or Billing/check out already 
done") 
 
        ans=input("Do you want to do more Checkout?") 
 
 
 
 
 
   
 
#*********************************************************** 
def analytics(): 
    dfrooms=pd.read_csv("rooms.csv") 
    dfcust=pd.read_csv("customer.csv") 
    dftrans=pd.read_csv("transaction.csv") 
    while True: 
        print("           A N A L Y S I S   M E N U") 
        print("          ***************************") 
        print() 
        print("           1- All Rooms") 
        print("           2- All Customers") 
        print("           3- Search Rooms (Number wise)") 
        print("           4- Search Rooms (Type wise)") 
        print("           5- Search Customer (ID wise)") 
        print("           6- Search Customer (Name wise)") 
        print("           7- Booked Room (Date wise)") 
        print("           8- Back to Main Menu")   
        ch=int(input("       Enter your choice [1-8] :")) 
        if ch==1: 
            print(dfrooms) 
        elif ch==2: 
            print(dfcust) 
        elif ch==3: 
            rno=int(input("Please Enter Room Number: ")) 
            print(dfrooms.loc[dfrooms.roomno==rno]) 
        elif ch==4: 
            rtype=input("Please Enter Room Type: ") 
            print(dfrooms.loc[dfrooms.type==rtype]) 
        elif ch==5: 
            cid=int(input("Please Enter Customer ID: ")) 
            print(dfcust.loc[dfcust.cust_id==cid]) 
        elif ch==6: 
            c_nm=input("Please Enter Customer Namee: ") 
            length=len(dfcust) 
            for i in range(length): 
                if c_nm in dfcust.cust_name[i]: 
                    print(dfcust.cust_id[i],"-
>",dfcust.cust_name[i],"-->",dfcust.Address[i]) 
        elif ch==7: 
            dt_buk=input("Please Enter Date of Booking: ") 
            print(dftrans.loc[dftrans.dt_book==dt_buk]) 
        else: 
            print("Going back to Main Menu") 
            break 