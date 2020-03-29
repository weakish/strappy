import shutil
import subprocess
from typing import Optional


def apt(name: str) -> None:
    subprocess.run(['apt', 'install', '--yes', '--quite', name], check=True)


def pkg_install(name: str) -> None:
    # assuming debian
    apt(name)


def apt_add_repository(repo: str) -> None:
    subprocess.run(['add-apt-repository', '--yes', repo], check=True)


def pkg(name: str, executable_name: Optional[str] = None, ppa: Optional[str] = None) -> None:
    if shutil.which(name if executable_name == None else executable_name) == None:
        if ppa != None:
            apt_add_repository(f'ppa:{ppa}')
        pkg_install(name)            