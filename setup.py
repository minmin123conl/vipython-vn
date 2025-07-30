"""
Setup script cho ViPython-VN
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="vipython-vn",
    version="0.1.0",
    author="ViPython Team",
    author_email="team@vipython.vn",
    description="Ngôn ngữ lập trình ViPython-VN - phiên bản Việt hoá không dấu theo phong cách Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vipython-team/vipython-vn",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Software Development :: Interpreters",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "vipython=vipython.__main__:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

