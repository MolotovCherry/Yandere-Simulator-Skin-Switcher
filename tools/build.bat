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
set files[26]=d3dcompiler_47.dll
set files[27]=libcrypto-1_1.dll
set files[28]=libEGL.dll
set files[29]=libGLESv2.dll
set files[30]=libssl-1_1.dll
set files[31]=opengl32sw.dll
set files[32]=_asyncio.pyd
set files[33]=_bz2.pyd
set files[34]=_decimal.pyd
set files[35]=_elementtree.pyd
set files[36]=_hashlib.pyd
set files[37]=_lzma.pyd
set files[38]=_overlapped.pyd
set files[39]=_queue.pyd
set files[40]=_ssl.pyd
set files[41]=_testcapi.pyd
set files[42]=_pyexpat.pyd

for /l %%n in (0,1,42) do ( 
   DEL /F /Q /S !files[%%n]!
   RMDIR /Q /S !files[%%n]!
)

cd ..
cd ..