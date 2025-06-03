import sys


def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = int(input[ptr]), int(input[ptr + 1])
    ptr += 2
    x_list = list(map(int, input[ptr:ptr + N]))
    ptr += N

    # 预处理每个i的前缀和
    max_i = 15
    pre = []
    for i in range(max_i + 1):
        mod = 1 << (i + 1)
        cnt = [0] * mod
        for x in x_list:
            r = x % mod
            cnt[r] += 1
        # 构建前缀和数组
        prefix = [0] * (mod + 1)
        for j in range(mod):
            prefix[j + 1] = prefix[j] + cnt[j]
        pre.append(prefix)

    delta = 0
    for _ in range(M):
        op = input[ptr]
        ptr += 1
        if op == 'C':
            d = int(input[ptr])
            ptr += 1
            delta = (delta + d) % 65536
        elif op == 'Q':
            i = int(input[ptr])
            ptr += 1
            mod = 1 << (i + 1)
            d_mod = delta % mod
            # 计算区间A
            startA = max(0, (1 << i) - d_mod)
            endA = (mod - d_mod) - 1
            countA = 0
            if startA <= endA:
                endA_plus1 = endA + 1
                if endA_plus1 > mod:
                    endA_plus1 = mod
                if startA < mod:
                    countA = pre[i][endA_plus1] - pre[i][startA]
            # 计算区间B
            startB = max(0, mod + (1 << i) - d_mod)
            endB = mod - 1
            countB = 0
            if startB <= endB and startB < mod:
                endB_plus1 = endB + 1
                if endB_plus1 > mod:
                    endB_plus1 = mod
                countB = pre[i][endB_plus1] - pre[i][startB]
            print(countA + countB)


if __name__ == '__main__':
    main()