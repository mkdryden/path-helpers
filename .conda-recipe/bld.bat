@echo off
REM Construct version tag from Conda [Git environment variables][1].
REM
REM [1]: http://conda.pydata.org/docs/building/environment-vars.html#git-environment-variables
set MINOR_VERSION=%GIT_DESCRIBE_TAG:~1%
if %GIT_DESCRIBE_NUMBER%==0 (
    set PACKAGE_VERSION=%MINOR_VERSION%
) else (
    set PACKAGE_VERSION=%MINOR_VERSION%.post%GIT_DESCRIBE_NUMBER%
)

"%PYTHON%" -m pip install .
if errorlevel 1 exit 1

:: Add more build steps here, if they are necessary.
