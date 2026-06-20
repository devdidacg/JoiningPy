# JoiningPy

JoiningPy is an interactive terminal-based Python package manager that simplifies the installation, removal, discovery, and management of Python libraries.

Instead of manually typing `pip install` and `pip uninstall` commands, users can manage packages through a guided menu-driven interface.

JoiningPy is designed for beginners, students, and developers who prefer a structured workflow for managing Python dependencies.

---

## Features

### Package Management

* Install multiple predefined Python libraries at once
* Remove multiple installed libraries at once
* List all installed Python packages
* Confirmation prompts before package operations
* Number-based package selection
* Bulk selection using comma-separated input

### PyPI Integration

* Search packages directly from PyPI
* Display package information:

  * Package name
  * Current version
  * Package description
* Install searched packages immediately

### Cross-Platform Support

* Windows
* Linux
* macOS

### Automatic Setup

* Optional pip installation during first launch
* Automatic dependency installation
* Environment preparation before using JoiningPy

---

## Included Libraries

JoiningPy includes a catalog of 40 commonly used Python packages across multiple categories.

### Data Science

* Pandas
* NumPy
* Matplotlib
* Plotly
* Seaborn

### Machine Learning & AI

* Scikit-learn
* TensorFlow
* PyTorch
* Keras

### Web Development

* Flask
* Django

### Automation & Networking

* Requests
* Selenium
* BeautifulSoup

### Computer Vision & Media

* OpenCV
* Pillow

### Database

* SQLAlchemy

### Development Tools

* Pytest
* Jupyter

### Game Development

* Pygame

Additional libraries can be added easily through the configuration files.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/devdidacg/JoiningPy.git
cd JoiningPy
```

### Install Dependencies

```bash
python dependencies.py
```

or

```bash
python3 dependencies.py
```

### Start JoiningPy

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## Windows Installer

Download the latest release from GitHub:

https://github.com/devdidacg/JoiningPy/releases

Steps:

1. Download the latest installer.
2. Run the installer.
3. Launch JoiningPy.
4. Start managing Python packages.

---

## Screenshots

### Installer

![Installer](https://github.com/devdidacg/JoiningPy/blob/main/images/download-installer.png?raw=true)

### Installation Process

![Installation](https://github.com/devdidacg/JoiningPy/blob/main/images/Installer%20Image%20JoiningPy.png?raw=true)

### Source Code Download

![Source Code](https://github.com/devdidacg/JoiningPy/blob/main/images/Source%20Code%20Image.png?raw=true)

---

## First Launch

When starting JoiningPy for the first time:

```text
[JoiningPy] Hello, Ready to start? (y/n)
```

If pip is not installed, JoiningPy can install it automatically:

```text
[JoiningPy] Do you want install pip? (y/n)
```

Supported installation methods:

| System  | Method                  |
| ------- | ----------------------- |
| Windows | get-pip.py              |
| Linux   | apt install python3-pip |
| macOS   | get-pip.py              |

---

## Main Menu

```text
install
remove
list
search
exit
```

### Install

Install one or multiple predefined libraries:

```text
1,2,3,5
```

JoiningPy will install all selected packages.

---

### Remove

Remove one or multiple packages:

```text
4,7,10
```

JoiningPy will uninstall all selected packages after confirmation.

---

### List Installed Packages

```text
list
```

Displays all installed Python packages using:

```bash
pip list
```

---

### Search Packages

Search any package available on PyPI:

```text
search
requests
```

Example output:

```text
Library found!

Name: requests
Version: 2.x.x
Summary: Python HTTP for Humans.
```

Install immediately:

```text
You want to install this library? (y/n): y
```

---

## Project Structure

```text
JoiningPy/
│
├── main.py
├── install.py
├── PyLibSearch.py
├── variables.py
├── requeriments.py
│
├── images/
│   ├── download-installer.png
│   ├── Installer Image JoiningPy.png
│   └── Source Code Image.png
│
├── README.md
└── LICENSE
```

---

## Requirements

* Python 3.10 or newer
* Internet connection
* pip
* Windows, Linux, or macOS

Check your Python version:

```bash
python --version
```

---

## Contributing

Contributions are welcome.

Possible improvements include:

* Adding new predefined packages
* Improving the terminal interface
* Refactoring repetitive package logic
* Better package categorization
* Enhanced error handling
* Performance optimizations
* Additional operating system support

Workflow:

```text
Fork → Clone → Modify → Commit → Pull Request
```

---

## Roadmap

### Planned Features

* Dynamic package catalog
* Category-based filtering
* Package recommendations
* Version selection
* Dependency analysis
* Progress bars
* Improved terminal UI
* Configuration file support
* Favorites system
* Package update checker

---

## License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 devdidacg

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software and
associated documentation files.
```

---

## About

JoiningPy aims to make Python package management easier and more accessible through a simple interactive terminal interface.

Current capabilities:

* Install packages
* Remove packages
* List installed packages
* Search packages on PyPI
* Install searched packages
* Multi-package operations
* Cross-platform support
* Automatic pip setup
