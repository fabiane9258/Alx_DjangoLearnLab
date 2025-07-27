# LibraryProject - Django Starter Setup
## 🔒 Security Best Practices Implemented in This Django Project

1. **DEBUG Disabled**
   - `DEBUG = False` to avoid exposing sensitive information in error messages.

2. **Host Header Validation**
   - `ALLOWED_HOSTS` is restricted to trusted domains: `['localhost', '127.0.0.1']`.

3. **HTTPS Cookie Settings**
   - `CSRF_COOKIE_SECURE = True`
   - `SESSION_COOKIE_SECURE = True`

4. **Clickjacking and XSS Protection**
   - `X_FRAME_OPTIONS = 'DENY'` blocks iframe embedding.
   - `SECURE_BROWSER_XSS_FILTER = True` activates browser XSS protection.
   - `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents content-type sniffing.

5. **Content Security Policy (CSP)**
   - Integrated `django-csp` with policies for:
     - Scripts: `'self'`
     - Styles: `'self'` and Google Fonts
     - Images: `'self'`, `data:`
     - Fonts: Google Fonts only
     - Objects: None (disabled)

6. **Middleware Security Order**
   - `csp.middleware.CSPMiddleware` is added right after `SecurityMiddleware`.

These settings ensure a more secure deployment posture and are aligned with OWASP and Django security guidelines.
