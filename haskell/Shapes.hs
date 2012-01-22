module Shapes (
  Point(..),  -- .. to export all value constructors
  Shape(..),  -- Shape (Circle) to export just one of the value ctors
  surface,
  nudge,
  baseCircle,
  baseRect
) where

data Point = Point Float Float deriving (Show)

-- Circle and Rectangle are value constructors which are just functions
-- taking certain parameters and returning the new algebraic data type
-- we're creating (e.g. Shape)
data Shape = Circle Point Float
           | Rectangle Point Point 
           deriving (Show)

surface :: Shape -> Float
surface (Circle _ r) = pi * r ^ 2
surface (Rectangle (Point x1 y1) (Point x2 y2)) =
   (abs $ x2 - x1) * (abs $ y2 - y1)

nudge :: Shape -> Float -> Float -> Shape
nudge (Circle (Point x y) r) a b = Circle (Point (x+a) (y+b)) r
nudge (Rectangle (Point x1 y1) (Point x2 y2)) a b =
    Rectangle (Point (x1+a) (y1+b)) (Point (x2+a) (y2+b))

origin = (Point 0 0)

baseCircle :: Float -> Shape
baseCircle r = Circle origin r

baseRect :: Float -> Float -> Shape
baseRect width height = Rectangle origin (Point width height)
