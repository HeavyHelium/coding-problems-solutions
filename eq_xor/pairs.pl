between(A, B, A) :- A =< B.
between(A, B, C) :- A < B, 
                    A1 is A + 1, 
                    between(A1, B, C).

pairs([A, B], S) :- between(0, S, A), 
                    B is S - A.

genAnswers(M, N) :- pairs([A, B], M), 
                    A xor B =:= N,
                    write([A, B]), nl, fail.
                
