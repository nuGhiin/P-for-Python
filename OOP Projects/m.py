#""" answer to the question: 1"""
class Star_Cinema:
    hall_list = []
    def __init__(self) -> None:
        pass
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)

#""" answer to the question no: 2 """ 
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

        Star_Cinema.entry_hall(self, self)

        
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











hall1 = Hall(10, 15, 'Hall-1')   
hall2 = Hall(12, 20, 'Hall-2') 
print(Star_Cinema.hall_list)



        