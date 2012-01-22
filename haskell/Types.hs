module Types (
  Day(..),
  Tree(..),
  TrafficLight(..)
) where

-- nullary constructors take no parameters
data Day = Monday | Tuesday | Wednesday
         | Thursday | Friday | Saturday | Sunday
          deriving (Eq, Ord, Show, Read, Bounded, Enum)

-- a is a type parameter. Like templated classes in imperative OOP langs.
data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

data TrafficLight = Red | Yellow | Green

-- Make TrafficLight an instance of the Eq typeclass by providing a minimal
-- complete definition of Eq's functions
instance Eq TrafficLight where
  Red == Red = True
  Green == Green = True
  Yellow == Yellow = True
  _ == _ = False

instance Show TrafficLight where
  show Red = "Red light"
  show Yellow = "Yellow light"
  show Green = "Green light"

--instance Functor (Map k) where
--  fmap f (Map k v) = Map k (f v)
