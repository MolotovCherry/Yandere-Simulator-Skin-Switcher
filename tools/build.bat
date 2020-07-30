@echo off

rem python setup.py build_exe
pyinstaller --clean --distpath=dist main.spec

cd dist/Yandere Sim Skin Switcher

setlocal enabledelayedexpansion
set files[0]=Qt5DBus.dll
set files[1]=Qt5Pdf.dll
set files[2]=Qt5QmlModels.dll
set files[3]=Qt5Quick.dll
set files[4]=Qt5Svg.dll
set files[5]=Qt5VirtualKeyboard.dll
set files[6]=Qt5WebSockets.dll
set files[7]=Include
set files[8]=PySide2\qt.conf
set files[9]=PySide2\translations
set files[10]=PySide2\plugins\platforms\qminimal.dll
set files[11]=PySide2\plugins\platforms\qoffscreen.dll
set files[12]=PySide2\plugins\platforms\qwebgl.dll
set files[13]=PySide2\plugins\bearer
set files[14]=PySide2\plugins\platformthemes
set files[15]=PySide2\plugins\platforminputcontexts
set files[16]=PySide2\plugins\iconengines
set files[17]=PySide2\plugins\imageformats\qgif.dll
set files[18]=PySide2\plugins\imageformats\qicns.dll
set files[19]=PySide2\plugins\imageformats\qjpeg.dll
set files[20]=PySide2\plugins\imageformats\qpdf.dll
set files[21]=PySide2\plugins\imageformats\qsvg.dll
set files[22]=PySide2\plugins\imageformats\qtga.dll
set files[23]=PySide2\plugins\imageformats\qtiff.dll
set files[24]=PySide2\plugins\imageformats\qwbmp.dll
set files[25]=PySide2\plugins\imageformats\qwebp.dll

for /l %%n in (0,1,25) do ( 
   DEL /F /Q /S !files[%%n]!
)

cd ..
cd ..