import random

class Book:

    def __init__(self, description, title, author, page, images, publish):
        self.description = description # опис
        self.title = title #назва книги
        self.author = author # автор
        self.page = page # кількість сторінок
        self.images = images # кількість ілюстрацій
        self.publish = publish # видавництво
        
    def Price(self, title):
        page_b = random.randrange(100)
        images_b = random.randrange(100)
        price = page_b*self.page + images_b*self.images
        return price
 
    def Info(self):
        print("Book description:", self.description)
        print("Book title:", self.title)
        print("Book author:", self.author)
        print("Book page:", self.page)
        print("Book images:", self.images)
        print("Book publish:", self.publish,"\n")

def MeanPriceByAuthor(bookList, author):
    s = 0
    k = 0
    for book in bookList:
        if book.author == author:
            s += book.Price(book.title)            
            k += 1
    if k != 0:
        return s/k
    else:
        return 0
    
def MeanPriceByPublisher(bookList, publish):
    s = 0
    k = 0
    for book in bookList:
        if book.publish == publish:
            s += book.Price(book.title)            
            k += 1
    if k != 0:
        return s/k
    else:
        return 0
    
            

listOfBooks = []  

b1 = Book("роман", "Ідіот","Достоєвський",1,12, "Ranok")
b2 = Book("повість", "Ідіот","Достоєвський",1,1232,"abbb ")
b3 = Book("драма", "Ідіот","Достоєвський",1,1243,"lalala")
b4 = Book("драма", "Злочин і кара","Достоєвський",1,2,"lalala")

listOfBooks.append(b1)
listOfBooks.append(b2)
listOfBooks.append(b3)
 
# call member functions for each object
b1.Info()
b2.Info()
b3.Info()

b1.Price("Ідіот")
b3.Price("Ідіот")

mean1 =  MeanPriceByAuthor(listOfBooks, "Достоєвський")
print("Середня ціна автора = ", mean1)

mean2 =  MeanPriceByPublisher(listOfBooks, "lalala")
print("Середня ціна видавництва = ", mean2)


