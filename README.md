# UV Package Manager Demo

## What is UV?

UV is a cutting-edge Python package and project manager built with Rust, designed to be a comprehensive solution for Python development. It combines the functionality of multiple tools like `pip`, `poetry`, `virtualenv`, and more into a single, high-performance package manager.

### Key Features

- ⚡ **Blazing Fast**: 10-100x faster than traditional tools like `pip`, `pip-compile`, and `pip-sync`
- 💾 **Disk-Space Efficient**: Uses global cache for dependency deduplication
- 🔩 **Advanced Dependency Management**: Includes dependency version overrides and conflict-tracking resolver
- 🤝 **Modern Python Features**: Supports editable installs, Git dependencies, direct URLs, local dependencies
- 🚀 **Unified Tooling**: Replaces multiple tools (`pip`, `pipx`, `poetry`, `pyenv`, etc.)
- 🗂️ **Universal Lockfile**: Provides consistent and portable lockfiles
- 🏢 **Workspace Support**: Handles scalable projects with Cargo-style workspace management

## Why Use UV?

1. **Speed & Efficiency**: UV's Rust-based implementation offers significant performance improvements
2. **Simplified Workflow**: Single tool replaces multiple package management tools
3. **Better Dependency Resolution**: Advanced algorithm prevents dependency conflicts
4. **Cross-Platform**: Full compatibility with macOS, Linux, and Windows
5. **Modern Standards**: Follows latest Python packaging standards and best practices

## Installation

You can install UV through multiple methods:

```bash
# On Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# With pip
pip install uv

# With pipx
pipx install uv
```

### Environment Setup

After installation, add UV to your PATH:

**Windows**:
```
%USERPROFILE%\.local\bin
```

**Linux/macOS**:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

## UV in Projects

### Creating a New Project

```bash
uv init project-name
```

This creates:
- Basic project structure
- `pyproject.toml` file
- `README.md`
- Source directory
- `.gitignore`

### Managing Dependencies

```bash
# Add a dependency
uv add package-name

# Remove a dependency
uv remove package-name

# Sync dependencies
uv sync

# Lock dependencies
uv lock
```

### Virtual Environments

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On Windows
.venv\Scripts\activate
# On Linux/macOS
source .venv/bin/activate
```

## UV in Scripts

### Running Scripts

```bash
# Run a Python script
uv run script.py

# Run with specific dependencies
uv add --script dependency-name
```

## Common UV Commands

### Package Management
```bash
# Install packages
uv pip install package-name
uv pip install -r requirements.txt

# Install in editable mode
uv pip install -e .

# Sync with requirements
uv pip sync requirements.txt
```

### Python Version Management
```bash
# Install Python version
uv python install 3.12

# List available versions
uv python list

# Pin Python version
uv python pin
```

### Tool Management
```bash
# Install a tool
uv tool install tool-name

# List installed tools
uv tool list

# Run a tool
uv tool run tool-name
```

## Best Practices

1. Always use virtual environments for projects
2. Keep `pyproject.toml` and lockfiles in version control
3. Use UV's caching mechanism for better performance
4. Regularly update dependencies with `uv sync`
5. Use UV's built-in Python version management

## Contributing

Feel free to contribute to this demo repository by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 