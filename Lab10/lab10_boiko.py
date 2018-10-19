class Book:

    def __init__(self, description, title, author, page, images, price):
        self.description = description # опис
        self.title = title #назва книги
        self.author = author # автор
        self.page = page # кількість сторінок
        self.images = images # кількість ілюстрацій
        self.price = price # ціна
        
 
    def Info(self):
        print("Book description:", self.description)
        print("Book title:", self.title)
        print("Book author:", self.author)
        print("Book page:", self.page)
        print("Book images:", self.images)
        print("Book price:", self.price,"\n")
     
   '''я ПИТАЛСЯ НО НЕ СМОГ ЧОТО ПРИДУМАТИ
    def Prace(self,page_b,images_b,price):
        page_b = random.randrange(100)
        images_b = random.randrange(100)
        price = page_b*page + images_b*images '''

b1 = Book("роман", "Ідіот","Достоєвський",11,12, 1121)
b2 = Book("повість", "Ідіот","Достоєвський",13,1232,121)
b3 = Book("драма", "Ідіот","Достоєвський",115,1243,21212)
 
# call member functions for each object
b1.Info()
b2.Info()
b3.Info()


