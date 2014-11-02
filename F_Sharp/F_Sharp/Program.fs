module _main

open System

[<EntryPoint>]
let main argv = 
    let sw = Diagnostics.Stopwatch()
    sw.Start()
    let res = Run()
    printfn "%s" res
    System.Diagnostics.Debug.WriteLine res
    sw.Stop()
    printfn "Time: %.02f s" sw.Elapsed.TotalSeconds
    
    match argv with
        | [|"--wait"|] -> printf "Press any key to quit"; Console.ReadKey(true) |> ignore
        | _ -> ()
    0 
