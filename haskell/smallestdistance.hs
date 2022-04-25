
smallestDistance xs = [distance | (a,b,c) <- xs, let distance = sqrt(a^2 + b^2 + c^2), distance < 10]