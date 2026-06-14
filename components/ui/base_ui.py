"""Base UI component."""

from .component import CoreComponent

PACKAGE_NAME = "@base-ui/react"
PACKAGE_VERSION = "1.5.0"


class BaseUIComponent(CoreComponent):
    """Base UI component."""

    lib_dependencies: list[str] = [f"{PACKAGE_NAME}@{PACKAGE_VERSION}"]
