"""Xiaomi MiMo provider profile."""

from typing import Any

from providers import register_provider
from providers.base import ProviderProfile


class XiaomiProfile(ProviderProfile):
    """Xiaomi MiMo — extra_body.thinking + top-level reasoning_effort."""

    def build_api_kwargs_extras(
        self, *, reasoning_config: dict | None = None, **context
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        extra_body = {}
        top_level = {}

        if not reasoning_config or not isinstance(reasoning_config, dict):
            extra_body["thinking"] = {"type": "enabled"}
            top_level["reasoning_effort"] = "medium"
            return extra_body, top_level

        enabled = reasoning_config.get("enabled", True)
        if enabled is False:
            extra_body["thinking"] = {"type": "disabled"}
            return extra_body, top_level

        extra_body["thinking"] = {"type": "enabled"}
        effort = (reasoning_config.get("effort") or "").strip().lower()
        if effort in ("low", "medium", "high"):
            top_level["reasoning_effort"] = effort
        else:
            top_level["reasoning_effort"] = "medium"

        return extra_body, top_level


xiaomi = XiaomiProfile(
    name="xiaomi",
    aliases=("mimo", "xiaomi-mimo"),
    env_vars=("XIAOMI_API_KEY",),
    base_url="https://api.xiaomimimo.com/v1",
)

register_provider(xiaomi)
