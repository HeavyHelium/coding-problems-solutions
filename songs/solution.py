
def gen_playlist(input: list[list[int]]):
    songs: set[int] = set()

    for playlist in input:
        for song in playlist:
            songs.add(song)

    print(songs)



if __name__ == "__main__":
    input = [[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]
    gen_playlist(input)
    print("Hello World!")