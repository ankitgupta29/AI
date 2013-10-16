READ ME
-------------

ANKIT GUPTA
UIN: 621009649
Artificial Intelligence
														
TO LOAD:
	(load "deriv.lsp")
	
TO EXECUTE:	
	deriv : to differentiate
		(deriv expr var)
	deriv-eval: to derive and evaluate
		(deriv-eval expr var val)
	simplify: to simplify expressions	
		(simplify expr)
	deriv-simplify: to find derivative and simplify the output
		(deriv-simplify expr var)
	evaluate : to evaluate value of an expression
		(evaluate expr var val)

Test Cases and Output		
---------------------
1. (deriv '(- (sqrt (* 8 x)) (* (log x) (* 2 (* x x)))) 'x)
OUTPUT : (- (* (* 1/2 (/ 1 (SQRT (* 8 X)))) 8) (+ (* (LOG X) (* 2 (* 2 X))) (* (* 2 (* X X)) (/ 1 X))))

2. (deriv '(* (sin (* 2 x)) (+ (sqrt x) (exp x))) 'x)
OUTPUT : (+ (* (SIN (* 2 X)) (+ (* 1/2 (/ 1 (SQRT X))) (EXP X))) (* (+ (SQRT X) (EXP X)) (* 2 (COS (* 2 X)))))

3. (deriv '(/ (exp (* 5 x)) (* x (+ 3 x))) 'x)
OUTPUT : (* (/ 1 (* (* X (+ 3 X)) (* X (+ 3 X)))) (- (* (* X (+ 3 X)) (* 5 (EXP (* 5 X)))) (* (EXP (* 5 X)) (+ X (+ 3 X)))))

4. (deriv '(+ (- (cos (* x x)) (* x 3)) (* (* x x) (* x 4))) 'x)
OUTPUT : (+ (- (* (* 2 X) (* -1 (SIN (* X X)))) 3) (+ (* (* X X) 4) (* (* X 4) (* 2 X))))

5. (deriv-eval '(* (+ (sqrt x) (exp x)) (/ (* x 2) (log x))) 'x 10)
OUTPUT : 202145.4

6. (deriv-eval '(/ 1 (- (* x x) (+ (* 2 (* x x)) (sqrt (* x x))))) 'x 2)
OUTPUT : 5/36

7. (deriv-eval '(+ (cos (* 5 x)) (- (sin (* x x)) (* 5 x))) 'x 50)
OUTPUT : 75.83515

8. (simplify '(+ 0 (- ( * x 0) (/(* x x) 5))))
OUTPUT : (* -1 (/ (* X X) 5))

9. (simplify '(* (* 1 x) (- x 0)))
OUTPUT : (* X X)

10.(simplify '(+ (* 1 x) (- (+ x 0)(/ x 1))))
OUTPUT : X

11. (simplify '(+ 0 (- ( * x 0) (/(* (log 0) x) 5))))
OUTPUT : Undefined

12. (simplify '(+ 0 (- ( * (cos x) 0) (/(* (log 10) x) 5))))
OUTPUT: (* -1 (/ (* 2.3025851 X) 5))
