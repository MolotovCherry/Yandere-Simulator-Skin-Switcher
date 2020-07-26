@echo off

for %%f in (..\resources\*.qrc) do (
 echo converting %%~nf.qrc
 pyside2-rcc -o ..\resources\%%~nf_rc.py %%f
)

for %%f in (..\qtmodern\resources\*.qrc) do (
 echo converting %%~nf.qrc
 pyside2-rcc -o ..\qtmodern\resources\%%~nf_rc.py %%f
)
