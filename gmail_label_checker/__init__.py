"""
Gmail Label Checker

A Python package for checking, creating, and deleting Gmail labels using OAuth2 authentication.
"""

from .core import get_gmail_service, check_label_exists, create_label, delete_label

__version__ = '0.1.0'
__all__ = ['get_gmail_service', 'check_label_exists', 'create_label', 'delete_label']
