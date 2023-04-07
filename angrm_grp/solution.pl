app([], L, L).
app([H | T], L, [H | R]) :- app(T, L, R).

mem(X, [X | _]).
mem(X, [H | T]) :- x \= H, mem(X, T).

insert(X, L, R) :- app(A, B, L), app(A, [X | B], R).

perm([], []).
perm([H | T], R) :- perm(T, P), insert(H, P, R).



insert_in_classes(X, L, R) :- app(A, [C | B], L), 
                              perm(X, P),
                              mem(P, C),
                              app(A, [[X | C] | B], R).

insert_in_classes(X, L, [[X] | L]) :- not((app(_, [C | B], L), 
                                           perm(X, P),
                                           mem(P, C))).

group([], []).
group([H | T], R) :- group(T, R1), 
                     insert_in_classes(H, R1, R).