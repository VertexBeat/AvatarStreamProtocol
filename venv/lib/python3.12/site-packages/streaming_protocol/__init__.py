# src/streaming_protocol/__init__.py
__version__ = "0.2.0"  # Add or update this line
from streaming_protocol import DataSerializer, BaseMetadata, TimelineMetadata, AudioMetadata


__all__ = [
    'DataSerializer',
    'BaseMetadata',
    'TimelineMetadata',
    'AudioMetadata'
]