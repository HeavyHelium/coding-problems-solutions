subseq([], []).
subseq([H | T], [H | Res]) :- subseq(T, Res).
subseq([_ | T], Res) :- subseq(T, Res).

