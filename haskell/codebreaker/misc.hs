-- graveyard of functions we don't need anymore

evaluateGuess :: [Int] -> [Int] -> String
evaluateGuess nums [] = ""
evaluateGuess nums@(n:ns) (g:gs)
  | n == g      = 'X':rest
  | isin g      = '*':rest
  | otherwise   = '.':rest
  where rest = evaluateGuess ns gs
        isin = flip elem $ nums

isHit :: [Int] -> [Int] -> [Bool]
isHit = zipWith (==)

isNearHit :: [Int] -> [Int] -> [Bool]
isNearHit nums [] = []
isNearHit nums (g:gs) = (isin g):(isNearHit nums gs)
  where isin = flip elem $ nums
