-- Codebreaker: a simple game where you try to unlock a 5-digit code
-- Authors: Arkajit Dey, David Lewis
--
-- Gameplay:
--  1) Enter a guess.
--  2) Computer returns a hint string like '.*XX.' where
--      X = correct digit in the correct place
--      * = a digit that's in the code, but in the wrong place
--      . = a digit that's not in the codea
--  3) Use the hint to refine your guess. Try to crack the code
--     using as few guesses as you can!

import System.Random

evaluateGuess :: [Int] -> [Int] -> String
evaluateGuess guess solution = evaluateGuessInner guess solution
  where evaluateGuessInner (x:xs) (y:ys) = (result):(evaluateGuessInner xs ys)
          where result = if x == y
                           then 'X'
                         else if (x `elem` solution)
                           then '*'
                         else '.'
        evaluateGuessInner _ _ = ""

-- Break a positive integer into a list of its digits
-- NOTE(arkajit): trims leading zeros
numToDigits :: Int -> [Int]
numToDigits = reverse . helper
  where helper n
          | n < 10      = [n]
          | otherwise   = (n `mod` 10):(helper $ n `div` 10)

-- TODO(arkajit): break this up into a few functions
-- (e.g. playing a single round, etc...)
main = do
  gen <- getStdGen
  putStrLn "I'm thinkin' of a 5-digit code. Can you guess it?:"
  guessStr <- getLine
  let guess = numToDigits $ read guessStr
      code = take 5 $ randomRs (0, 9) gen 
      response = evaluateGuess guess code
  if response == "XXXXX"
    then putStrLn "That's right!"
    else do
      putStrLn ("Close, but not quite: " ++ response)
      main
