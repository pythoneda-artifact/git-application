"""
pythoneda/artifact/git/application/git_artifact_app.py

This file can be used to run Git artifact.

Copyright (C) 2023-today rydnr's pythoneda-artifact/git-application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.application import PythonEDA

class GitArtifactApp(PythonEDA):
    """
    Runs the domain of Git artifacts.

    Class name: GitArtifactApp

    Responsibilities:
        - Runs the domain of Git artifacts.

    Collaborators:
        - None
    """
    def __init__(self):
        """
        Creates a new GitArtifactApp instance.
        """
        # git_artifact_banner is automatically generated by pythoneda-artifact/git-application-artifact
        banner = None
        try:
            from pythoneda.artifact.git.application.git_artifact_banner import GitArtifactBanner
            banner = GitArtifactBanner()
        except ImportError:
            pass
        from pythoneda.artifact.git import import GitArtifact
        super().__init__(banner, __file__)

if __name__ == "__main__":
    asyncio.run(GitArtifactApp.main())
