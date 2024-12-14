#""" answer to the question: 1"""
class Star_Cinema:
    __hall_list = [] #private attribute, respective to ans no: 8
    def __init__(self) -> None:
        pass
    
    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    # def entry_hall(self, hall):
    #     self.hall_list.append(hall)



#""" answer to the question no: 2 """ 
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__rows = rows #private attribute, respective to ans no: 8
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

        Star_Cinema.entry_hall(self)

        #Star_Cinema.entry_hall(self, self)

        
#"""answer to the question no: 3"""
    def entry_show(self, id, movie_name, time):
        showInfo = (id, movie_name, time) #tupple
        self.__show_list.append(showInfo)

        seatArrangement = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append('free')
            seatArrangement.append(row)
        
        self.__seats[id] = seatArrangement


#"""answer to the question no: 4"""
    def book_seats(self, id, seatPos):
        if id not in self.__seats:
            print(f"Error: show ID '{id}' does not exist")
        seatArrangement = self.__seats[id]

        for row, col in seatPos:
            if row<0 or row>=self.__rows or col<0 or col>=self.__cols:
                print(f"Invalid seat position: ({row}, {col})")
                continue

            if seatArrangement[row][col] == 'B':
                print(f"Seat ({row}, {col}) is already booked")
            
            seatArrangement[row][col] = 'B'

        self.__seats[id]=seatArrangement
        

#"""answer to the question no: 5"""
    def view_show_list(self):
        if not self.__show_list:
            print("No shows on run!")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie:{show[1]}, Time: {show[2]}")


#"""answer to the question no: 6"""
    def view_available_seats(self, id):
        #check show id exist or not:
        if id not in self.__seats:
            print(f"Error: Show ID {id} does not exist.")

        seatArrangement = self.__seats[id]

        print("Available seats: ")
        for row in seatArrangement:
            print(" ".join(row))


#"""answer to the question no: 7"""
"""replica system"""
class CounterSystem:
    @staticmethod
    def run(hall):
        while True:
            print("\n1. View Show List\n2. View Available Seats\n3. Book Seats\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                hall.view_show_list()
            elif choice == "2":
                id=input("Enter show id: ")
                hall.view_available_seats(id)
            elif choice == "3":
                id=input("Enter show id: ")
                numSeats = int(input("Enter number of seats to book: "))
                seatList =[]
                for _ in range(numSeats):
                    row, col = map(int, input("Enter row & column: ").split())
                    seatList.append((row,col))
                hall.book_seats(id, seatList)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try Again!")

#Answer to Question 8: Error handling is included in `book_seats` and `view_available_seats` methods
#Answer to Question 9: Attributes are private and accessed via methods







# Simulation
hall1 = Hall(5, 5, "H1") #an instance of Hall
hall1.entry_show("S1", "Movie A", "18:00")
hall1.entry_show("S2", "Movie B", "21:00")


CounterSystem.run(hall1) #the counter system




        