class Star_Cinema:
    __hall_list = []  

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)  

    @classmethod
    def view_halls(cls):
        return cls.__hall_list  # সব হলের লিস্ট দেখানো


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()  # প্যারেন্ট ক্লাস থেকে অ্যাট্রিবিউট ইনিশিয়ালাইজ করা
        self.__seats = {}  # প্রাইভেট ডিকশনারি: সিট সংরক্ষণের জন্য
        self.__show_list = []  # প্রাইভেট লিস্ট: শো-এর তথ্য সংরক্ষণ
        self.__rows = rows  # হলের রো সংখ্যা
        self.__cols = cols  # হলের কলাম সংখ্যা
        self.__hall_no = hall_no  # ইউনিক হল নাম্বার

        # Star_Cinema-এর hall_list-এ বর্তমান হল অবজেক্ট যোগ করা
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)  # শো-এর তথ্য একটি টুপলে সংরক্ষণ
        self.__show_list.append(show_info)

        # সিট তৈরি করা (২ডি লিস্ট)
        seat_layout = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seat_layout  
    def book_seats(self,user_mv_id:str,seat_number:int):
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
    
    


       
    def view_show_list(self):
        for id,moive,time in self.__show_list:
            print(f"Todays starting Movies are -> Movie_name : {moive}, Movie_id : {id}, Time : {time}")
    
    def view_avaiable_seats(self,Mv_id:str):
        if Mv_id not in self.__seats:
            print(f"This Movie id ->{Mv_id} is not valid place try again latter")
            return
        print(f"Avaiable seats for Show Id -> {Mv_id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(" ".join(self.__seats[Mv_id][row]))
        
        







        

        