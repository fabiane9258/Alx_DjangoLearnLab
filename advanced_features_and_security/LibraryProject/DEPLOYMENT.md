# Django Secure Deployment Instructions

This file documents the necessary steps to securely deploy the Django project using HTTPS and Let's Encrypt.

---

## ✅ 1. Set `DEBUG = False`

In `LibraryProject/settings.py`, ensure the following:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
