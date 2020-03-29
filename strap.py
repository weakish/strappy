import shutil
import subprocess


def apt(name: str) -> None:
    subprocess.run(['apt', 'install', '-y', '-q', name], check=True)


def pkg_install(name: str) -> None:
    # assuming debian
    apt(name)


def pkg(*names: str) -> None:
    for name in names:
        if shutil.which(name) == None:
            pkg_install(name)
