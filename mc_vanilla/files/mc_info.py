#!/usr/bin/env python3

import dataclasses
import json
import urllib
import urllib.error
import urllib.request
import sys


@dataclasses.dataclass
class ManifestV2Data:
    """Version number (e.g. 1.20)"""
    ID: str
    """Type of update (release, snapshot, etc.)"""
    Type: str
    """URL of Version-JSON data"""
    URL: str


@dataclasses.dataclass
class VersionData:
    DownloadURLClient: str
    DownloadURLServer: str


def get_manifest(version: str) -> ManifestV2Data:
    url = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
    headers = {"Content-Type": "application/json"}

    req = urllib.request.Request(url=url, headers=headers)

    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            RetJSON = json.loads(response.read())

            if "latest" in RetJSON and "versions" in RetJSON:
                ReleaseVersion = RetJSON["latest"]["release"]

                if version != "latest":
                    ReleaseVersion = version

                VersionsData = RetJSON["versions"]
                LatestVersionData = ManifestV2Data

                for Version in VersionsData:
                    if Version["id"] == ReleaseVersion:
                        LatestVersionData.ID = Version["id"]
                        LatestVersionData.Type = Version["type"]
                        LatestVersionData.URL = Version["url"]

                        return LatestVersionData

                raise KeyError("Error - Version not found!")

        else:
            raise urllib.error.HTTPError(
                url=url,
                code=response.status,
                msg="Error while trying to retrieve web-resource",
            )


def parse_manifest(version_manifest: ManifestV2Data) -> VersionData:
    url = version_manifest.URL
    headers = {"Content-Type": "application/json"}

    req = urllib.request.Request(url=url, headers=headers)

    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            RetJSON = json.loads(response.read())

            ParsedData = VersionData(
                DownloadURLClient=RetJSON["downloads"]["client"]["url"],
                DownloadURLServer=RetJSON["downloads"]["server"]["url"],
            )

            return ParsedData

        else:
            raise urllib.error.HTTPError(
                url=url,
                code=response.status,
                msg="Error on requesting version manifest data!",
            )


def get_latest_version() -> str:
    Manifest = get_manifest("latest")
    
    return Manifest.ID


if __name__ == "__main__":
    def general_usage():
        print(f"Modes available:\n\t{sys.argv[0]} url\n\t{sys.argv[0]} version")

    def usage_version():
        print(f"\nWarning! Using {sys.argv[0]} with 'version' takes no arguments!\n")

    def usage_url():
        print(
            f"Usage: {sys.argv[0]} url FILE {{server|client}} [VERSION {{latest|VERSION}}]\n"
        )
        print("\tFILE")
        print("\t\t- File to request; either 'server' or 'client'")
        print("\t[VERSION] - optional")
        print(
            "\t\t- version to request; use 'latest' or a specific version (e.g.: 1.20.6)"
        )
        print("\t\t- defaults to: latest")


    PossibleArgv = [2, 3, 4]
    argc = len(sys.argv)

    if argc not in PossibleArgv:
        general_usage()
        exit(0)

    if sys.argv[1] == "version":
        if argc != 2:
            usage_version()

        VersionLatest = get_latest_version()
        print(f"{VersionLatest}")
        exit(0)

    elif sys.argv[1] == "url":
        if argc not in [3, 4]:
            usage_url()
            exit(0)

        Version = "latest"
        if argc == 4:
            Version = sys.argv[3]

        FileType = sys.argv[2]

        ManifestData = get_manifest(version=Version)
        ParsedData = parse_manifest(ManifestData)

        if FileType in ["server", "client"]:
            if FileType == "server":
                print(ParsedData.DownloadURLServer)

            else:
                print(ParsedData.DownloadURLClient)

        else:
            raise KeyError(f"Wrong file type '{FileType}'! Use 'server' or 'client' only.")  

    else:
        general_usage()
        exit(0)
