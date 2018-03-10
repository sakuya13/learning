import Data.Function
import Data.List
-- 1. Write a function that computes the number of elements in a list. To test 
-- it, ensure that it gives the same answers as the standard length function.

len :: [a] -> Int
len [] = 0
len (x:xs) = 1 + len xs

-- 3. Write a function that computes the mean of a list, i.e., the sum of 
-- all elements in the list divided by its length. (You may need to use the 
-- fromIntegral function to convert the length of the list from an integer 
-- into a floating-point number.)

mean' :: (Fractional t) => [t] -> t
mean' xs 
    | null xs        = error "no elements"
    | otherwise      = sum' xs / fromIntegral (length xs) 

sum' :: (Num t) => [t] -> t
sum' [] = 0
sum' (y:ys) = y + sum' ys

-- 4. Turn a list into a palindrome; i.e., it should read the same both 
-- backward and forward. For example, given the list [1,2,3], your function 
-- should return [1,2,3,3,2,1].

palin :: [t] -> [t]
palin zs = append zs (myReverse zs)

append :: [t] -> [t] -> [t]
append [] xs = xs
append (y:ys) xs = y : append ys xs

myReverse :: [t] -> [t]
myReverse xs = rReverse xs []

rReverse :: [t] -> [t] -> [t]
rReverse [] temp = temp
rReverse (y:ys) temp = rReverse ys (y:temp)

-- 5. Write a function that determines whether its input list is a palindrome.

isPalin :: (Eq t) => [t] -> Bool
isPalin xs
    | null xs            = True
    | xs == myReverse xs = True
    | otherwise          = False

-- 6. Create a function that sorts a list of lists based on the length of 
-- each sublist. (You may want to look at the sortBy function from 
-- the Data.List module.)
sortList :: (Ord t) => [[t]] -> [[t]]
sortList xs = sortBy (compare `on` length) xs

-- 7. Define a function that joins a list of lists together using
-- a separator value.

interesperse :: t -> [[t]] -> [t]
interesperse _ [] = []
interesperse _ [x] = x
interesperse a (x:xs) = x ++ [a] ++ interesperse a xs
-- interesperse a (x:xs)
--     | length (x:xs) == 1 = x
--     | length (x:xs) > 1 = x ++ [a] ++ interesperse a xs
--     | otherwise         = []

foo _ [] = []
foo _ [x] = x
foo a (x:xs) =
    case x of
        []     -> a : foo a xs
        (y:ys) -> y : foo a (ys:xs)

-- foo' a ((x:xs):xss)
-- foo' a ([]:xss) 
--
