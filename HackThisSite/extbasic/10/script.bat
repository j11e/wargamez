
@ECHO OFF

SETLOCAL ENABLEDELAYEDEXPANSION

SET PRIME=2  3  5  7  11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101
SET CHARS=a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s t  u  v  w  x  y  z
SET PASSWORDVALUE=1
SET INPUT=
SET /P INPUT=Insert password:

REM empty input: call the script again
IF "%INPUT%"=="" "%~0"

ECHO Authenticating...
ECHO "Your input is %INPUT% ; your password is %PASSWORDVALUE%"

:OVERLOOP
    SET CURRENTPOSITION=0

    :SUBLOOP
        REM caseinsens if CHARPOSth char from input == CURPOSth char from list,  PASSVAL *= PRIME[CURPOS]
        IF /I "!INPUT:~%CHARACTERPOSITION%,1!"=="!CHARS:~%CURRENTPOSITION%,1!" SET /A PASSWORDVALUE*=!PRIME:~%CURRENTPOSITION%,3!

        REM CURPOS += 3
        SET /A CURRENTPOSITION+=3

		REM while CURPOS != 78        
	    IF NOT %CURRENTPOSITION%==78 GOTO :SUBLOOP

    REM CHARPOS++
    SET /A CHARACTERPOSITION+=1

    REM while CHARPOS < INPUT.length
    IF NOT "!INPUT:~%CHARACTERPOSITION%,1!"=="" GOTO :OVERLOOP
:END

ENDLOCAL & IF NOT %PASSWORDVALUE%==1065435274 GOTO :ACCESSDENIED

ECHO You have been authenticated. Welcome aboard!

GOTO :SILENTPAUSE

:ACCESSDENIED
ECHO "Access denied with pwd = %PASSWORDVALUE%!"

:SILENTPAUSE
PAUSE > NUL


2147483647 * i + 1065435274

decompose ^

in all factors <= 101