rev_helper([], Acc, Acc).
rev_helper([H | T], Acc, Res) :- 
    rev_helper(T, [H | Acc], Res).

rev(L, R) :- rev_helper(L, [], R).


upside_down(0, 0).
upside_down(1, 1).
upside_down(6, 9).
upside_down(8, 8).
upside_down(9, 6).


to_digits_stack(0, [0]).
to_digits_stack(Digit, [Digit]) :- Digit >= 1, Digit =< 9.
to_digits_stack(Number, [Digit | Next]) :-
    Number > 9, 
    Digit is Number mod 10,
    Temp is Number // 10,
    to_digits_stack(Temp, Next).


to_digits(N, Res) :- 
    to_digits_stack(N, Digits), 
    rev(Digits, Res).

% to_upside_down_helper(Digits, Res)
to_upside_down_helper([], []).
to_upside_down_helper([Digit | Next], [Udd | Res]) :- 
    upside_down(Digit, Udd),
    to_upside_down_helper(Next, Res).  


to_upside_down(Number, Res) :-
    to_digits_stack(Number, Digits),
    to_upside_down_helper(Digits, Res).


is_strobogrammatic(M) :-
    to_upside_down(M, Udd),
    to_digits(M, Digits),
    Udd = Digits.

between(A, B, A) :- A =< B.
between(A, B, C) :- 
    A < B, 
    A1 is A + 1, 
    between(A1, B, C).


gen_strobogrammatic(N, Res) :-
    LB = 10 ** (N - 1),
    UB = 10 ** N - 1,
    between(LB, UB, M),
    is_strobogrammatic(M),
    Res = M.
