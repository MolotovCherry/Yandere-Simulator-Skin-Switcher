@echo off

for %%f in (..\ui\designer\*.ui) do (
 echo converting %%~nf.ui
 pyside2-uic -o "..\ui\%%~nf.py" "%%f"
 rem i can't believe there's no --import-from option!!
 bin\sed -i "s/import resources_rc/from resources import resources_rc/g" "..\ui\%%~nf.py"
)

rem remove yucky sed(*&#)(* files :(
for %%f in (.\sed*) do (
    del %%f
)
