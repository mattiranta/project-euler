[<AutoOpen>]
module _3
open System

/// The prime factors of 13195 are 5, 7, 13 and 29.
/// What is the largest prime factor of the number 600851475143 ?

let factorize(n)  =
    let factors = seq {
        //let limit = BigIntSqrt (bigint(n))
        let limit = int64(sqrt(float(n)))
        
        for i in 2L .. limit  do
            if n % i = 0L && lib.trialDivision i then yield i
    }
    factors

let factorizeBigInt(n:bigint)  =
    let factors = seq {
        let limit = lib.BigIntSqrt (n)
        
        for i in 2I .. limit  do
            if n % i = 0I && lib.trialDivision_BigInt i then yield i
    }
    factors

let Run() =
    let useBigInt = false
    if not useBigInt then
        let n = 600851475143L
        let largestPrimeFactor = Seq.max (factorize n)
        sprintf "Largest prime factor: %A" largestPrimeFactor
    else
        let n_bigint = 600851475143I
        let largestPrimeFactor_bigint = Seq.max (factorizeBigInt n_bigint) + 1I
        sprintf "Largest prime factor (bigint): %A" largestPrimeFactor_bigint

        //if bigint(largestPrimeFactor) = largestPrimeFactor_bigint then
        //    sprintf "Largest prime factor: %A" largestPrimeFactor
        //else
        //    sprintf "Largest prime factor: (null)"
