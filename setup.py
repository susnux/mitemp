"""Python package description."""
from setuptools import setup, find_packages

setup(
    name="mitemp_bt",
    version="0.0.5",
    description="Library to read data from Mi Temperature and Humidity Sensor (V2) using Bluetooth LE with LCD display",
    url="https://github.com/ratcashdev/mitemp",
    author="ratcashdev",
    author_email="developer@ratcash.net",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.4",
    packages=find_packages(exclude=["test.*", "test"]),
    install_requires=["btlewrap>=0.0.8", "cryptography"],
    keywords="temperature and humidity sensor bluetooth low-energy ble",
    zip_safe=False,
    extras_require={"testing": ["pytest"]},
)
