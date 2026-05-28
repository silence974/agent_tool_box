import re

from agent_tool_box import __version__


def test_version_is_semver_like() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+", __version__)
