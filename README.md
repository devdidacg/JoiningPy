# JoiningPy

JoiningPy is a terminal-based Python package manager that allows users to install and remove multiple Python libraries through an interactive menu system. It removes the need to manually type pip commands and replaces them with a guided interface for managing packages directly from the terminal.

The goal of JoiningPy is to simplify Python dependency management, especially for beginners or users who prefer a structured and visual workflow instead of command-line syntax.

---

## Features

- Interactive terminal menu system
- Install multiple Python packages at once
- Remove multiple Python packages at once
- Number-based selection system
- Bulk selection using comma-separated input
- Confirmation prompts before executing actions
- Lightweight and fast execution
- Easy to extend with new libraries
- Organized library categories

---

## Supported Libraries

Libraries are grouped by category. Each section can be expanded and extended easily.

<details>
<summary>Data Science</summary>

- Pandas  
- NumPy  
- Matplotlib  
- Plotly  
- Seaborn  

</details>

<details>
<summary>Machine Learning & AI</summary>

- Scikit-learn  
- TensorFlow  
- PyTorch  
- Keras  

</details>

<details>
<summary>Web Development</summary>

- Flask  
- Django  

</details>

<details>
<summary>Automation & Networking</summary>

- Requests  
- Selenium  
- BeautifulSoup  

</details>

<details>
<summary>Computer Vision & Media</summary>

- OpenCV  
- Pillow  

</details>

<details>
<summary>Database</summary>

- SQLAlchemy  

</details>

<details>
<summary>Development Tools</summary>

- Pytest  
- Jupyter  

</details>

<details>
<summary>Game Development</summary>

- PyGame  

</details>

---

## Installation

### Git (Recommended)

```bash
git clone https://github.com/devdidacg/JoiningPy
cd JoiningPy
python main.py
Windows Installer

Download the latest release:

https://github.com/devdidacg/JoiningPy/releases

Steps:

Download the installer
Run the setup
Open JoiningPy
Screenshots
Installer

Installation Process

Source Code Download

Getting Started

When you launch JoiningPy, you will see:

[JoiningPy] (Ready) version by author

Hello, Ready to start? (y/n)

Then choose an option:

install
remove
exit
Usage Example
Installing packages

Input multiple numbers separated by commas:

1,2,3

JoiningPy will automatically install selected libraries.

Removing packages
1,5,7
Project Structure
JoiningPy/
│
├── main.py
├── variables.py
├── requeriments.py
├── images/
│   ├── download-installer.png
│   ├── Installer Image JoiningPy.png
│   ├── Source Code Image.png
│
├── README.md
└── LICENSE
Requirements
Python 3.10+
pip installed
Windows recommended

Check version:

python --version
Contributing

Contributions are welcome.

You can help by:

Adding new libraries
Improving interface
Fixing bugs
Optimizing installation logic
Improving documentation

Workflow:

fork → clone → edit → commit → pull request
Roadmap
Package search system
Version selection for libraries
Dependency validation
Linux and macOS support
Configuration file support
Progress indicators
Better UI navigation
License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2026 devdidacg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
Notes

JoiningPy is designed to make Python package management easier, faster, and more structured using a simple terminal interface.