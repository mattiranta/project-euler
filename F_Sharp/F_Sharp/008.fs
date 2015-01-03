[<AutoOpen>]
module _8

// Find the greatest product of five consecutive digits in the 1000-digit number. 

open System

let Run() =
    let text = "../../data/008_input.txt" |> lib.fileread |> lib.replaceText "\r\n" ""
    let strLen = String.length text
    let r = seq {for i in 0 .. (strLen - 5) do yield text.Substring(i, 5)} 
            |> Seq.map(fun n -> seq {for i in 0 .. 4 do yield int(n.Substring(i, 1))} 
                                |> Seq.fold (fun x acc -> x*acc) 1  ) 
            |> Seq.max

    sprintf "Greatest product of five consecutive digits: %d" r