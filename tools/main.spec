# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['../main.pyw'],
             pathex=['.'],
             binaries=[],
             datas=[ ('../skins/default', 'skins/default') ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[
                'lib2to3'
             ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Yandere Sim Skin Switcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=True,
          upx=True,
          console=False,
          icon='../resources/icons/app.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Yandere Sim Skin Switcher')
