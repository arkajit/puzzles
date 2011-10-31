-- file: ch03/BookStore.hs
data BookInfo = Book Int String [String]
								deriving (Show)

data MagazineInfo = Magazine Int String [String]
										deriving (Show)

myInfo = Book 9780135072455 "Algebra of Programming"
				 ["Richard Bird", "Oege de Moor"]

-- Use the wildcard _ to represent parts of the pattern we don't want
bookID			(Book id _ _) = id
bookTitle		(Book _ title _) = title
bookAuthors	(Book _ _ authors) = authors

type CustomerID = Int
type ReviewBody = String
data BookReview = BookReview BookInfo CustomerID ReviewBody

type BookRecord = (BookInfo, BookReview)

type CardHolder = String
type CardNumber = String
type Address = [String]

data BillingInfo = CreditCard CardNumber CardHolder Address
								 | CashOnDelivery
								 | Invoice CustomerID
									 deriving (Show)

data Customer = Customer {
			customerID			:: CustomerID,
			customerName		:: String,
			customerAddress	:: Address
		} deriving (Show)

-- Two ways to create a customer
-- with function application
customer1 = Customer 123 "J.R. hacker" ["a", "Milpitas, CA", "USA"]

-- or using record syntax
customer2 = Customer {
							customerID = 271828,
							customerAddress = ["1048576 Disk Drive",
																 "Milpitas, CA 95134",
																 "USA"],
							customerName = "Jane Q. Citizen"
						}


