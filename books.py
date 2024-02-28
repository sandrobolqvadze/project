import json
from datetime import datetime

class Book: # Book კლასის შექმნა
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year
    

    def to_dict(self):       # # # გვჭირდება json ფაილში ინფორმაციის ჩაწერის დროს 
        return {"title": self._title, "author": self._author, "year": self._year}


    @classmethod    # # # გვჭირდება json ფაილიდან ინფორმაციის წასაკითხად 
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["year"])


    def get_title(self):
        return self._title


    def get_author(self):
        return self._author


    def get_year(self):
        return self._year


class BookManager: # BookManager კლასის შექმნა 
    def __init__(self):
        self._books = []  

    # წიგნის სახელის შეყვანა-შემოწმება
    def input_title(self):
        while True: #ციკლი ამოწმებს რომ დასახელება არ იყოს ცარიელი
            title = input("შეიყვანეთ წიგნის სათაური: ")
            if title.strip():  # დასახელების შემოწმება რომ ცარიელი არ იყოს
                return title
            else:
                print("სათაური არ შეიება იყოს ცარიელი, გთხოვთ შეიყვანოთ დასახელება: ")
    
    # წიგნის ავტორის შეყვანის შემოწმება
    def input_author(self):
        while True: #ციკლი ამოწმებს რომ მნიშვნელობა არ იყოს ცარიელი, ასევე მიიღოს მხოლოდ წერტილი, გამოტოვება და ასოები
            author = input("შეიყვანეთ წიგნის ავტორი: ")
            if not author.strip():
                print("ავტორის სახელი არ შეილება იყოს ცარიელი!")
            elif not all(char.isalpha() or char.isspace() or char == '.' for char in author):  # # ამოწმებს რომ იყოს მხოლოდ ასოები, გამოტოვება და წერტილი
                print("გთხოვთ შეიყვანოთ მხოლოდ დასაშვები სიმბოლოები: ")
            else:
                return author

    # ამოწმებს წიგნის გამოცემის წლის მნიშვნელობას, იღებს მხოლოდ რიცხვს
    def input_year(self):
        while True:
            year = input("მიუთითეთ წიგნის გამოშვების წელი: ")
            try:
                year = int(year)

                if not 1900 <= year <= datetime.now().year:
                    print("მიუთითეთ სწორი წელი(1900დან 2024მდე).")
                else:
                    return year
            except ValueError:
                print("არასწორი ფორმატი! შეიყვანეთ სწორი ფორმატი")



    # ახალი წიგნის დამატება
    def append_book(self):
        title = self.input_title()
        author = self.input_author()
        year = self.input_year()


        new_book = Book(title, author, year)
        self._books.append(new_book)  # # ამატებს ცარიელ სიაში
        print(f'წიგნი "{title}" დაემატა წარმატებით')
        self.save_books_to_file() #ინახავს წიგნს ფაილში

    # წიგნის სათაურით ძებნა 
    def search_book_by_title(self, title):
        searched_books = [book for book in self._books if book.get_title().lower() == title.lower()]  # # # სათითაოდ გადაივლის და შეამოწმებს ქვედა რეგისტრში
        #თუ სათაური ვერ მოიძებნა
        if not searched_books:
            print(f'წიგნის სათური "{title}" ვერ მოიზებნა')
        else:
            # წარმატებული პოვნის შემთხვევაში გამოიტანს შესაბამის შეტყობინებას
            print(f'ნაპოვნია წიგნი დასახელებით: "{title}": ')
            for book in searched_books:
                print(f"ავტორი: {book.get_author()}, გამოშვების წელი: {book.get_year()}")



    #სრული სიის ბეჭვდა
    def book_full_list(self):
        if not self._books:
            print("წიგნების სია ცარიელია") # თუ სია ცარიელია
        else:
            # სრული სიის დაბეჭვდა ცხრილის სახით
            #ბეჭდავს სათაურს
            print("წიგნების სია:")
            for book in self._books:
                print(f"სათაური: {book.get_title()}, ავტორი: {book.get_author()}, გამოშვების წელი: {book.get_year()}")


    #მონაცემების ჩაწერა ფაილში და შენახვა
    def save_books_to_file(self):
            with open("books.json", mode="w", encoding="utf-8") as file:
                book_data = [book.to_dict() for book in self._books]
                json.dump(book_data, file, indent=2)
       

    # ჩატვირთვა შენახული ფაილიდან
    def load_books_from_file(self):
        
        try:
            with open("books.json", mode="r", encoding="utf-8") as file:
                book_data = json.load(file)
                self._books = [Book.from_dict(data) for data in book_data]

        except FileNotFoundError as ex:
            #თუ ვერ ნახავს შენახულ ფაილს გააგრძელებს მუშაობას
            print(f"მსგავსი ფაილი ვერ მოიზებნა: {ex}")


def main():
    book_manager = BookManager()
    book_manager.load_books_from_file() # ფაილის არსებობის შემთხვევაში ჩაიტვირთება პროგრამაში

    while True: #ენიუს გამოტანა კონსოლში
        print("\nმართვის მენიუ:")
        print("1. ახალი წიგნის დამატება")
        print("2. წიგნების სია")
        print("3. სათაურით წიგნის მოზებნა")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ ოპერაცია (1-4): ")

        if choice == '1': # ახალი წიგნის დამატება
            book_manager.append_book()

        elif choice == '2':  # სრული სიის გამოტანა
            book_manager.book_full_list()
        
        elif choice == '3': #ძებნის შედეგის გამოტანა
            title = input("შეიყვანეთ საზიებო წიგნის სახელი: ")
            book_manager.search_book_by_title(title)
        
        elif choice == '4':
            book_manager.save_books_to_file() #ფაილში შენახვა პროგრამის გათიშვამდე
            print("პროგრამიდან გამოსვლა. ნახვამდის!")
            break

        else:
            # არასწორი არჩევანის შემთხვევაში გამოიტანოს შეტყობინება
            print("არასწორი ბრნება, აირჩიეთ 1-დან 4-მდე.")



main()
