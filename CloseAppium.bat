@echooff

titlestopAppiumServer
tasklist /V|find "startAppiumServer">nul

if %errorlevel% ==0(

::�ر�appium����
taskkill /F /IM node.exe

taskkill /F /FI "WINDOWTITL Eeq startAppiumServer"

)

taskkill /F /FI "WINDOWTITL Eeq stopAppiumServer"	