[<AutoOpen>]
module _12

/// What is the value of the first triangle number to have over five hundred divisors?

// Three implementations for triangulars:
let triangulars_unfold =
    Seq.unfold 
        (fun n -> Some((n*(n+1I)/2I), n + 1I)) 
        1I

let triangulars_unfold_and_sum =
    Seq.unfold (fun (acc, state) -> Some (acc, (state + acc, state + 1I))) (0I, 1I)
    |> Seq.skip 1 // skip the initial 0

let triangulars_yield =
    let rec loop (n: bigint) =
        seq { 
            yield (n*(n+1I)/2I) 
            yield! loop (n + 1I)
        }

    loop 1I

let triangulars =
    //triangulars_unfold
    //triangulars_unfold_and_sum
    triangulars_yield

let Run() =
    let limit = 500
    let t = triangulars 
            |> Seq.filter (fun n -> (n % bigint(2)) = 0I )

            // Choose either one of the following implementations:
            //|> Seq.map (fun n -> (n, lib.divisorCount_Bigint n))   // Big integer version, orders of magnitude slower
            |> Seq.map (fun n -> (n, lib.divisorCount (uint64 n)))      // int version, will overflow at some point

            |> Seq.filter (fun (n, count) -> count > limit)
            |> Seq.nth 0

    sprintf "First triangle with over %d divisors: %A (%A divisors)" limit (fst t) (snd t) 