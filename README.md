# AWS Deadline Cloud for Rhino

This GitHub repository is an example integration with AWS Deadline Cloud that is intended to only be used for testing and is subject to change. This code is an alpha release. It is not a commercial release and may contain bugs, errors, defects, or harmful components. Accordingly, the code in this repository is provided as-is. Use within a production environment is at your own risk!
 
Our focus is to explore a variety of software applications to ensure we have good coverage across common workflows. We prioritized making this example available earlier to users rather than being feature complete.

This example has been used by at least one internal or external development team to create a series of jobs that successfully rendered. However, your mileage may vary. If you have questions or issues with this example, please start a discussion or cut an issue.

## Overview

This package has two active branches:

- `mainline` -- For active development. This branch is not intended to be consumed by other packages. Any commit to this branch may break APIs, dependencies, and so on, and thus break any consumer without notice.
- `release` -- The official release of the package intended for consumers. Any breaking releases will be accompanied with an increase to this package's interface version.

## Development

See [DEVELOPMENT](DEVELOPMENT.md) for more information.

## Build / Test / Release

### Build the package

```bash
hatch build
```

### Run tests

```bash
hatch run test
```

### Run linting

```bash
hatch run lint
```

### Run formatting

```bash
hatch run fmt
```

## Run tests for all supported Python versions

```bash
hatch run all:test
```

## Use development Submitter in Rhino

See DEVELOPMENT.md

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.