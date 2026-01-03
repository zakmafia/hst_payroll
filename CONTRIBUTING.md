# Contributing to HST Payroll Management System

First off, thank you for considering contributing to HST Payroll Management System! It's people like you that make this project such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Style Guides](#style-guides)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible using our bug report template.

**How to submit a good bug report:**
- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed and what behavior you expected to see
- Include screenshots if possible
- Include your environment details (OS, Python version, Django version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- A clear and descriptive title
- A detailed description of the proposed functionality
- Explain why this enhancement would be useful
- List any alternative solutions you've considered

### Your First Code Contribution

Unsure where to begin? You can start by looking through `beginner` and `help-wanted` issues:

- **Beginner issues**: Issues that should only require a few lines of code
- **Help wanted issues**: Issues that are more involved than beginner issues

### Pull Requests

- Fill in the required pull request template
- Follow our coding standards
- Include appropriate test cases
- Update documentation as needed
- Ensure all tests pass

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/hst_payroll.git
   cd hst_payroll
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

6. **Make your changes and test them**
   ```bash
   python manage.py test
   ```

## Coding Standards

### Python Code Style

We follow PEP 8 guidelines with some modifications:

- **Line Length**: Maximum 100 characters (not strict 79)
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Group imports in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application imports
  
- **Naming Conventions**:
  - Classes: `CapitalizedWords`
  - Functions/Variables: `lowercase_with_underscores`
  - Constants: `UPPERCASE_WITH_UNDERSCORES`

### Django-Specific Guidelines

- Follow Django's coding style
- Use Django's built-in features when possible
- Keep views simple; move business logic to models or utils
- Use class-based views for common patterns
- Always use Django's ORM; avoid raw SQL unless absolutely necessary

### JavaScript Code Style

- Use ES6+ features when possible
- Use 2 spaces for indentation
- Use single quotes for strings
- Use meaningful variable names
- Add comments for complex logic

### CSS/SCSS Guidelines

- Use meaningful class names
- Follow BEM naming convention when applicable
- Keep specificity low
- Group related properties together

## Commit Message Guidelines

We follow the Conventional Commits specification:

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring without adding features or fixing bugs
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, dependency updates

### Examples
```
feat(payroll): add export to PDF functionality

Implemented PDF export for payroll reports using ReportLab.
Users can now download payroll data in PDF format.

Closes #123
```

```
fix(employee): correct phone number validation

Fixed regex pattern to accept international phone numbers
with country codes.

Fixes #456
```

## Pull Request Process

1. **Update Documentation**: Update the README.md or other documentation with details of changes if needed

2. **Update Tests**: Add or update tests to cover your changes

3. **Run Tests**: Ensure all tests pass
   ```bash
   python manage.py test
   flake8
   ```

4. **Update CHANGELOG**: Add your changes to CHANGELOG.md under "Unreleased"

5. **Create Pull Request**: 
   - Use a clear and descriptive title
   - Fill out the pull request template completely
   - Reference any related issues

6. **Code Review**: Address any feedback from reviewers

7. **Merge**: Once approved, a maintainer will merge your PR

### PR Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Style Guides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Python Docstrings

Use Google-style docstrings:

```python
def calculate_tax(gross_salary, tax_rate):
    """Calculate tax based on gross salary and tax rate.
    
    Args:
        gross_salary (Decimal): The employee's gross salary
        tax_rate (Decimal): The applicable tax rate percentage
        
    Returns:
        Decimal: The calculated tax amount
        
    Raises:
        ValueError: If gross_salary or tax_rate is negative
    """
    if gross_salary < 0 or tax_rate < 0:
        raise ValueError("Salary and tax rate must be non-negative")
    return gross_salary * (tax_rate / 100)
```

### Testing

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names that explain what is being tested
- Follow the Arrange-Act-Assert pattern

```python
def test_calculate_tax_with_valid_inputs(self):
    """Test tax calculation with valid salary and rate."""
    # Arrange
    gross_salary = Decimal('5000.00')
    tax_rate = Decimal('10.0')
    
    # Act
    result = calculate_tax(gross_salary, tax_rate)
    
    # Assert
    self.assertEqual(result, Decimal('500.00'))
```

## Questions?

Don't hesitate to ask questions! You can:
- Open an issue with the `question` label
- Reach out to the maintainers
- Start a discussion in GitHub Discussions

## Recognition

Contributors will be recognized in our README.md file and release notes.

Thank you for contributing! 🎉
