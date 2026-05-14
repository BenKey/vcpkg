import inspect
import os
import subprocess
import sys

from enum import Enum

type str_list = list[str]

class ExitCode(Enum):
    EX_OK = getattr(os, 'EX_OK', 0)
    EX_NOINPUT = getattr(os, 'EX_NOINPUT', 66)
    EX_UNAVAILABLE = getattr(os, 'EX_UNAVAILABLE', 69)
    EX_SOFTWARE = getattr(os, 'EX_SOFTWARE', 70)

def GetScriptFile() -> str:
    """Obtains the full path and file name of the Python script."""
    if (hasattr(GetScriptFile, "file")):
        return getattr(GetScriptFile, "file")
    ret: str = ""
    try:
        # Use abspath instead of realpath to keep subst drives
        ret = os.path.abspath(__file__)
    except NameError:
        if (len(sys.argv) > 0 and len(sys.argv[0]) > 0 and os.path.isabs(sys.argv[0])):
            ret = os.path.abspath(sys.argv[0])
        else:
            ret = os.path.abspath(inspect.getfile(GetScriptFile))
    if (not os.path.exists(ret)):
        ret = os.path.dirname(ret)
    ret = os.path.normpath(ret) 
    ret = ret.replace("\\", "/")
    setattr(GetScriptFile, "file", ret)
    return getattr(GetScriptFile, "file")

def GetScriptDirectory() -> str:
    """Obtains the path to the directory containing the script."""
    if (hasattr(GetScriptDirectory, "dir")):
        return getattr(GetScriptDirectory, "dir")
    ret: str = os.path.dirname(GetScriptFile())
    if (len(ret) == 3 and ret[1] == ":" and ret[2] == "/"):
        ret = ret[0:2]
    setattr(GetScriptDirectory, "dir", ret)
    return getattr(GetScriptDirectory, "dir")

def filter_list(unfiltered_list: str_list, excluded_list: str_list) -> str_list:
    if len(excluded_list) == 0:
        return unfiltered_list
    excluded_set = set(excluded_list)
    return [item for item in unfiltered_list if item not in excluded_set]

def IsDryRun() -> bool:
    return "--dry-run" in sys.argv

def ShouldRecurse() -> bool:
    return "--recurse" in sys.argv

def create_vcpkg_response(filename: str, packages: str_list, options: dict[str, str]) -> None:
    """Generates a vcpkg response file for classic mode."""
    with open(filename, "w", encoding="utf-8") as f:
        # Write configuration flags.
        for flag, value in options.items():
            if value:
                f.write(f"{flag}={value}\n")
            else:
                f.write(f"{flag}\n")
        # Write package list.
        for package in packages:
            f.write(f"{package}\n")


def InstallPackagesUsingResponseFile(scriptDirectory: str, responseFile: str) -> bool:
    executable_name: str = "vcpkg.exe" if os.name == "nt" else "vcpkg"
    vcpkg_executable: str = os.path.join(scriptDirectory, executable_name)
    args: str_list = [vcpkg_executable, "install", f"@{responseFile}"]
    try:
        print(f"Calling '{' '.join(args)}'.")
        subprocess.check_call(args)
        return True
    except (subprocess.CalledProcessError, OSError):
        return False

def CreateConfigObject(scriptDirectory: str, hostTriplet: str) -> dict[str, str]:
    config: dict[str, str] = {
        "--classic": "",
        "--clean-buildtrees-after-build": "",
        "--clean-packages-after-build": "",
        "--host-triplet": hostTriplet,
        "--overlay-triplets": f"{scriptDirectory}/triplets/custom",
        "--x-buildtrees-root": f"{scriptDirectory}/bt",
    }
    if ShouldRecurse():
        config["--recurse"] = ""
    return config

def ModuleMain(scriptDirectory: str, packages: str_list, hostTriplet: str, requiredOS: str = "") -> int:
    config: dict[str, str] = CreateConfigObject(scriptDirectory, hostTriplet)
    responseFile: str = f"{scriptDirectory}/vcpkg_response.txt"
    create_vcpkg_response(responseFile, packages, config)
    if (not os.path.exists(responseFile)):
        print(f"Error: Response file '{responseFile}' does not exist.")
        return ExitCode.EX_NOINPUT.value
    if (IsDryRun()):
        print(f"Dry run: vcpkg response file created at '{responseFile}'.")
        return ExitCode.EX_OK.value
    if (requiredOS and os.name != requiredOS):
        print(f"Only dry run is supported on this platform.")
        return ExitCode.EX_UNAVAILABLE.value
    if (InstallPackagesUsingResponseFile(scriptDirectory, responseFile)):
        print("Packages installed successfully.")
        return ExitCode.EX_OK.value
    else:
        print("Failed to install packages.")
        return ExitCode.EX_SOFTWARE.value
