# WHEN A USER HALL CREATE THEN PROPER INTITIAL TIME SET 

from datetime import datetime,timedelta
#Extra function write such that hall_name show


    
    

class Star_Cinema:
    __hall_list = [] 
    __view_hall_list=[]
    #Extra function write such that hall_name show
    __add_hall_name=[] 
    #--------------------------------------------
   

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)  

    @classmethod
    def view_halls(cls):
        return cls.__view_hall_list 
    
    #hall info append this list
    @classmethod
    def add_view_hall_info(cls,hall_name):
        cls.__view_hall_list.append(hall_name)


    #Extra function write such that hall_name show
    @classmethod   
    def get_hall_variable_name(cls,*obj):
        for obj_name in obj:
            names=[name for name,val in globals().items() if val is obj and
            isinstance(val,Hall)]
            cls.__add_hall_name.append(names)
    @classmethod
    def view_hall_name(cls):
        return cls.__add_hall_name
        
    #--------------------------------------------
  




#Create Hall class and taken three parameter

class Hall(Star_Cinema):
    def __init__(self, rows:int, cols:int, hall_no:int):
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
        show_info = (id, movie_name, time) 
        self.__show_list.append(show_info)
        view_info = f"Hall {self.__hall_no}: Movie '{movie_name}' at {time} (Show ID: {id})"
        Star_Cinema.add_view_hall_info(view_info)
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
    
    
    #user check hall in whose moive are avaiable today 
    def view_show_list(self):
        for id,moive,time in self.__show_list:
            print(f"Todays starting Movies are -> Movie_name : {moive}, Movie_id : {id}, Time : {time}")
   
    #user check right hall are seat are avaiable
    def view_avaiable_seats(self,Mv_id:str):
        if Mv_id not in self.__seats:
            print(f"This Movie id ->{Mv_id} is not valid place try again latter")
            return
        print(f"Avaiable seats for Show Id -> {Mv_id}:")
        for row in range(self.__rows):
            print()
            for col in range(self.__cols):
                print(self.__seats[Mv_id][row][col],end=" ")

#-----------------admin data set in hall-------------------------->
kaji_hall=Hall(10,10,250)
kaji_hall.entry_show("112","Robot3.0",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

savana_hall=Hall(10,10,250)
savana_hall.entry_show("115","AmmJan",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))




        
        







        

        