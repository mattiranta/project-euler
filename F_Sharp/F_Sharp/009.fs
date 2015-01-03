[<AutoOpen>]
module _9

open System

// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//
// a2 + b2 = c2
// For example, 32 + 42 = 9 + 16 = 25 = 52.
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

let square n = n * n



let Run() =
    let triplet = seq { for i in 1..1000 do for j in 1..i do yield (i, j) } 
                    |> Seq.map (fun (a, b) -> a, b, (sqrt ((square (float a)) + (square (float b)))))
                    |> Seq.filter (fun (a,b,c) -> round c = c )
                    |> Seq.find (fun (a, b, c) -> a + b + int(c) = 1000)
    
    let a, b, c = triplet

    sprintf "a * b * c = %d * %d * %d = %d" a b (int c) (a * b * int(c))