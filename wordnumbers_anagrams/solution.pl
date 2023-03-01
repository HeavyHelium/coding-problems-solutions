app([], L, L).
app([H | T], L, [H | R]) :- app(T, L, R).

insert(X, L, R) :- app(A, B, L), app(A, [X | B], R).

permute([], []).
permute([H | T], R) :- permute(T, P), insert(H, P, R).

valid_anagram([], []).

valid_anagram(L, [0 | Next]) :- app(['z', 'e', 'r', 'o'], T, L), 
                                valid_anagram(T, Next).

valid_anagram(L, [1 | Next]) :- app(['o', 'n', 'e'], T, L),
                                valid_anagram(T, Next).

valid_anagram(L, [2 | Next]) :- app(['t', 'w', 'o'], T, L), 
                                valid_anagram(T, Next).     

valid_anagram(L, [3 | Next]) :- app(['t', 'h', 'r', 'e', 'e'], T, L),   
                                valid_anagram(T, Next).

valid_anagram(L, [4 | Next]) :- app(['f', 'o', 'u', 'r'], T, L),
                                valid_anagram(T, Next).

valid_anagram(L, [5 | Next]) :- app(['f', 'i', 'v', 'e'], T, L),
                                valid_anagram(T, Next).

valid_anagram(L, [6 | Next]) :- app(['s', 'i', 'x'], T, L),
                                valid_anagram(T, Next).

valid_anagram(L, [7 | Next]) :- app(['s', 'e', 'v', 'e', 'n'], T, L),
                                valid_anagram(T, Next).

valid_anagram(L, [8 | Next]) :- app(['e', 'i', 'g', 'h', 't'], T, L),
                                valid_anagram(T, Next).

valid_anagram(L, [9 | Next]) :- app(['n', 'i', 'n', 'e'], T, L),
                                valid_anagram(T, Next).


is_sorted([]).
is_sorted([_]).
is_sorted([H1, H2 | T]) :- H1 =< H2, is_sorted([H2 | T]).

get_numbers_from_anagram(L, R) :- permute(L, P), 
                                  valid_anagram(P, R), 
                                  is_sorted(R).

%?- get_numbers_from_anagram(['o', 'n', 'e',  'i', 'g', 'e', 'h', 't'], R).