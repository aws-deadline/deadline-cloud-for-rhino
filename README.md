# Amazon Deadline Cloud for Rhino

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
