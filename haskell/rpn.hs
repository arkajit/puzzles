-- LYAH Ch. 10
-- A Reverse Polish Notation calculator

import Data.List

solveRPN :: String -> Float
solveRPN = head . foldl foldFn [] . words
  where foldFn (x:y:ys) "*" = (x * y):ys
        foldFn (x:y:ys) "+" = (x + y):ys
        foldFn (x:y:ys) "-" = (y - x):ys
        foldFn (x:y:ys) "/" = (y / x):ys
        foldFn (x:y:ys) "^" = (y ** x):ys
        foldFn (x:xs) "log" = (log x):xs
        foldFn xs "sum" = [sum xs]
        foldFn xs numString = (read numString):xs
