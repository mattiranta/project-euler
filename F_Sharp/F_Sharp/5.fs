[<AutoOpen>]
module _5

// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

let numDivisibleByAll numbers n = 
    List.forall (fun i -> n % i = 0 ) numbers

let Run() =
    //let res = Seq.unfold (fun x -> Some(x, x + 20)) 20 
    //          |> Seq.find (fun n -> numDivisibleByAll [11;12;13;14;15;16;17;18;19] n) 
    let res = lib.reduce lib.lcm [1 .. 21]
    sprintf "Smallest positive number evenly divisible by all [%A..%A] : %A" 1 20 res
