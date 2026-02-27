# Drawing Analyzer

AI Area Calculator for 2D Drawings using OpenCV.

## Cursor Cloud specific instructions

### Project structure

- `drawing_analyzer/app.py` — Streamlit web UI (standalone, the primary runnable component)
- `drawing_analyzer/api.py` — Frappe-based backend API for area calculation (requires full Frappe/Bench stack with MariaDB + Redis; not runnable standalone)
- `drawing_analyzer/requirements.txt` — Python pip dependencies for the Streamlit app

### Running the Streamlit app

```
cd drawing_analyzer
streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
```

The app accepts PNG, JPG, and PDF uploads. The core area-calculation logic in `api.py` uses OpenCV contour detection and is tightly coupled to the Frappe framework (`frappe.whitelist()`, `frappe.get_site_path()`), so it cannot be imported directly without a Frappe bench environment.

### Linting

No lint configuration is committed. You can use `ruff check drawing_analyzer/` for quick Python linting. Existing code has two unused-import warnings (F401) that are part of the repo.

### Testing

No automated tests exist in the repository. To verify the core OpenCV logic works independently of Frappe, you can run the area-calculation pipeline directly against a test image:

```python
import cv2, numpy as np
img = cv2.imread("path/to/image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 150)
contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest = max(contours, key=cv2.contourArea)
print(cv2.contourArea(largest))
```

### Frappe backend (heavyweight, not needed for Streamlit UI)

The `api.py` module is a Frappe custom app. Running it requires `bench init`, `bench new-site`, MariaDB, and Redis. This is not needed to develop or test the Streamlit frontend.
