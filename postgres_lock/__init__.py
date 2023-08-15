# --------------------------------------------------------------------------------------
# Copyright (c) 2023 Sean Kerr
# --------------------------------------------------------------------------------------

"""
Lock mechanism implemented with Postgres advisory locks.
"""

from .lock import Lock

__all__ = ["Lock"]
