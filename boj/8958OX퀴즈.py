for test in range(int(input())):
    results = input()
    ans = 0
    now = 0
    for i in range(len(results)):
        if results[i] == "O":
            ans += now + 1
            now += 1
        else:
            now = 0
    print(ans)
