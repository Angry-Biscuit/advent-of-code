def find_xmas(board: list[list[str]]) -> int:
    XMAS = ['X', 'M', 'A', 'S']
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    m, n = len(board), len(board[0])
    def dfs(r: int, c: int, idx: int, towards: int) -> int:
        cnt = 0
        if not 0 <= r < m or not 0 <= c < n:
            return 0
        if board[r][c] != XMAS[idx]:
            return 0
        if board[r][c] == 'S':
            return 1
        
        dr, dc = directions[towards]
        nr, nc = r + dr, c + dc
        cnt += dfs(nr, nc, idx+1, towards)
        return cnt
    
    res = 0
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'X':
                for d in range(8):
                    res += dfs(r, c, 0, d)
    return res

def part2(board: list[list[str]]):
    m, n = len(board), len(board[0])
    res = 0
    for r in range(1, m-1):
        for c in range(1, n-1):
            if board[r][c] == 'A':
                if board[r-1][c-1] == 'M' and board[r-1][c+1] == 'M' and board[r+1][c-1] == 'S' and board[r+1][c+1] == 'S':
                    res += 1
                elif board[r-1][c-1] == 'S' and board[r-1][c+1] == 'S' and board[r+1][c-1] == 'M' and board[r+1][c+1] == 'M':
                    res += 1
                elif board[r-1][c-1] == 'M' and board[r-1][c+1] == 'S' and board[r+1][c-1] == 'M' and board[r+1][c+1] == 'S':
                    res += 1
                elif board[r-1][c-1] == 'S' and board[r-1][c+1] == 'M' and board[r+1][c-1] == 'S' and board[r+1][c+1] == 'M':
                    res += 1
    return res

def main():
    board = []
    with open('input.txt', 'r') as f:
        for line in f:
            board.append(line.rstrip())
    cnt = find_xmas(board)
    print(cnt)
    cnt = part2(board)
    print(cnt)

if __name__ == '__main__':
    main()