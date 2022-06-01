"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['agdx-roadmap.live.py']
DATA_FILES = ["sounds", "data"]
OPTIONS = {
    'includes': ['PyQt6._qt', 'playsound', "sip"]
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)