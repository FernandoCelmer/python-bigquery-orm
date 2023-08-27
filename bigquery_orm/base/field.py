from typing import Dict, Any


class BaseField:

    def __init__(
        self,
        name: str,
        field_type: str,
        mode: str,
        description: str,
        max_length: int
    ) -> None:
        self.properties: Dict[str, Any] = {
            "name": name,
            "type": field_type,
            "mode": mode,
            "description": description,
            "max_length": max_length
        }
