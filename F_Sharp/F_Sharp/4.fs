[<AutoOpen>]
module _4

// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
// Find the largest palindrome made from the product of two 3-digit numbers.


let isProductOfNumbersBetween n min max =
    match lib.factors n min max with
    | None -> false
    | factors -> (printfn "%A" factors); true

let Run() =
    let largestProduct = 999 * 999
    let largestPalindrome = 
        seq { largestProduct .. -1 .. 1 } 
        |> Seq.filter (fun n -> lib.isPalindromic (n.ToString()) && isProductOfNumbersBetween n 99 999) 
        |> Seq.take 1

    sprintf "Largest palindromic number made of two 3-digit numbers: %A" largestPalindrome