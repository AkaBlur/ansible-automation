import argparse
import dataclasses
import json
import urllib
import urllib.error
import urllib.request


@dataclasses.dataclass
class MinecraftPaperInfo:
    DownloadURL: str
    Version: str
    Build: int


_ApiBaseURL = "https://api.papermc.io/v2/projects"
_ApiEndPaper = "paper"
_ApiEndVersions = "versions"
_ApiEndBuilds = "builds"
_ApiEndDownloads = "downloads"


def json_check_return_entries(Entries: list[str], CheckDict):
    # some safeguard features
    for key in Entries:
        if key not in CheckDict:
            raise KeyError("API return not according to standard! Aborting...")


def json_fetcher(URL: str):
    """
    Request JSON data from an API endpoint.\n
    Decodes the return value and returns a JSON dict.
    """
    Headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0",
    }

    Req = urllib.request.Request(url=URL, headers=Headers)

    try:
        with urllib.request.urlopen(Req) as Ret:
            if Ret.code == 200:
                try:
                    JSONReply = json.loads(Ret.read().decode("utf-8"))

                    return JSONReply

                except json.JSONDecodeError as jsonE:
                    print("Error while decoding JSON from PaperMC API!")
                    print(jsonE)

            else:
                print(f"Something went wrong!\nReturn Code: {Ret.code}")

    except urllib.error.HTTPError as e:
        print("Error on requesting PaperMC backend!")
        print(e)


def get_minecraft_paper_versions():
    """Returns a dictionary for all available PaperMC versions"""
    AvailableVersions = json_fetcher(_ApiBaseURL + "/" + _ApiEndPaper)
    Entries = ["project_id", "project_name", "version_groups", "versions"]

    json_check_return_entries(Entries=Entries, CheckDict=AvailableVersions)

    if (AvailableVersions["project_id"].lower() != "paper") or (
        AvailableVersions["project_name"].lower() != "paper"
    ):
        raise ValueError("API not according to standard! Aborting...")

    Versions = AvailableVersions["versions"]

    return Versions


def get_minecraft_paper_builds(Version: str):
    """Returns a dictionary for all available PaperMC builds for a given version"""
    AvailableBuilds = json_fetcher(
        _ApiBaseURL + "/" + _ApiEndPaper + "/" + _ApiEndVersions + "/" + Version
    )
    Entries = ["project_id", "project_name", "version", "builds"]

    json_check_return_entries(Entries=Entries, CheckDict=AvailableBuilds)

    if (AvailableBuilds["project_id"].lower() != "paper") or (
        AvailableBuilds["project_name"].lower() != "paper"
    ):
        raise ValueError("API not according to standard! Aborting...")

    if AvailableBuilds["version"] != Version:
        raise ValueError("API not according to standard! Aborting...")

    Builds = AvailableBuilds["builds"]

    return Builds


def get_minecraft_paper_download_info(Version: str, Build: str) -> MinecraftPaperInfo:
    """Returns information about a specific PaperMC version and build with download URL"""
    PaperInfo = json_fetcher(
        _ApiBaseURL
        + "/"
        + _ApiEndPaper
        + "/"
        + _ApiEndVersions
        + "/"
        + Version
        + "/"
        + _ApiEndBuilds
        + "/"
        + Build
    )
    Entries = ["project_id", "project_name", "version", "build", "downloads"]
    json_check_return_entries(Entries=Entries, CheckDict=PaperInfo)

    Downloads = PaperInfo["downloads"]
    EntriesDownload = ["application"]
    json_check_return_entries(Entries=EntriesDownload, CheckDict=Downloads)

    DownloadApp = Downloads["application"]
    EntriesApplication = ["name", "sha256"]
    json_check_return_entries(Entries=EntriesApplication, CheckDict=DownloadApp)

    if (PaperInfo["project_id"].lower() != "paper") or (
        PaperInfo["project_name"].lower() != "paper"
    ):
        raise ValueError("API not according to standard! Aborting...")

    if PaperInfo["version"] != Version:
        raise ValueError("API not according to standard! Aborting...")

    if str(PaperInfo["build"]) != Build:
        raise ValueError("API not according to standard! Aborting...")

    AppName = DownloadApp["name"]
    DownloadURL = (
        _ApiBaseURL
        + "/"
        + _ApiEndPaper
        + "/"
        + _ApiEndVersions
        + "/"
        + Version
        + "/"
        + _ApiEndBuilds
        + "/"
        + Build
        + "/"
        + _ApiEndDownloads
        + "/"
        + AppName
    )

    VersionPaperInfo = MinecraftPaperInfo(
        DownloadURL=DownloadURL, Version=PaperInfo["version"], Build=PaperInfo["build"]
    )

    return VersionPaperInfo


def get_minecraft_paper(
    Version: str = "latest", Build: str = "latest"
) -> MinecraftPaperInfo:
    """Returns the requested PaperMC info data for a given version and build string"""
    Versions = get_minecraft_paper_versions()
    FetchVersion = ""

    if Version == "latest":
        # latest version should always be the last entry
        FetchVersion = str(Versions[-1])

    else:
        FetchVersion = str(Version)

    Builds = get_minecraft_paper_builds(Version=FetchVersion)
    FetchBuild = ""

    if Build == "latest":
        # latest build should always be the last entry
        FetchBuild = str(Builds[-1])

    else:
        FetchBuild = str(Build)

    PaperVersionInfo = get_minecraft_paper_download_info(FetchVersion, FetchBuild)

    return PaperVersionInfo


if __name__ == "__main__":
    ArgParser = argparse.ArgumentParser(
        description="Get the download URL for the PaperMC server file"
    )
    ArgParser.add_argument(
        "--version",
        default="latest",
        help="Version string for the PaperMC server (e.g. '1.20.1')",
    )
    ArgParser.add_argument(
        "--build",
        default="latest",
        help="Build version for the PaperMC server (e.g. '60')",
    )

    Args = ArgParser.parse_args()

    PaperInfo = get_minecraft_paper(Version=Args.version, Build=Args.build)
    print(PaperInfo.DownloadURL)
    print(PaperInfo.Version)
    print(PaperInfo.Build)
