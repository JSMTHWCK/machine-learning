clothing tempc 
    | tempf >= 80 = "wearing a short sleeve shirt is advised"
    | tempf >= 65 = "wearing a long sleeve shirt is uncomfortable, but you should do it"
    | tempf >= 50 = "https://www.youtube.com/watch?v=GCdwKhTtNNw"
    | otherwise = "colder than anything in california ... wear a jacket"
    where tempf = tempc* 1.8 + 32
