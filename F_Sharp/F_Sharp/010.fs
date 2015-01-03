[<AutoOpen>]
module _10

open System

// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.

let Run() =
    let n = bigint 2000000
    let sum = (lib.sieveOfErastothenes (int n)) |> Seq.map (fun x -> Numerics.BigInteger(x: int)) |> Seq.takeWhile (fun x -> x < n) |> Seq.sum

    sprintf "Sum of primes below %d: %A" (int n) sum