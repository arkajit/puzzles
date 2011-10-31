-- file: ch03/Intersperse.hs

intersperse :: a -> [[a]] -> [a]

intersperse _ []      = []
intersperse s [x]     = x
intersperse s (x:xs)  = x ++ s:(intersperse s xs)
