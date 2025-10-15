from PyInstaller.building.build_main import Analysis, PYZ, EXE
from PyInstaller.utils.hooks import collect_all, collect_data_files, collect_submodules
import os

app_name = "AgendaRadicador"

def add_pkg(all_datas, all_binaries, all_hidden, pkg):
    try:
        datas, bins, hidden = collect_all(pkg)
        all_datas += datas
        all_binaries += bins
        all_hidden += hidden
    except Exception:
        all_datas += collect_data_files(pkg, include_py_files=True)
        all_hidden += collect_submodules(pkg)

datas = []
binaries = []
hidden = []

for pkg in [
    "streamlit","st_aggrid","pandas","numpy","openpyxl","requests",
    "altair","tzdata","charset_normalizer","idna","urllib3","certifi",
]:
    add_pkg(datas, binaries, hidden, pkg)

datas += [(os.path.abspath("app.py"), ".")]
if os.path.exists("README.txt"):
    datas += [(os.path.abspath("README.txt"), ".")]

hidden += [
    "streamlit.web.cli",
    "streamlit.runtime",
    "streamlit.web.bootstrap",
]

a = Analysis(
    ["run_app.py"],
    pathex=["."],
    binaries=binaries,
    datas=datas,
    hiddenimports=hidden,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name=app_name,
    console=False,
    icon=None,
    upx=False,
)
