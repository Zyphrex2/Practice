100 REM LASTWORD05.BAS
110 REM This program will count backwards from 20 to 0.
120 REM For each number, it will display whether it has
130 REM 1 or 2 digits. Compare this BASIC code to the 
140 REM code from other languages.
150 REM
160 REM
170 FOR K = 20 TO 0 STEP -1
180 PRINT K;
190 IF K >= 10 THEN PRINT " is a 2-digit number. " ELSE PRINT " is a 1-digit number."
200 NEXT K
