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

            view_info = f"Hall {id}: Movie '{movie_name}' at {time} (Show ID: {id})"
            Star_Cinema._add_hall_show_list(view_info)

        # attach hall_no depend add the set of hall class
            seat_layout = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
            self.__seats[id] = seat_layout  
            


        #Anyone set book of the depanded mv id of entry_show

    def book_seats(self,user_mv_id:str,seat_number:tuple):
        if user_mv_id not in self.__seats:
            print("The Movie Id did not match anyone place check id and try again latter!")
            return
        for row,col in seat_number:
            if not (0 <=row<self.__rows and 0<=col<self.__cols):
                print(f"This ({row},{col}) seat Number is Invalid !")
                continue
            if self.__seats[user_mv_id][row][col]==1:
                print(f"Movie id ->{id} are {row}{col} is Booked place choice another seat NUmber")
            else:
                self.__seats[user_mv_id][row][col]=1
                print(f"Movie id->{user_mv_id} are ({row},{col} )is Booked Successfully")
    
    
  
    
   
    #user check right hall are seat are avaiable
    # @classmethod
    def view_avaiable_seats(self,Mv_id:str):
        if Mv_id not in self.__seats:
            print(f"This Movie id ->{Mv_id} is not valid place try again latter")
            return
        print(f"Avaiable seats for Show Id -> {Mv_id}:")
        cnt=0
        for row in range(self.__rows):
            print()
            for col in range(self.__cols):
                if(self.__seats[Mv_id][row][col]==0):
                    cnt+=1
                print(self.__seats[Mv_id][row][col],end=" ")
        if(cnt==0):
            print(f"Sorry Sir ! There are not avaiable seat in this show id : {Mv_id}")
        else:
            print(f"In this move id : {Mv_id} are {cnt} is empty")

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

def display_fronted_data_leavcurr_idx(idx):
    for i in range(len(lst)):
        if(i!=idx):
            print(lst[i])

   

#----------------------- User Given Data Checking ----------------------------------


def Cheking_User_data(x):
    if  x.isalpha():
        print(f"This {x} is alpha Character Place given integer Number !")
        return False
    elif x.isdigit():
        if not((x>=1 and x<=4)):
            print(f"Place Sir given This Number (1 to 4) are inclusive")
            return False
        else:
            return True
    else:
        print(f"This {x} is Numeric number Place given integer Number !")
        return False
        
    
def user_diplay_comment(x):
    pass


#-----------User Display Data given------------

while True:

    for comment in lst:
        print(comment)
    
    x = input()
    if( Cheking_User_data(x)):
        x = int(x)


        if(x==1):
            #Enter view hall Display User:(1)
            print(f" Today Movie are Avaibale Hall 📽️: ")
            for display_hall in Star_Cinema.view_halls():
                print(display_hall)

            #(1) leave Another Enter display show
            while True:
                display_fronted_data_leavcurr_idx(x)
                x1a=input()
                if(Cheking_User_data(x1a)):
                    x1a =int(x)

                    if(x1a==2):
                        #Enter Total Seat view hall Display User:(1)
                        print("Enter Movie Id: ")
                        Movie_id=input()
                        Hall.view_avaiable_seats(None,Movie_id)
                    # (2)  leave Another Enter display show
                        while True:
                            display_fronted_data_leavcurr_idx(x1a)
                            x1b=input()
                            if(Cheking_User_data(x1b)):
                                x1b=int(input())


                            else:
                                continue



                        
                    elif(x==3):
                        pass
                    else:
                        break


                else:
                    continue

   

        elif(x==2):
            pass

        elif(x==3):
            pass

        else:
            break
    else:
        continue

    
    





        
        







        

        