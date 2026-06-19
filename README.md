# JoiningPy

JoiningPy is a terminal-based Python package manager that allows users to install, remove, search, and manage Python libraries through an interactive menu system.

It removes the need to manually type pip commands and replaces them with a guided interface for managing packages directly from the terminal.

The goal of JoiningPy is to simplify Python dependency management, especially for beginners or users who prefer a structured and visual workflow instead of command-line syntax.

---

## Features

* Interactive terminal menu system
* Install multiple Python packages at once
* Remove multiple Python packages at once
* Search packages directly from PyPI
* Install searched packages instantly
* List installed libraries
* Number-based selection system
* Bulk selection using comma-separated input
* Confirmation prompts before executing actions
* Easy to extend with new libraries
* Package information display:

  * Name
  * Version
  * Summary

---

## Supported Libraries

Libraries are grouped by category and can be expanded easily.

<details>
<summary>Data Science</summary>

* Pandas
* NumPy
* Matplotlib
* Plotly
* Seaborn

</details>

<details>
<summary>Machine Learning & AI</summary>

* Scikit-learn
* TensorFlow
* PyTorch
* Keras

</details>

<details>
<summary>Web Development</summary>

* Flask
* Django

</details>

<details>
<summary>Automation & Networking</summary>

* Requests
* Selenium
* BeautifulSoup

</details>

<details>
<summary>Computer Vision & Media</summary>

* OpenCV
* Pillow

</details>

<details>
<summary>Database</summary>

* SQLAlchemy

</details>

<details>
<summary>Development Tools</summary>

* Pytest
* Jupyter

</details>

<details>
<summary>Game Development</summary>

* PyGame

</details>

---

## Installation

### Git (Recommended)

```bash
git clone https://github.com/devdidacg/JoiningPy
cd JoiningPy
python main.py
```

---

### Windows Installer

Download the latest release:

https://github.com/devdidacg/JoiningPy/releases

Steps:

1. Download the installer
2. Run the setup
3. Open JoiningPy

---

## Screenshots

### Installer

![Installer](https://github.com/devdidacg/JoiningPy/blob/main/images/download-installer.png?raw=true)

### Installation Process

![Installation](https://github.com/devdidacg/JoiningPy/blob/main/images/Installer%20Image%20JoiningPy.png?raw=true)

### Source Code Download

![Source Code](https://github.com/devdidacg/JoiningPy/blob/main/images/Source%20Code%20Image.png?raw=true)

---

## Getting Started

Launch JoiningPy:

```bash
python main.py
```

You will see:

```text
[JoiningPy] (Ready) version by author

Hello, Ready to start? (y/n)
```

Then choose an option:

```text
install
remove
list
search
exit
```

---

## Usage Examples

### Installing packages

Input multiple numbers separated by commas:

```text
1,2,3
```

JoiningPy will install selected libraries automatically.

---

### Removing packages

```text
1,5,7
```

---

### Listing installed packages

```text
list
```

Displays all installed Python libraries.

---

### Searching packages

Search any package from PyPI:

```text
search
requests
```

Example output:

```text
Library found!

Name: requests
Version: 2.34.2
Summary: Python HTTP for Humans.
```

Install immediately:

```text
You want to install this library? (y/n): y
```

---

## Search Packages

JoiningPy includes package search powered by PyPI.

Capabilities:

* Search packages by name
* View package details
* Install directly after search
* Return to menu after actions

---

## Project Structure

```text
JoiningPy/
│
├── main.py
├── PyLibSearch.py
├── variables.py
├── requeriments.py
├── images/
│   ├── download-installer.png
│   ├── Installer Image JoiningPy.png
│   ├── Source Code Image.png
│
├── README.md
└── LICENSE
```

---

## Requirements

* Python 3.10+
* pip
* Internet connection (for package search)
* Windows, Linux, or macOS

Check version:

```bash
python --version
```

---

## Contributing

Contributions are welcome.

You can help by:

* Adding new libraries
* Improving interface
* Fixing bugs
* Optimizing installation logic
* Improving documentation
* Improving search functionality

Workflow:

```text
fork → clone → edit → commit → pull request
```

---

## Roadmap

* Search filters and package recommendations
* Version selection for libraries
* Dependency validation
* Dynamic package catalog
* Configuration file support
* Install progress tracking
* Better UI navigation
* Better error handling
* Cross-platform improvements

---

## License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 devdidacg

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software
and associated documentation files.
```

---

## Notes

JoiningPy is designed to make Python package management easier, faster, and more structured through a simple interactive terminal interface.

Current functionality includes:

* Install
* Remove
* List
* Search
* PyPI integration
* Multi-selection package operations
