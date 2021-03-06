-- file: ch04/InteractWith.hs

module InteractWith where
-- import only the getArgs function from System.Environment
import System.Environment (getArgs)

interactWith function inputFile outputFile = do
  input <- readFile inputFile
  writeFile outputFile (function input)

mainWith function = do
  args <- getArgs
  case args of
    [input, output] -> interactWith function input output
    _ -> putStrLn "error: exactly two arguments needed"
