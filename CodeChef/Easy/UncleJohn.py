try:
    for _ in range(int(input())):
        n = int(input())
        songs = list(map(int, input().split()))
        k = int(input())
        print(songs)
        temp = songs[k-1]
        songs.sort()

        print(songs.index(temp))
except:
    pass
