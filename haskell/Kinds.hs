import Types

-- Typeclass
-- t has kind * -> (* -> *) -> *
class Tofu t where
  tofu :: j a -> t a j

-- Custom Algebraic Datatype (ADT)
data Frank a b = Frank {
  frankField :: b a
} deriving (Show)

-- Mae type Frank a member of typeclass Tofu
instance Tofu Frank where
  tofu x = Frank x

-- Barry has kind: (* -> *) -> * -> * -> *
data Barry t k p = Barry {
  yabba :: p,  -- type p is kind * since values must have concrete types
  dabba :: t k  -- type t is kind (* -> *), k is *, so that dabba is concrete
} deriving (Show)

-- fmap :: (a -> b) -> f a -> f b
instance Functor (Barry a b) where
  fmap f (Barry {yabba = x, dabba = y}) = Barry {yabba = f x, dabba = y}

