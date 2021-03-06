-- file: ch03/ListADT.hs
data List a = Cons a (List a)
						| Nil
							deriving (Show)

fromList (x:xs) = Cons x (fromList xs)
fromList [] 		= Nil

toList (Cons a b) = a:(toList b)
toList Nil 				= []
