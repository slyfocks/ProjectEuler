--sum of digits in factorial
factorial :: Integer -> Integer
factorial x = foldl (*) 1 [1..x]

digits :: Integral a => a -> [a]
digits 0 = []
digits x =  x `mod` 10 : digits (x `div` 10)

digitSum :: Num a => [a] -> a
digitSum xs =  foldl (+) 0 xs

answer = digitSum $ digits $ factorial 100

main = do putStrLn $ show answer