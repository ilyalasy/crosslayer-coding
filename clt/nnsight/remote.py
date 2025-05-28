from nnsight import CONFIG
from nnsight.intervention.backends import RemoteBackend
from dataclasses import dataclass
import os


@dataclass
class RemoteConfig:
    """Configuration for remote backend."""

    host: str | None = None
    ssl: bool | None = None
    api_key: str | None = None


def create_remote_backend(model_name: str, config: RemoteConfig | None = None):
    if config is None:
        config = RemoteConfig()
    backend = RemoteBackend(
        model_name,
        host=config.host or os.getenv("NNSIGHT_API_HOST", CONFIG.API.HOST),
        ssl=config.ssl or os.getenv("NNSIGHT_API_SSL", CONFIG.API.SSL),
        api_key=config.api_key or os.getenv("NNSIGHT_API_KEY", CONFIG.API.APIKEY),
        blocking=True,
    )
    return backend
