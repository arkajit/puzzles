-- file: ch03/Tree.hs
data Tree a = Node a (Tree a) (Tree a)
						| Empty
							deriving (Show)

simpleTree = Node "parent" (Node "left child" Empty Empty)
													 (Node "right child" Empty Empty)

data SimplerTree a = SimplerNode a (Maybe (SimplerTree a))
																	 (Maybe (SimplerTree a))
										 deriving (Show)

-- Must have the two Nothings at the end, otherwise interpreted as
-- creating a new two-parameter function with "a" bound to first
-- parameter of SimplerNode function
aTree = SimplerNode "a" Nothing Nothing
bTree = SimplerNode "b" Nothing Nothing
simplerTree = SimplerNode "parent" (Just aTree) (Just bTree)
