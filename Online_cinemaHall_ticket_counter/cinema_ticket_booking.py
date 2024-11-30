# WHEN A USER HALL CREATE THEN PROPER INTITIAL TIME SET 

from datetime import datetime,timedelta


    
    

class Star_Cinema:
    __hall_list = [] 
    __view_hall_show_list=[]
    
 
   

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)  
    #user check hall in whose moive are avaiable today 
    @classmethod
    def _add_hall_show_list(cls,details):
        cls.__view_hall_show_list.append(details)
    @classmethod
    def view_halls(cls):
        return cls.__view_hall_show_list
    
    #check duplicated same Hall are hall No exited My Optional use
    __hall_no_store=[]
    
    @classmethod
    def _hall_no_valueSet(cls,value):
        cls.__hall_no_store.append(value)

    @classmethod
    def get_hall_no_store(cls):
        return cls.__hall_no_store

    
    #check Movie id are add
    __movie_id_store=[]
    @classmethod
    def _movie_id_add(cls,Movie_id_admin):
        cls.__movie_id_store.append(Movie_id_admin)
    @classmethod
    def _get_movie_id_store(cls):
        return cls.__movie_id_store

    
    # Hall No seat layout Store for user:

    __movie_id_seat_store={}
    @classmethod
    def _movie_id_seat_add(cls,Move_id_no,row,col):
        user_seat_layout =[[0 for _ in range(col)] for _ in range(row)]
        cls.__movie_id_seat_store[Move_id_no]=user_seat_layout

    @classmethod
    def _user_seat_booking(cls,user_mv_id_sent,seat_numbers):

        if user_mv_id_sent not in cls.__movie_id_seat_store:
            print("The Movie Id did not match anyone place check id and try again latter!")
            return

        for row,col in seat_numbers:
            #key = row and value =col
            movie_id_row= len(cls.__movie_id_seat_store[user_mv_id_sent])
            movie_id_col= len(cls.__movie_id_seat_store[user_mv_id_sent][0])
            #working
            if not (0 <=row<movie_id_row and 0<=col<movie_id_col):
                print(f"This ({row},{col}) seat Number is Invalid !")
                continue
            if cls.__movie_id_seat_store[user_mv_id_sent][row][col]==1:
                print(f"Movie id ->{user_mv_id_sent} are {row}{col} is Booked place choice another seat NUmber")
            else:
                cls.__movie_id_seat_store[user_mv_id_sent][row][col]=1
                print(f"Movie id->{user_mv_id_sent} are ({row},{col} )is Booked Successfully")
    

    @classmethod
    def _get_seat_list(cls,user_mv_id):

        cnt=0
        for row in range(len(cls.__movie_id_seat_store[user_mv_id])):
            print()
            for col in range(len(cls.__movie_id_seat_store[user_mv_id][0])):
                if(cls.__movie_id_seat_store[user_mv_id][row][col]==0):
                    cnt+=1
                print(cls.__movie_id_seat_store[user_mv_id][row][col],end=" ")
        if(cnt==0):
            print(f"Sorry Sir ! There are not avaiable seat in this show id : {Mv_id}")
        else:
            print(f"In this move id : {user_mv_id} are {cnt} seat is empty")


        


    #Extra function write such that hall_name show
    # __add_hall_name=[] 
    #--------------------------------------------

    
    #Extra function write such that hall_name show
    #hall info append this list
    # @classmethod
    # def add_view_hall_info(cls,hall_name):
    #     cls.__view_hall_list.append(hall_name)


    # #Extra function write such that hall_name show
    # @classmethod   
    # def get_hall_variable_name(cls,*obj):
    #     for obj_name in obj:
    #         names=[name for name,val in globals().items() if val is obj and
    #         isinstance(val,Hall)]
    #         cls.__add_hall_name.append(names)
    # @classmethod
    # def view_hall_name(cls):
    #     return cls.__add_hall_name
        
    #--------------------------------------------
  




#Create Hall class and taken three parameter

