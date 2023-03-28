count(_, [], 0).
count(H, [H | T], Res) :-  count(H, T, R1), 
                           Res is R1 + 1.

count(H, [H1 | T], Res) :-  H \= H1, 
                            count(H, T, Res).

contains(_, [], false).
contains(H, [H | _], true).
contains(H, [H1 | T], Res) :-  H \= H1, 
                               contains(H, T, Res).

mapped([], _,  []).
mapped([H | T], L, [[H, Occ] | Res]) :- count(H, L, Occ),  
                                        mapped(T, L, Res).

order([_, V1], [_, V2]) :- V1 > V2.
order([K1, V1], [K2, V1]) :- K1 @=< K2. 

append([], L, L).
append([H | T], L, [H | Res]) :- append(T, L, Res).


insert(X, L, R) :- append(L1, L2, L), 
                   append(L1, [X | L2], R).

permutation([], []).
permutation([H | T], R) :- permutation(T, R1), 
                           insert(H, R1, R).

is_sorted([]).
is_sorted([_]).
is_sorted([H1, H2 | T]) :- order(H1, H2), 
                           is_sorted([H2 | T]).

bogosort([], []).
bogosort([H | T], R) :- permutation([H | T], R), 
                        is_sorted(R).

get_keys([], []).
get_keys([[K, _] | T], [K | R]) :- get_keys(T, R).

sort_string(S, R) :- mapped(S, S, M), 
                     bogosort(M, M1), 
                     get_keys(M1, R).
