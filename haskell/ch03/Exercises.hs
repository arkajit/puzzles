-- file: ch03/Exercises.hs

-- 1. length of a list
myLength :: [a] -> Int
myLength []     = 0
myLength (_:xs) = 1 + myLength xs

-- 3. mean of a list
mean xs = sum xs / (fromIntegral (length xs))

-- 4. make a palindrome
palindromize xs = xs ++ reverse xs

-- 5. is a palindrome
isPalindrome []  = True
isPalindrome [x] = True
isPalindrome xs  = ((head xs) == (last xs)) && isPalindrome (tail (init xs))

-- 6. sort list of lists by length
listCmp xs ys = compare (length xs) (length ys)
sortLists lists = sortBy listCmp lists
