# Drawing Analyzer

AI Area Calculator for 2D Drawings — a Frappe custom app with a Streamlit frontend.

## Cursor Cloud specific instructions

### Architecture

- **Streamlit frontend** (`drawing_analyzer/app.py`): Standalone UI for uploading 2D drawings (PNG/JPG/PDF). Runs on port 8501.
- **Frappe backend** (`drawing_analyzer/api.py`): Exposes a `calculate_area` whitelisted API that uses OpenCV to detect shapes and compute areas. Runs via `bench start` on port 8000.

### Services

| Service | Port | How to start |
|---------|------|-------------|
| Streamlit | 8501 | `cd /workspace/drawing_analyzer && streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true` |
| Frappe (bench) | 8000 | `cd /home/ubuntu/frappe-bench && bench start` |

### Frappe bench setup caveats

- The bench lives at `/home/ubuntu/frappe-bench` (Frappe v15, Python 3.12).
- The `drawing_analyzer` module is added to the bench's Python path via a `.pth` file (`env/lib/python3.12/site-packages/drawing_analyzer.pth` pointing to `/workspace`).
- The app's symlink is at `apps/drawing_analyzer -> /workspace`.
- A module subdirectory `drawing_analyzer/drawing_analyzer/` with `__init__.py` was created because Frappe requires it for its module system (matches `modules.txt`).
- MariaDB must be running before `bench start`. Start it with: `sudo mariadbd-safe &>/dev/null &`
- Redis is started automatically by bench's Procfile, but a standalone instance can be started with `redis-server --daemonize yes`.
- Site: `dev.localhost`, admin password: `admin`.

### Lint

```
flake8 drawing_analyzer/api.py drawing_analyzer/app.py drawing_analyzer/hooks.py --max-line-length=120
```

### Testing the image processing logic

The core logic in `api.py` uses OpenCV to find contours and calculate areas. It can be tested standalone by importing `cv2` and `numpy` and running the contour detection pipeline on a test image.
