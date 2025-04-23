# HyperWorksPyAPI

The HyperWorksPyAPI is a Visual Studio Code extension which provides syntax support for HyperMesh, Simlab and Inspire Python API. This extension aims to improve productivity for users who are coding customization and automation tasks for the HyperWorks applications using Visual Studio Code. Classes and methods from hm, hw, simlab and hwx modules and sub-modules are currently supported. 

A tree structure of all availble modules is the following:
``` bash
hm
└── hm.entities

hw
├── hw.hv
├── hw.hg
└── hw.taskmanager

report
├── report.hwxpptxtypes
└── report.hwxdocxtypes

simlab
├── simlab.messagebox
└── simlab.simlab

hwx
├── hwx.gui
├── hwx.inspire
│   ├── hwx.inspire.core
│   ├── hwx.inspire.math
│   └── hwx.inspire.motion
└── hwx.common
    └── hwx.common.math
```
## Quick Start 

This extension is activated when vscode opens but in general, is good practice to activate the extension by opening an existing workspace (directory) or creating a new one. Then a hidden folder is created (.vscode) in this workspace which permits to use the extension. 

## Supported Features 

The features of this extension are supported via Pylance extension, which is installed together with HyperWorksPyAPI extension if not already installed. Currently, HyperWorksPyAPI supports: 

* Syntax highlighting.

* Tooltips showing the function description, signature and arguments.

![Tooltips](https://github.com/altairengineering/HyperWorksPyAPI/blob/master/images/gif1.gif?raw=true)

* Autocompletion.

![Autocompletion](https://github.com/altairengineering/HyperWorksPyAPI/blob/master/images/gif2.gif?raw=true)


Other features as such as code navigation and syntax checking are supported through Pylance. 


## Questions and Support 

<!--Users appreciate release notes as you update your extension. -->
We encourage feedback. If you face any issues please reach out to us via [Discussions - Altair Community.](https://community.altair.com/discussions) 