class Hall(Star_Cinema):


    def __init__(self, rows:int, cols:int, hall_no:int):
        
        if hall_no in Star_Cinema.get_hall_no_store():
            # raise ValueError(f"Error: Hall No. {hall_no} is already booked.")
            print(f"Error: Hall No. {hall_no} is already booked.")
            self.__valid=False
            
        if  getattr (self,"__valid",False):
            pass
        else:

            Star_Cinema._hall_no_valueSet(hall_no)


        
           
            
        
        # Sir Optional my creativity error handle of duplicate hall No---- 

        super().__init__()  
        self.__seats = {}  
        self.__show_list = [] 
        self.__rows = rows 
        self.__cols = cols 
        self.__hall_no = hall_no 
           
        #added entery hall for passing hall_list
        Star_Cinema.entry_hall(self)


      # This show are entery in hall class init method are added that private __show_list
      
      #-----Only Admin Changes-----
    def entry_show(self, id:str, movie_name:str, time:str):

        # Prevent operations on an invalid instance
        if not getattr(self,"__valid",True):
            print("Error: Cannot add a show to an invalid hall instance.")

        else:           

            show_info = (id, movie_name, time)       
            self.__show_list.append(show_info)

            view_info = f"======> Movie_id->: {id}, Movie_Name: '{movie_name}', Move_start_time: {time} "
            Star_Cinema._add_hall_show_list(view_info)

        # attach hall_no depend add the set of hall class
            seat_layout = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
            self.__seats[id] = seat_layout  
        # added user display movie id list and this add are seat layout
            Star_Cinema._movie_id_add(id)
            Star_Cinema._movie_id_seat_add(id,self.__rows,self.__cols)

            


        #Anyone set book of the depanded mv id of entry_show

    def book_seats(self,user_mv_id:str,seat_number:dict):
        Star_Cinema._user_seat_booking(user_mv_id,seat_number)
        
        
    
  
    
   
    #user check right hall are seat are avaiable
    # @classmethod
    def view_avaiable_seats(self,Mv_id:str):
        if Mv_id not in Star_Cinema._get_movie_id_store():
            print(f"This Movie id ->{Mv_id} is not valid place try again latter")
            return
        print(f"Avaiable seats for Show Id -> {Mv_id}:")
        Star_Cinema._get_seat_list(Mv_id)
       
#-----------------admin data set in hall-------------------------->
kaji_hall=Hall(10,10,250)
kaji_hall.entry_show("250","Robot3.0",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
kaji_hall=Hall(10,10,350)
kaji_hall.entry_show("350","IronMan5.0",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
kaji_hall=Hall(10,10,350)
kaji_hall.entry_show("112","Superman",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

savana_hall=Hall(10,10,450)
savana_hall.entry_show("450","AmmJan",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#----------------------- Close Authority Function ----------------------------------

#-----------------------Admin show Fronted data set---------------------------------

#Append display data
lst=[]
lst.append("(1) Enter View Hall: ")
lst.append("(2) Enter Movie Id & Show Avaiable seat: ")
lst.append("(3) Enter Movie Id & Book seat: ")
lst.append("(4) Exit: ")

def display_fronted_data_leavcurr_idx(idx=None):
    for i in range(len(lst)):
        if(i!=idx):
            print(lst[i])

   

#----------------------- User Given Data Checking ----------------------------------


def Cheking_User_data(x):
    if  x.isalpha():
        print(f"This {x} is alpha Character Place given integer Number !")
        return False
    elif x.isdigit():
        x = int(x)
        if not((x>=1 and x<=4)):
            print(f"Place Sir given This Number (1 to 4) are inclusive")
            return False
        else:
            return True
    else:
        print(f"This {x} is Numeric number Place given integer Number !")
        return False


#-----------User Display Data given------------
current_idx=None
while True:
    display_fronted_data_leavcurr_idx(current_idx)
    
    x = input()
    if( Cheking_User_data(x)):
        x = int(x)
        if(x==1):

            #Enter view hall Display User:(1)
            current_idx=x-1
            print(f"(1)You are present at View Hall Inside !")
            print()
            print(f" Today Movie are Avaibale Hall 📽️: ")
            print(f" ---------------------------------- ")
            for display_hall in Star_Cinema.view_halls():
                print(display_hall)
            print()
        
        elif(x==2):

            #Enter Avaible set list Display User:(2)
            current_idx=x-1
            print(f"(1)You are present at Show Avaiable seat Inside !")
            print()
            print(f"Enter the Movie Id")
            Move_id = input()
            Hall.view_avaiable_seats(None,Move_id)

        elif(x==3):
            #Enter Book set list Display User:(2)
            current_idx=x-1
            while True:
                print(f"(1)You are present at Booking seat Inside !")
                print()
                print("Enter Movie_id")
                user_movie_id = input()
                print("Enter Booking seat Number (separate by (,) comma):")
                seat_id = input()
                seat_id_spilt = seat_id.split(",")
                if (seat_id_spilt[0].isdigit() and seat_id_spilt[1].isdigit()):
                    seat_number_booking={seat_id_spilt[0]: seat_id_spilt[1]}
                    Hall.book_seats(None,user_movie_id,seat_number_booking)
                    break
                else:
                    print(f"your row: {seat_id_spilt[0]} & col: {seat_id_spilt[1]} are Invalid")
                    print("Place sir row are col Number Only Digit Value")
                    continue
        else:
            print("Exiting system. Goodbye!")


            
            

            







      

                        
                        
                        
                        
            
                        







   

