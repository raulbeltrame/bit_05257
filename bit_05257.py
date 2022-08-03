stop = "f"
while stop != "v":
    N = int(input().strip())
    if (N > 1000):
        print("ERRO")
        stop ="v"
        break

    S1 = str(input().strip())
    S2 = str(input().strip())

    expression= str(input().strip())

    if len(S1) != N or len(S2) != N:
        print("ERRO")
        stop ="v"
        break

    erro = "f"
    for i in range(N):
        if S1[i] != "1" and S1[i] != "0":
            erro = "v"
        elif S2[i] != "1" and S2[i] != "0":
            erro = "v"
    if erro == "v":
        print("ERRO")
        stop ="v"
        break
