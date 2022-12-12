def Function(Array):
    SearchIndex = Array[0]
    SearchChar = [i for i in Array[1:]]
    CopyString = SearchIndex

    Output = []
    Return = ""
    i = 1
    while True:
        i += 1
        try:
            if len(str(CopyString).removesuffix(SearchChar[-i])) != len(CopyString):
                CopyString = str(CopyString).removesuffix(SearchChar[-i]).strip()
                Output.append(str(SearchChar[-i]).strip())
                SearchChar.pop(-i)
                i = 1
                if len(CopyString) == 0:
                    break
        except:
            print("Kelime Tanımlanmamış.")
            break

    for i in range(1, len(Output) + 1):
        Return += Output[-i]

    print(f"Output : {str(Return)}")
    print(Output)


Function(
    ["HastaneOrmanPatatesKöftesi", "tesi", "OrmanPata", "manKı", "taneOr", "tesKöf", "Bil", "Ama", "Hastanse", "Amaz",
     "zon", "da", "Bilgi"])
