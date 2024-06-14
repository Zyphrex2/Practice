{ LASTWRD4.PAS
  This program will count backwards from 20 to 0.
  For each number, it will display whether it has 1 or 2 digits.
  Compare this Pascal code to the code from other languages. }


PROGRAM My_Pascal_Program;

VAR
   K : INTEGER;  { Loop Counter }

BEGIN
   FOR K := 20 DOWNTO 0 DO BEGIN
   	IF K >= 10 THEN BEGIN
       	WRITELN(K,' is a 2-digit number.')
   	END  
   	ELSE BEGIN
       	WRITELN(K,' is a 1-digit number.')
   	END
   END	    
END.
