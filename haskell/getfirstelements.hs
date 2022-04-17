reverseList [] = []
reverseList(x:xs) = reverseList xs ++ [x]

getFirstElements n _  | n <= 0 = []
getFirstElements n (x:xs) = x : getFirstElements (n-1) xs
-- x is head, xs is everything else

getLastElements n a = reverseList (getFirstElements n (reverseList a))