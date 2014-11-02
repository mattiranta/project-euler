[<AutoOpen>]
module _13

open System
open System.Numerics
open lib

//  Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

let Run() =
    let sumDigits = "13_input.txt" 
                    |> lib.readlines 
                    |> Seq.map (fun l -> BigInteger.Parse l) 
                    |> Seq.sum 
                    |> sprintf "%A"  
                    |> Seq.take 10 
                    |> String.Concat

    sprintf "First ten digits of the sum: %A" sumDigits