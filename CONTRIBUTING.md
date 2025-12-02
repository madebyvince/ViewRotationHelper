# Contributing to View Rotation Helper

Thank you for your interest in contributing to View Rotation Helper! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your Blender version
- Screenshots or error messages (if applicable)

### Suggesting Features

Feature suggestions are welcome! Please create an issue with:
- A clear description of the feature
- Use cases explaining why this feature would be useful
- Examples of how it would work (mockups welcome!)

### Submitting Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines below
3. **Test thoroughly** in multiple Blender versions if possible
4. **Update documentation** (README, CHANGELOG) if needed
5. **Commit with clear messages** describing what and why
6. **Submit a pull request** with a clear description

## Code Style Guidelines

### Python Style
- Follow [PEP 8](https://pep8.org/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable and function names

### Blender Add-on Conventions
- Follow [Blender's add-on guidelines](https://wiki.blender.org/wiki/Process/Addons)
- Use proper `bl_idname` naming: lowercase with underscores
- Include `bl_label` and `bl_description` for all operators and panels
- Add `bl_options = {'REGISTER', 'UNDO'}` to operators when appropriate

### Documentation
- Add docstrings to all classes and functions
- Update README.md for new features
- Add entries to CHANGELOG.md following the existing format
- Include comments for complex logic

## Testing

Before submitting a pull request:
1. Test in Blender 3.x and 4.x if possible
2. Verify all buttons and operators work correctly
3. Check that undo/redo works properly
4. Ensure no errors appear in the console
5. Test with different viewport configurations

## Commit Message Guidelines

Use clear and meaningful commit messages:
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Start with a capital letter
- Keep the first line under 50 characters
- Add detailed description after a blank line if needed

Examples:
```
Add custom rotation angle input

Update README with installation screenshots

Fix rotation bug in perspective mode
```

## Project Structure

```
view-rotation-helper/
├── view_rotation_helper.py  # Main add-on file
├── README.md                # Project documentation
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # This file
└── .gitignore              # Git ignore rules
```

## Questions?

Feel free to open an issue for any questions about contributing!

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Assume good intentions

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Personal attacks
- Publishing others' private information

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to View Rotation Helper! 🎉
