from typing import List


def valid_count(N: int, M: int, K: int) -> int:
    """
    M unique songs downloaded
    make playlist of N > M songs, s.t. 
    a song cannot be played again iff 
    there are at least K other songs in between
    :Returns: the number of valid playlists
    """
    # dp[i][j] -- number of valid playlists of length i, 
    #             containing j unique songs
    dp: List[List[int]] = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # play a new song 
            dp[i][j] += dp[i - 1][j - 1] * (N - j + 1)
            # play a song already played
            if(j > K):
                dp[i][j] += dp[i - 1][j] * (j - K) 

    return dp[N][M]


if __name__ == "__main__":

    print(valid_count(3, 3, 1))
