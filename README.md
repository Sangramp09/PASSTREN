# PASSTREN
PasStren is a Python-based password strength analyzer designed to evaluate password security using intelligent scoring techniques instead of simple length checks.


# 🔐 PasStren

**PasStren** is a lightweight and accurate password strength analyzer built with Python.

It evaluates password security using multiple scoring factors such as:

* Password length
* Character diversity
* Entropy estimation
* Common password detection
* Sequential pattern detection
* Repeated character penalties
* Strength visualization
* Improvement suggestions

PasStren is designed to provide realistic password strength predictions while remaining simple and easy to understand.

---

# Features

✅ Password strength scoring (0–100)

✅ Entropy-based prediction

✅ Detection of weak password patterns

✅ Character diversity analysis

✅ Visual strength bar

✅ Security recommendations

✅ Command-line interface (CLI)

---

# Project Structure

```plaintext
PasStren/
│
├── passtren.py
├── README.md
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
https://github.com/Sangramp09/PASSTREN
```

Move into project folder:

```bash
cd PasStren
```

---

# Requirements

Python 3.8+

Install dependencies:

```bash
pip install -r requirements.txt
```

No external libraries are required.

---

# Run PasStren

Start interactive mode:

```bash
python passtren.py
```

Example:

```plaintext
==============================
      🔐 PASSTREN
==============================

Enter Password:
```

Exit:

```plaintext
quit
```

or

```plaintext
exit
```

---

# Example Output

```plaintext
============================================================

              🔐 PASSTREN REPORT

============================================================

Password : ************
Length   : 12
Score    : 88/100
Rating   : STRONG ✅
Strength : [████████░░]

GOOD:
- ✅ Good length (12)
- ✅ Lowercase
- ✅ Uppercase
- ✅ Numbers
- ✅ Special characters

SUGGESTIONS:
- 🎉 Excellent password

============================================================
```

---

# Scoring Method

PasStren evaluates passwords using:

| Factor                 | Description                                      |
| ---------------------- | ------------------------------------------------ |
| Length                 | Longer passwords receive higher scores           |
| Character Diversity    | Mix of lowercase, uppercase, digits, and symbols |
| Entropy                | Estimates unpredictability                       |
| Weak Pattern Detection | Detects sequences and common combinations        |
| Repeat Detection       | Penalizes repeated characters                    |
| Common Password Check  | Reduces score for known weak passwords           |

---


# Future Improvements

* Breached password detection
* GUI version
* Web dashboard
* Password history analysis
* Export reports
* Batch password testing
* Machine learning scoring

---

# Security Note

PasStren masks password output and does not store passwords.

Do not use password analyzers to validate real production credentials.

---

# Author

Developed by Sangram

GitHub: https://github.com/Sangramp09?tab=repositories
