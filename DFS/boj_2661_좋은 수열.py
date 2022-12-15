import sys
input = sys.stdin.readline

n = int(input().strip())
global answer, check
answer, check = 0, False

def dfs(seq: str):
    global answer, check
    if len(seq) == n + 1:
        answer = int(seq[:-1])
        check = True
    else:
        if check:
            return
        for i in range(1, len(seq)//2 + 1):
            if seq[-2*i:-i] == seq[-i:]:
                break
        else:
            dfs(f"{seq}1")
            dfs(f"{seq}2")
            dfs(f"{seq}3")
    return

if __name__ == "__main__":
    dfs("")
    print(answer)