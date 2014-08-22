module _3
open lib

/// The prime factors of 13195 are 5, 7, 13 and 29.
/// What is the largest prime factor of the number 600851475143 ?

let Run() =
    let n = 600851475143I

    let test1 = isPrime 2
    let test2 = isPrime 4
    let test3 = isPrime 7

    sprintf "Largest prime factor: %d" -1