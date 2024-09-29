#!/usr/bin/env python3

import dataclasses
import json
import re
import urllib
import urllib.request


@dataclasses.dataclass
class Settings:
    EmbyReleaseURL: str
    EmbyReleaseAssetStr: str


def get_emby_release(SessionSettings: Settings):
    Headers = {
        "Content-Type": "application/json"
    }

    Request = urllib.request.Request(SessionSettings.EmbyReleaseURL, headers = Headers)

    with urllib.request.urlopen(Request) as Response:
        if Response.status == 200:
            RespJSON = json.loads(Response.read())

            for ReleaseVer in RespJSON:
                if not ReleaseVer["draft"] and not ReleaseVer["prerelease"]:
                    Assets = ReleaseVer["assets"]
                    LatestVersionFound = False

                    for Asset in Assets:
                        VersionAsset = Asset["name"]

                        VersionPattern = re.compile(SessionSettings.EmbyReleaseAssetStr)
                        ReSearch = re.search(VersionPattern, VersionAsset)

                        if ReSearch is not None:
                            print(f"{Asset['browser_download_url']}")
                            LatestVersionFound = True
                            break

                    if not LatestVersionFound:
                        print("[WARNING] - No suitable file found for latest version")

                    break

        else:
            raise urllib.error.HTTPError(
                url=SessionSettings.EmbyReleaseURL,
                code=Response.status,
                msg="Error while trying to retrieve web-resource",
            )


if __name__ == "__main__":
    MySettings = Settings(
        EmbyReleaseURL = "https://api.github.com/repos/MediaBrowser/Emby.Releases/releases",
        EmbyReleaseAssetStr = r"emby-server-deb_.*\.deb"
    )

    get_emby_release(MySettings)