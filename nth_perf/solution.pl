sum_digits(0, 0).
sum_digits(X, Sum) :- X > 0, 
                      Digit is X mod 10,
                      Temp is X // 10,
                      sum_digits(Temp, Sum1), 
                      Sum is Digit + Sum1.


perfect(X) :- sum_digits(X, Sum), Sum = 10.

num_perfect_before(X, 0) :- X < 19.
num_perfect_before(X, K) :- X >= 19,
                            perfect(X),
                            Temp is X - 1,
                            num_perfect_before(Temp, K1),
                            K is K1 + 1.

num_perfect_before(X, K1) :- X >= 19,
                            not(perfect(X)),
                            Temp is X - 1,
                            num_perfect_before(Temp, K1).


nat(0).
nat(N) :- nat(M), N is M + 1.


n_th_perfect(N, X) :- nat(X),
                      perfect(X), 
                      num_perfect_before(X, K), 
                      K =:= N, 
                      !.