""" answer to the question: 1"""
class Star_Cinema:
    hall_list = []
    def __init__(self) -> None:
        pass
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)

""" answer to the question no: 2 """ 
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

        Star_Cinema.entry_hall(self, self)
    
hall1 = Hall(10, 15, 'Hall-1')   
hall2 = Hall(12, 20, 'Hall-2') 
print(Star_Cinema.hall_list)


        