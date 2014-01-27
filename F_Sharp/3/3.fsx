/// The prime factors of 13195 are 5, 7, 13 and 29.
/// What is the largest prime factor of the number 600851475143 ?

let mySeq = seq { for i in 1 .. 999 do if i % 3 = 0 || i % 5 = 0 then yield i }
let sum = Seq.fold (fun acc elem -> acc + elem) 0 mySeq

printfn "%d" sum