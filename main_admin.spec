# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main_admin.py'],
    pathex=[],
    binaries=[],
    datas=[('imagenesApp/user-graduateprueba3.png', 'imagenesApp'), ('imagenesApp/boton-busqueda-alumno.png', 'imagenesApp'), ('imagenesApp/boton-busqueda-materia.png', 'imagenesApp'), ('imagenesApp/boton-busqueda-profesor.png', 'imagenesApp'), ('imagenesApp/user-tie2.png', 'imagenesApp'), ('imagenesApp/bookprueba.png', 'imagenesApp')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main_admin',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
