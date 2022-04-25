chain 1 = [1]
chain n | even n = n: chain (n `div` 2) | odd n = n : chain (n * 3 + 1)

-- returns list
-- sum (takeWhile (<1000) (map (^2) [1..])) 
firstChainLonger n =  length (takeWhile (<=n) [length chainarr | chainarr <- [chain i | i <- [1..]]] )