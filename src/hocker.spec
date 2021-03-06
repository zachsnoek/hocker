# -*- mode: python -*-

block_cipher = None

added_files = [
	( 'hocker-run.py', 'src' ),
	( 'hocker-images.py', 'src' ),
	( 'hockernode.py', 'src' ),
    ( 'hockerslurm.py', 'src' ),
    ( 'hockerrun.py', 'src' ),
	]

a = Analysis(['hocker.py'],
             pathex=['/root/hocker/src'],
             binaries=[],
             datas= added_files,
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
          exclude_binaries=True,
          name='hocker',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='hocker1.0')
