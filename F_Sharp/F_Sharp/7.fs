[<AutoOpen>]
module _7


// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
// we can see that the 6th prime is 13.
// What is the 10001 prime number?

let Run() =
    let n = 10001
    let r = lib.findNthPrime n
    sprintf "%dth prime number: %d" n r