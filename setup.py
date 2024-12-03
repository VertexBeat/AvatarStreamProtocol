from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
import os
import pybind11

# Get the absolute path to the include directory
include_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "include"))

ext_modules = [
    Extension(
        "streaming_protocol",
        sources=["src/PythonBindings.cpp"],
        include_dirs=[
            include_dir,
            pybind11.get_include(),
            pybind11.get_include(user=True),
        ],
        language="c++",
        extra_compile_args=["-std=c++17"],
    )
]

setup(
    name="streaming_protocol",
    version="0.2.0",
    author="Dominique Mowius",
    author_email="d.mowius@icloud.com",
    description="A Python-based C++ Streaming Package for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vertexbeat/AvatarStreamingProtocol",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)