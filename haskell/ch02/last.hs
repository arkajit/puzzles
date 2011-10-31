-- file: ch02/last.hs
lastButOne xs = head (tail (reverse xs))
-- throws an exception if xs has fewer than two elements
