from hydra import initialize_config_dir, compose
from omegaconf import OmegaConf
from omegaconf.errors import InterpolationToMissingValueError
from pathlib import Path


def compose_config(config_dir: str | Path, config_name: str = "config") -> OmegaConf:
    """Compose a Hydra config from a config directory and config name."""
    config_dir = Path(config_dir).resolve()
    with initialize_config_dir(config_dir=str(config_dir), version_base=None):
        cfg = compose(config_name=config_name)
    return cfg

def load_config(config_dir: str | Path, config_name: str = "config", allow_missing: bool = True) -> dict:
    """Load and fully resolve a Hydra config into a plain Python dict.

    Interpolations that point to missing (???) values are replaced by '???'
    instead of raising InterpolationToMissingValueError.
    """
    config_dir = Path(config_dir).resolve()
    with initialize_config_dir(config_dir=str(config_dir), version_base=None):
        cfg = compose(config_name=config_name)
        if allow_missing:
            return _safe_resolve_with_missing(cfg)
        else:
            return OmegaConf.to_container(cfg, resolve=True)

def _safe_resolve_with_missing(cfg):
    """Resolve a config, replacing unresolvable interpolations with '???'."""
    def replace_unresolvable(obj):
        if isinstance(obj, dict):
            return {k: replace_unresolvable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [replace_unresolvable(v) for v in obj]
        elif isinstance(obj, str):
            # Replace explicit ??? or interpolations referencing ??? with ???
            if obj == "???" or obj.startswith("${"):
                return "???"
            return obj
        else:
            return obj

    try:
        return OmegaConf.to_container(cfg, resolve=True)
    except InterpolationToMissingValueError:
        partial = OmegaConf.to_container(cfg, resolve=False)
        return replace_unresolvable(partial)
    


