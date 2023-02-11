app([], L, L).
app([H | T], L, [H | R]) :- app(T, L, R).

leq_ord([_, B], [_, D]) :- B =< D.

partition([], _, [], []).
partition([H | T], P, [H | L], G) :- leq_ord(H, P), 
                                     partition(T, P, L, G).
partition([H | T], P, L, [H | G]) :- not(leq_ord(H, P)), 
                                     partition(T, P, L, G).

quicksort([], []).
quicksort([H | T], S) :- partition(T, H, L, G),
                         quicksort(L, SL),
                         quicksort(G, SG), 
                         app(SL, [H | SG], S).

schedule_helper([], _, []).
schedule_helper([[A, B] | T], C, [[A, B] | R]) :- A >= C, 
                                                  schedule_helper(T, B, R).
schedule_helper([[A, _] | T], C, R) :- A < C,
                                       schedule_helper(T, C, R).

schedule([], []).
schedule([H | T], R) :- quicksort([H | T], S),
                        schedule_helper(S, 0, R).

%schedule([[2, 5], [5, 10], [10, 20], [20, 30], [30, 45]], R).