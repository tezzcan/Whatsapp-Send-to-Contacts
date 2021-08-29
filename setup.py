from setuptools import setup

setup(
    name="wsa",
    version="1.0",
    description="A module for automating Whatsapp messages",
    author="Oğuzhan Tezcan",
    author_email="oguzhantezcann@gmail.com",
    packages=["wsa"],
    install_requires=["numpy", "pytest", "pandas", "pyautogui"],
)
