#""" answer to the question: 1"""
class Star_Cinema:
    hall_list = []
    def __init__(self) -> None:
        pass
    
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

    # def entry_hall(self, hall):
    #     self.hall_list.append(hall)



#""" answer to the question no: 2 """ 
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

        Star_Cinema.entry_hall(self)

        #Star_Cinema.entry_hall(self, self)

        
#"""answer to the question no: 3"""
    def entry_show(self, id, movie_name, time):
        showInfo = (id, movie_name, time) #tupple
        self.show_list.append(showInfo)

        seatArrangement = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append('free')
            seatArrangement.append(row)
        
        self.seats[id] = seatArrangement


#"""answer to the question no: 4"""
    def book_seats(self, id, seatPos):
        if id not in self.seats:
            print(f"Error: show ID '{id}' does not exist")
            return
        seatArrangement = self.seats[id]

        for row, col in seatPos:
            if row<0 or row>=self.rows or col<0 or col>=self.cols:
                print(f"Invalid seat position: ({row}, {col})")
                continue

            if seatArrangement[row][col] == 'B':
                print(f"Seat ({row}, {col}) is already booked")
            
            seatArrangement[row][col] = 'B'

        self.seats[id]=seatArrangement
        

#"""answer to the question no: 5"""
    def view_show_list(self):
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie:{show[1]}, Time: {show[2]}")











hall1 = Hall(10, 15, 'Hall-1')   
hall2 = Hall(12, 20, 'Hall-2') 
print(Star_Cinema.hall_list)



        