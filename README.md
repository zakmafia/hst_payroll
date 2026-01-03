# 🏢 HST Payroll Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-5.0-green.svg)](https://www.djangoproject.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive web-based payroll management system built with Django. This application helps organizations efficiently manage employee salaries, deductions, allowances, tax calculations, and generate detailed payroll reports.

---

## ✨ Features

- **Employee Management**: Complete employee information management including personal details, contact information, and employment data
- **Department & Position Management**: Organize employees by departments and positions
- **Salary Management**: Configure and manage employee salaries with support for multiple currencies (ETB, USD)
- **Tax Calculation**: Automated tax calculations based on configurable tax brackets and rates
- **Allowances**: Manage various employee allowances (taxable and non-taxable)
- **Deductions**: Support for both fixed-amount and percentage-based deductions
- **Pension Contributions**: Automated pension calculation and tracking
- **Payroll Processing**: Generate comprehensive payroll reports for specified date ranges
- **Excel Export**: Export payroll data to Excel format for record-keeping and analysis
- **Multi-Currency Support**: Handle payments in Ethiopian Birr (ETB) and US Dollars (USD)
- **User Authentication**: Secure login system for authorized access

---

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.0
- **Database**: SQLite (development) / PostgreSQL (production-ready)
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Material Design Icons (MDI)
- **Chart Library**: Chart.js
- **Excel Generation**: XlsxWriter
- **Python Version**: 3.8+

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git
- Virtual environment tool (venv or virtualenv)

---

## 🚀 Installation

Follow these steps to get the development environment running:

### 1. Clone the repository
```bash
git clone https://github.com/zakmafia/hst_payroll.git
cd hst_payroll
```

### 2. Create and activate a virtual environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory and configure the following variables (refer to `.env.example`):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run database migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```

### 7. Collect static files (production)
```bash
python manage.py collectstatic
```

### 8. Start the development server
```bash
python manage.py runserver
```

### 9. Access the application
Open your browser and navigate to: **http://localhost:8000**

Admin panel: **http://localhost:8000/admin**

---

## 📖 Usage

1. **Login**: Access the system using your credentials
2. **Dashboard**: View summary of employees, departments, and payroll statistics
3. **Manage Employees**: Add, edit, or deactivate employee records
4. **Configure Departments & Positions**: Set up organizational structure
5. **Set Up Tax Brackets**: Define tax rates for different income ranges
6. **Configure Allowances & Deductions**: Create taxable/non-taxable allowances and deductions
7. **Process Salaries**: Assign salaries to employees with automatic calculations
8. **Generate Payroll**: Create payroll reports for specific periods
9. **Export Reports**: Download payroll data in Excel format

---

## 🔧 Environment Variables

The following environment variables are required:

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for cryptographic signing | `your-secret-key-here` |
| `DEBUG` | Enable/disable debug mode | `True` or `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost,127.0.0.1` |
| `DATABASE_URL` | Database connection string | `sqlite:///db.sqlite3` |

Refer to `.env.example` for a complete list of configuration options.

---

## 🧪 Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test hst_payroll_manager

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows our coding standards and includes appropriate tests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔒 Security

If you discover any security-related issues, please review our [Security Policy](SECURITY.md) for information on how to responsibly disclose vulnerabilities.

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/zakmafia/hst_payroll/issues)
- **Discussions**: [GitHub Discussions](https://github.com/zakmafia/hst_payroll/discussions)
- **Email**: support@example.com

---

## 🙏 Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- UI components from [Material Design Icons](https://materialdesignicons.com/)
- Charts powered by [Chart.js](https://www.chartjs.org/)

---

**Made with ❤️ for HST**
