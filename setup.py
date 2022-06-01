"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['agdx-roadmap.live.py']
DATA_FILES = ["icon.icns", "sounds"]
OPTIONS = {
    'includes': ['PyQt6._qt', 'playsound', "sip"],
    'iconfile':'icon.icns',
    'plist': {'CFBundleShortVersionString':'0.1.0',}
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
