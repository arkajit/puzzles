-- file: ch03/MySecond.hs
mySecond :: [a] -> a  -- explicit type signature

mySecond xs = if null (tail xs)
							then error "list too short"
							else head (tail xs)

safeSecond :: [a] -> Maybe a

safeSecond [] 		= Nothing
safeSecond (x:[]) = Nothing
safeSecond xs			= Just (head (tail xs))

tidySecond (_:x:_) = Just x
tidySecond _ = Nothing
