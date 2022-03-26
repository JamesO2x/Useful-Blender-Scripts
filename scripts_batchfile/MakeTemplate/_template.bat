@ECHO OFF
@REM New Project Prompt
chcp 65001

echo ╔═════════════════════════════════════════════════════════════╔════════════════╗
echo ║ *                                                           ║ *            * ║
echo ║  This BATCH script Creates a new Project Folder with        ║       ██       ║
echo ║  some template files, notes, and folders within in it.      ║       ██       ║
echo ║                                                             ║       ██       ║
echo ║  Batch Script by JamesO2, 2021                              ║                ║
echo ║  https://ko-fi.com/jamesorthii                              ║       ██       ║
echo ║ *                                                           ║ *            * ║
echo ╚═════════════════════════════════════════════════════════════╚════════════════╝
echo ================================================================================
echo.

@REM ================================================================================

:program_loop
    @REM Prompt for File input
    set /p input=">>> Name of NEW Project Folder: "
    echo.

    @REM ECHO the VARS, just to verify
    echo Input:  %input%
    echo.

    xcopy "_template\*.*" "%input%" /s/h/e/k/f/c/i
    TIMEOUT 1
    rename "%cd%\%input%\untitled.blend" "%input%.blend"
    rename "%cd%\%input%\showcase_3.blend" "%input%_showcase.blend"
    rename "%cd%\%input%\REF\notes.md" "%input% Notes.md"

    @REM End the Process, and loop back to the top.
    echo.
    echo Process Complete.
    echo ================================================================================
    echo.
GOTO program_loop
