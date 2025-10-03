class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self.checked = _is_checked_out

    def book_name(self):
        return f"The book I just took from the library is {self.title}, written by {self.author} "
    
    def check_out(self):
        if self.checked == False:
            # self.checked = True
            return f"{self.title} is available"
        else:
            return f"{self.title} is not available, please check back later"
        
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, tit):
        self._books.append()
        return f"{self.title} has been added"
    
    def check_out_book(self, title):
        if self.checked == True:
            return f"{self.title} has been checked out"
        else:
            return f"{self.title} has not been checked out"
        
     def return_book(self):
        if not che

     def list_available_books(self):

