subset([], []). 
subset([H | T], [H | T1]) :- subset(T, T1).
subset([_ | T], T1) :- subset(T, T1).


# ?- subset([1, 2, 3], S).
# S = [1, 2, 3] ;
# S = [1, 2] ;
# S = [1, 3] ;
# S = [1] ;
# S = [2, 3] ;
# S = [2] ;
# S = [3] ;
# S = [].