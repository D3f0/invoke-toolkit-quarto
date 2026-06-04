# invoke-toolkit-quarto

A set of invoke-toolkit tasks

## Installation

### Use the plugin from `git`

```bash
uv tool install invoke-toolkit --with git+https://github.com/YOUR_USERNAME/invoke-toolkit-quarto
```

### Use the plugin from a checkout

Note that if you already ran this step for other plugins, you may want
to add the `--with` or `--with-editable` of other plugins.

```bash
git clone https://github.com/YOUR_USERNAME/invoke-toolkit-quarto
cd invoke-toolkit-quarto
uv tool install invoke-toolkit --with-editable .
```

## Usage

Once installed, the tasks from this package will be automatically available in `invoke-toolkit`/`intk`:

```bash
intk -l
```

You should see a collection named `quarto` with the available tasks.

### Available Tasks

- `quarto.hello` - Say hello

Example:

```bash
intk quarto.hello --name "Developer"
```

## License

MIT
