#|
ANKIT GUPTA
HW1 AI FALL 2013
UIN: 621009649
|#
;----------------------------------------
; 	deriv
;----------------------------------------
(defun deriv (expr var)
  (if (atom expr)				; if expr is atom and equal to var return 1 else if constant 0
    (if (equal expr var) 1 0)      
    (cond                       
        ((eq '+ (first expr))     ; PLUS 
            (derivplus expr var))
        ((eq '* (first expr))     ; MULT
            (derivmult expr var))
        ((eq '- (first expr))     ; SUB
			(derivsub expr var))
		((eq '/ (first expr))     ; DIV
			(derivdiv expr var))          
		((eq 'expt (first expr))  ; EXPT
			(derivexpt expr var)) 
		((eq 'exp (first expr))   ; EXP 
			(derivexp expr var))
		((eq 'expt (first expr))  ; EXP 
			(derivexpt expr var))
		((eq 'sqrt (first expr))  ; SQRT
			(derivsqrt expr var))
		((eq 'log (first expr))   ; LOG
			(derivlog expr var)) 
		((eq 'cos (first expr))   ; COS
			(derivcos expr var))			
		((eq 'sin (first expr))   ; SIN
			(derivsin expr var))			
		((eq 'tan (first expr))   ; TAN
			(derivtan expr var))          
        (t                        ; Invalid
            (error "Invalid Expression!"))
     )
  )
)

;----------------------------------------
;       deriv log
;----------------------------------------
(defun derivlog(expr var)
    (smult
	    (deriv (second expr) var)
		(sdiv 1 (second expr))
    )
)


;----------------------------------------
;       deriv sqrt
;----------------------------------------
(defun derivsqrt(expr var)
	(if (numberp (second expr)) ; if expression is number, derivative is zero
			0
		(smult					
			(smult 
				(sdiv 1 2) 
				(sdiv 1 expr)
			)
		    (deriv (second expr) var) 
		)
	)
)

;----------------------------------------
;	deriv sin
;----------------------------------------
(defun derivsin (expr var)
    (smult
          (deriv (second expr) var)
          (ssin (second expr))
    )
)

;----------------------------------------
;	simplify sin
;----------------------------------------
(defun ssin (expr)
	(list 'cos expr)
)

;----------------------------------------	
;	deriv cos
;----------------------------------------
(defun derivcos (expr var)
    (smult
          (deriv (second expr) var)
          (smult 
          	-1
          	(scos (second expr))
          )
    )
)

;----------------------------------------
;	simplify cos
;----------------------------------------
(defun scos (expr)
	(list 'sin expr)
)

;----------------------------------------
;	deriv tan
;----------------------------------------
(defun derivtan (expr var)
    (smult
          (deriv (second expr) var)
          (splus
             1	
          	 (stan (second expr))
          	 
          )
    )
)

;----------------------------------------
;	simplify tan
;----------------------------------------
(defun stan (expr)
	;(list '(* tan tan) expr)
	(smult 
		(list 'tan expr) 
		(list 'tan expr)
	)
)

;----------------------------------------
;	deriv plus
;----------------------------------------
(defun derivplus (expr var)
    (splus
          (deriv (second expr) var)
          (deriv (third expr) var)
    )
)

;----------------------------------------
;	deriv sub
;----------------------------------------
(defun derivsub (expr var)
	(if (null (third expr))			; if third expr is null, expr is a Unary Minus
		(smult						; return (- (derivative of second expr))
			-1
			(deriv (second expr) var)
		)
		(ssub
			(deriv (second expr) var)
		    (deriv (third expr) var)
		)
	)
)

;----------------------------------------
;       deriv mult
;----------------------------------------
(defun derivmult (expr var)
    (splus
	(smult (second expr) (deriv (third expr) var))
        (smult (third expr) (deriv (second expr) var)) 
    )
)

;----------------------------------------
;       deriv div
;----------------------------------------
(defun derivdiv (expr var)
	(if (numberp (third expr))
		(if (zerop (third expr))					; if third exp is zero, return error
			(error "Error: Undefined !!")
			(smult
				(deriv (second expr) var)
				(sdiv 1 (third expr))
			)
		)
		(smult
			(sdiv 1 (smult (third expr) (third expr)))
			(ssub
				(smult (third expr) (deriv (second expr) var))
				(smult (second expr) (deriv (third expr) var))
			)
		)
	)
)

;----------------------------------------
;       deriv exp
;----------------------------------------
(defun derivexp(expr var)
    (smult
	    (deriv (second expr) var)
		expr     
    )
)

;----------------------------------------
;       deriv expt
;----------------------------------------
(defun derivexpt(expr var)
	(if (equal (third expr) 0)
		0
	)
	(smult
    	(smult
    		(third expr)
	    	(sexpt (second expr) (ssub (third expr) 1))			;(expt (second expr) (ssub (third expr) 1))
		)
		(deriv (second expr) var)
    )
)

;----------------------------------------
;	simplify expt
;----------------------------------------
(defun sexpt (x y)
	(if (equal x 0) 0)
	(if (equal y 0) 1)
	(if (equal x 1) 1)
	(if (equal y 0) x)
	(list 'expt x y) 
)

;----------------------------------------
;	splus
; if both numbers are numbers, return addition
; if either of them is zero, returns other
; if one of them is number and other is non zero, return list of addition of both
;----------------------------------------
(defun splus (x y)
	(if (equal x y)
		(smult 2 x)
		(if (numberp x)
		    (if (numberp y)
		        (+ x y)    
		        (if (zerop x) 
		            y 
		            (list '+ x y)
		        )
		    )
		    (if (and (numberp y) (zerop y))
		        x
		        (list '+ x y)
		    )
		)
	)
)

;----------------------------------------
;	smult
; if both are numbers, return multipication of both
; if either of them is zero, return zerop
; if either of them is 1, return other
; else return list of multipication
;----------------------------------------
(defun smult (x y)
    (if (numberp x)
        (if (numberp y)
			(* x y)
			(if (zerop x)
				0
				(if (= x 1)
					y
					(list '* x y)
				)
			)
		)
		(if (numberp y)
			(if (zerop y)
				0
				(if (= y 1)
					x
					(list '* x y)
				)
			)
			(list '* x y)
		)
	)
)


;----------------------------------------
;	ssub
; In (- x y), if y i null, then handle as unary minus
; if both are numbers and non zero return subtraction of numbers
; if y is zero, return x
; if x is zerp return unary minus of y
; if either of them is not number, return list of subtraction
;----------------------------------------
(defun ssub (x y)
	(if (equal x y)
		0
		(if (null y)
			(- x)
			(if (numberp x)
				(if (numberp y)
					(if (zerop x)
						(- y)
						(- x y)
					)
					(if (zerop x)
						(smult -1 y)
				    	(list '- x y)
				    )
				)
				(if (numberp y) 
					(if (zerop y)
						x
						(list '- x y)
					)
					(list '- x y)
				)
			)
		)
	)
)

;----------------------------------------
;	sdiv
; in (/ x y)
; if x is zero, return zero
; if y is zero, returns error
; else if both are numbers, return division
;----------------------------------------
(defun sdiv (x y)
    (if (numberp x)
		(if (= x 0)
			0
			(if (numberp y)    
				(if (zerop y) 
					(error "error")
					(/ x y)
				)
				(list '/ x y)
			)
		)
		(if (numberp y)    
				(if (zerop y) 
					(error "error")
					(list '/ x y)
				)
				(list '/ x y)
        )
    )
)
;-----------------------------------
; PART 3
; deriv-eval
;-----------------------------------
(defun deriv-eval (expr var val)
	(evaluate (deriv expr var) var val)
)

;----------------------------------------
;	evaluate
; if expr is atom and equal to variable, return just assigned value
; if expr is atom and not a variable, return expression
; else check each for first parameter in expression and call recursivley
; on each further paramerte whether is *,+,-,/ etc and call their derivative on each 
;----------------------------------------	
	
(defun evaluate (expr var val)
        (if (atom expr)
            (if (equal expr var) 
            	val 
            	expr
            )
            (cond ((numberp expr) expr)
                ((equal(first expr) '+)							; PLUS
                    (splus 
                    	(evaluate (second expr) var val)
                    	(evaluate (third expr) var val))
                )
                ((equal (first expr) '-)						; MINUS
                    (ssub 
                    	(evaluate (second expr) var val)
                    	(evaluate (third expr) var val))
                )
                ((equal (first expr) '/)						; DIV
                    (sdiv 
                    	(evaluate (second expr) var val)
                    	(evaluate (third expr) var val))
                )
                ((equal (first expr) '*)						; MULT
                    (smult 
                    	(evaluate (second expr) var val)
                    	(evaluate (third expr) var val))
                )
                ((equal (first expr) 'expt)						; EXPT
                    (expt 
                    	(evaluate (second expr) var val)
                    	(evaluate (third expr) var val))
                )
                ((equal (first expr) 'sqrt)						; SQRT
                    (sqrt (evaluate (second expr) var val))
                )
                ((equal (first expr) 'log)						; LOG
                    (log (evaluate (second expr) var val))	
                ) 
                ((equal (first expr) 'exp)						; EXP
                    (exp (evaluate (second expr) var val))
                )
                ((equal (first expr) 'sin)						; SIN
                    (sin (evaluate (second expr) var val))
                )
                ((equal (first expr) 'cos)						; COS
                    (cos (evaluate (second expr) var val))
                )
                ((equal (first expr) 'tan)						; TAN
                    (tan (evaluate (second expr) var val))
                )
                (t
            		(error "Invalid Expression in evaluate")	; INVALID
                )
			)
        )
)

;----------------------------------
; deriv-simplify
; call simplify function which accpets inputs from deriv output
; this function returns simplified derivative
;----------------------------------
(defun deriv-simplify (expr var)
	(simplify (deriv expr var))
)

;----------------------------------
; simplify
; if expr is null, return null
; if expr is atom, return expr
; then check recursively based on the operator
;-----------------------------------
(defun 	simplify (expr)
	(cond
		((null expr) nil)
		((atom expr) expr)
		((equal (first expr) '*)							; MULTIPLY
			(cond
				((equal (second expr) 0) 0)					; if either of them is zero, return zero	
				((equal (third expr) 0) 0)
				((equal (second expr) 1) 					; if either of them is 1 return Simplify of other
					(simplify (third expr))
				)
				((equal (third expr) 1) 
					(simplify (second expr))
				)
				(t 									
					(smult									; else return simplify of each and return their multipication
						(simplify (second expr))
						(simplify (third expr))
					)
				)
			)
		)
		
		((equal (first expr) '+)							; ADDITION		
			(cond
				((null (third expr))
					(simplify (second expr))
				)
				((equal (second expr) 0) 					; if either of them is 0, return simplify of other
					(simplify (third expr))
				) 
				((equal (third expr) 0) 
					(simplify (second expr))
				)
				((equal (third expr) (second expr)) 		; if both expression are same, just multiply by 2
					(smult
						2
						(simplify (second expr))
					)
				)
				(t 
					(splus									; else return simplify of both and call splus on them
						(simplify (second expr))
						(simplify (third expr))
					)
				)
			)
		)
		((equal (first expr) '-)							; SUBTRACTION
			(cond
				((null ( third expr)) 						; Handling Unary Minus
					(smult
						-1
						(simplify (second expr))
					)
				)
			
				((equal (second expr) 0) 					; if second expr is zero, then return mult of -1 and simplify of third
					(smult
						-1
						(simplify (third expr) )
					)
				) 
				((equal (third expr) 0) 					; if third is zero, return simplify of second
					(simplify (second expr) )
				)
				((equal (third expr) (second expr)) 		; if both expression are same, return 0
					0
				)
				(t 
					(ssub									; else return ssub on simplify on each second and third expr
						(simplify (second expr) )
						(simplify (third expr) )
					)
				)
			)
		)
		((equal (first expr) '/)							; DIVISION
			(cond
				((equal (third expr) 0) 					; if third expr is zero, return undefined error
					(error "Error. Undefined !!")
				) 
				((equal (second expr) 0) 					; if second is zero, return zero
					0
				)
				((equal (third expr) 1) 					; if third is 1, return simplification of second
					(simplify (second expr))
				)
				((equal (second expr) 1) 					; if second is 1, return div of 1 and simplification of third
					(sdiv
						1
						(simplify (second expr))
					)
				)
				((equal (third expr) (second expr)) 		; if both expression are same, return 1
					1
				)
				(t 											; else return sdiv of simplification of second and simplification of third
					(sdiv
						(simplify (second expr))
						(simplify (third expr))
					)
				)
			)
		)
		((equal (first expr) 'sqrt)							; SQRT
			(if (numberp (second expr))						; Check if second expr is number, if zero returns 0 else evaluate
				(if (zerop (second expr))					; if expr has variable, returns expression
					0
					(eval expr)
				)
				expr
			)
		) 
		((equal (first expr) 'log)							; LOG
			(if (numberp (second expr))						; Check if second expr is number, if zero returns Undefined else evaluate
				(if (zerop (second expr))
					(error "Undefined !!")
					(eval expr)
				)				
				expr										; if expr has variable, returns expression
			)
		) 
		((equal (first expr) 'exp)							; EXP
			(if (numberp (second expr))						; Check if second expr is number, if zero returns 1 else evaluate
				(if (zerop (second expr))
					1
					(eval expr)
				)
				expr										; if expr has variable, returns expression
			)
		) 
		((equal (first expr) 'expt)							; EXPT
			(cond
				((equal (second expr) 0) 0)					; if second is zero, return zero	
				((equal (second expr) 1) 1)					; if either of them is 1 return Simplify of other
				((equal (third expr) 1) 
					(simplify (second expr))
				)
				((equal (third expr) 0) 1)
				(t						
					(sexpt									; else return simplify of each and return their multipication
						(simplify (second expr))
						(simplify (third expr))
					)
				)
			)
		)
		
		((equal (first expr) 'sin)							; SIN
			(if (numberp (second expr))						; Check if second expr is number, evaluate
				(eval expr)
				expr										; if expr has variable, returns expression
			)
		) 
		((equal (first expr) 'cos)							; COS
			(if (numberp (second expr))						; Check if second expr is number, evaluate
				(eval expr)	
				expr										; if expr has variable, returns expression
			)
		)
		((equal (first expr) 'tan)							; TAN
			(if (numberp (second expr))						; Check if second expr is number, evaluate
				(eval expr)
				expr										; if expr has variable, returns expression
			)
		)  
		(t 
			(error "Unknown Expression !!")
		)					
	)
)




















