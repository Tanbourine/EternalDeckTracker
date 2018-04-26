# -*- mode: python -*-

block_cipher = None


a = Analysis(['EternalDeckTracker.py'],
             pathex=['/Users/dtan/gitRepos/EternalDeckTracker'],
             binaries=[],
             datas=[('deck.csv', '.'), ('clienticon.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='EternalDeckTracker',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='clienticon.ico')
app = BUNDLE(exe,
             name='EternalDeckTracker.app',
             icon='clienticon.ico',
             bundle_identifier=None)