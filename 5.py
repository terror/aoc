def main():
    ans, s = 0, []
    for i in [i for i in open('input/5.txt').readlines()]:
        x = int((i[:7].replace("F", "0").replace("B", "1")), 2) * 8 \
            + int(i[7:].replace("L", "0").replace("R", "1"), 2)
        ans = max(ans, x)
        s.append(x)
    print("Part 1:", ans)
    s.sort()
    print("Part 2:", *[s[i]-1 for i in range(1, len(s)) if s[i-1] != s[i]-1])


if __name__ == '__main__':
    main()
