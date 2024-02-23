# Amazon Deadline Cloud for Rhino Development

This package has two active branches:

    mainline -- For active development. This branch is not intended to be consumed by other packages. Any commit to this branch may break APIs, dependencies, and so on, and thus break any consumer without notice.
    release -- The official release of the package intended for consumers. Any breaking releases will be accompanied with an increase to this package's interface version.

## Submitter Development Workflow

1. Install deadline-cloud and PySide2
2. Set the following environment variables
    - Set the environment variable `DEADLINE_PYTHON` as the path to the Python installation where deadline-cloud and PySide2 were installed in step 1.
      - e.g. On Windows if using Python 3.10 it might be `set DEADLINE_PYTHON="C:/Users/<USER>/AppData/Local/Programs/Python/Python310/python"`
    - Set the environment variable `DEADLINE_RHINO` as the path to the `<PATH TO>/deadline-cloud-for-rhino/src/deadline/rhino_submitter` folder
      - e.g. On Windows if the source was on the user's desktop it might be  `set DEADLINE_RHINO="C:/Users/<USER>/Desktop/deadline-cloud-for-rhino/src/deadline/rhino_submitter"`
4. Launch Rhino with the environment variables from step 2. set.
5. Install the submitter into the Rhino toolbar `<PATH TO>/deadline-cloud-for-rhino/rhino_script/deadlinecloud.rui`

## Adaptor Development Workflow

Worker needs to find Rhino.exe

```
set PATH=C:\Program Files\Rhino 8\System;%PATH%

```

