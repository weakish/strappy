import shutil
import subprocess
from typing import Optional, Sequence, TypedDict, Union


def test(args: Union[str, Sequence[str]]) -> bool:
    if subprocess.run(args).returncode == 0:
        return True
    else:
        return False


class PKGOptions(TypedDict, total=False):
    ppa: str


def apt_add_repository(repo: str) -> None:
    subprocess.run(['add-apt-repository', '--yes', repo], check=True)


def apt(name: str, options: PKGOptions = {}) -> None:
    if 'ppa' in options:
        apt_add_repository(f'ppa:{options["ppa"]}')
    subprocess.run(['apt', 'install', '--yes', '--quiet', name], check=True)


def pkg_install(name: str, options: PKGOptions = {}) -> None:
    # assuming debian
    apt(name, options)


def pkg(name: str, executable_name: Optional[str] = None, options: PKGOptions = {}) -> None:
    '''Install a package.'''
    if shutil.which(name if executable_name == None else executable_name) == None:
        pkg_install(name, options)