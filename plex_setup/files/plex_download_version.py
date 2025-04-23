import argparse
import json
from typing import Any
import urllib
import urllib.request

__ApiPlexDownloads = "https://plex.tv/api/downloads/5.json"


def get_info_json() -> dict[Any]:
    """GET all download information from Plex download API for server packages.

    Raises:
        RuntimeError: Malformed API return
        ConnectionError: Non-200 return code from API

    Returns:
        dict[Any]: JSON dictionary answer
    """
    Headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0",
    }

    Req = urllib.request.Request(__ApiPlexDownloads, headers=Headers)

    with urllib.request.urlopen(Req) as SiteConn:
        if SiteConn.code == 200:
            try:
                JSONRep = json.loads(SiteConn.read().decode("utf-8"))
                return JSONRep

            except json.JSONDecodeError as JSONError:
                print(JSONError)
                raise RuntimeError("Error while parsing API response!")

        else:
            raise ConnectionError(f"API returned error return code: {SiteConn.code}")


def parse_api_json(
    jsonDict: dict[Any], platform: str, arch: str, distro: str = None
) -> str:
    """Parse the JSON object from Plex download API for a resulting download
    URL. Must result in a distinct singular URL.

    System, build architecture and optional distribution for system may be set.

    Args:
        jsonDict (dict[Any]): Input JSON API object
        platform (str): Platform to select
        arch (str): Build architecture
        distro (str, optional): Distribution to choose from. Defaults to None.

    Raises:
        KeyError: Malformed API JSON object
        ValueError: Multiple download options detected

    Returns:
        str: Download URL for Plex server package
    """
    if "computer" not in jsonDict:
        raise KeyError("No platforms for computer found inside Plex downloads!")

    if platform not in jsonDict["computer"]:
        raise KeyError(f"Platform {platform} not in Plex downloads!")

    if "releases" not in jsonDict["computer"][platform]:
        raise KeyError("Malformed API return!")

    PlatformReleases = jsonDict["computer"][platform]["releases"]
    ApplicableReleases = []

    for Release in PlatformReleases:
        ReleaseBuildArch = Release["build"].split("-")[1:]
        ReleaseBuildArch = ("-").join(ReleaseBuildArch)

        if "distro" in Release and distro is not None:
            if ReleaseBuildArch == arch and Release["distro"] == distro:
                ApplicableReleases.append(Release)

        else:
            if ReleaseBuildArch == arch:
                ApplicableReleases.append(Release)

    if len(ApplicableReleases) > 1:
        print("Applicable distributions:")
        for Release in ApplicableReleases:
            print(Release["distro"])

        raise ValueError(
            "Multiple releases inside result! Not applicable for filtering"
        )

    return ApplicableReleases[0]["url"]


if __name__ == "__main__":
    ArgParser = argparse.ArgumentParser(
        description="Get download URL for specific version of Plex Media Server"
    )
    ArgParser.add_argument(
        "--platform", default="Linux", help="Platform to select latest version from"
    )
    ArgParser.add_argument(
        "--arch", default="x86_64", help="Platform architecture (if supplied)"
    )
    ArgParser.add_argument(
        "--distro", help="Optional distribution for chosen system. May be omitted."
    )

    Args = ArgParser.parse_args()

    ApiJSON = get_info_json()

    Distro = Args.distro
    if Distro is None or Distro == "":
        Distro = None

    print(parse_api_json(ApiJSON, Args.platform, Args.arch, Distro))
