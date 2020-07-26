from cx_Freeze import setup, Executable
import os
import sys

# hack to import parent module(s)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path = [parent_dir] + sys.path

def qt5_plugins_dir():
    from PySide2.QtCore import QCoreApplication
    app = QCoreApplication([])
    try:
        return app.libraryPaths()[0]
    except (IndexError, TypeError):
        sys.exit("Can't find qt5 plugins directory")
    finally:
        app.quit()

plugins_dir = qt5_plugins_dir()


# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = ['appdirs', 'pkg_resources._vendor'],
    zip_include_packages = [ 'PySide2', 'shiboken2'], #, 'ui', 'qtmodern' ],
    includes = [
        'PySide2.QtCore', 'PySide2.QtWidgets', 'PySide2.QtGui',
        'PySide2.QtWebSockets', 'PySide2.QtNetwork', 'PySide2.QtMultimedia',
        'PySide2.QtWinExtras', 'sys', 'json', 'datetime', 'math', 'logging',
        'imp', 'six'
    ],
    excludes = [
        'unittest', 'pydoc_data', 'pyside2uic',
        'html', 'http',
        # too far?
        '_hashlib', 'unicodedata', '_lzma', '_bz2'
    ],
    include_files = [
        (os.path.join(plugins_dir, 'imageformats/qico.dll'), 'imageformats/qico.dll'),
        (os.path.join(plugins_dir, 'platforms/qwindows.dll'), 'platforms/qwindows.dll'),
        (os.path.join(plugins_dir, 'styles/qwindowsvistastyle.dll'), 'styles/qwindowsvistastyle.dll'),
        #(os.path.join(plugins_dir, 'audio/qtaudio_windows.dll'), 'audio/qtaudio_windows.dll')
    ],
    bin_path_excludes = [
        'C:/Program Files/Java/'
    ]
)

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable(
        os.path.join(parent_dir, 'main.py'),
        base=base,
        icon=os.path.join(parent_dir, 'resources/icons/app.ico')
    )
]

setup(name='Yandere Sim Skin Switcher',
      version = '1.0',
      description = 'Yandere Sim Skin Switcher',
      options = dict(build_exe = buildOptions),
      executables = executables, requires=['PySide2']
      )
