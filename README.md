# MOVIE — Movie Recommender

Small Gradio app that recommends movies using precomputed pickled data.

## Contents
- `app.py` — main application (Gradio UI)
- `requirements.txt` — Python dependencies
- `new_dataset.pkl` — pickled movie dataset (required)
- `similarity.pkl` — pickled similarity matrix (required)

## Setup (Windows)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # in PowerShell
# or
.\.venv\Scripts\activate.bat    # in CMD
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Ensure `new_dataset.pkl` and `similarity.pkl` are placed in the same folder as `app.py`.

## Run

```powershell
python app.py
```

- The Gradio app will start and show a local URL in the console (e.g., `http://127.0.0.1:7860`).
- Use the dropdown to pick a movie and click "Recommend" to see clickable search tags.

## Notes & Troubleshooting
- If you see `Movie not found in dataset!`, the exact title (from the dropdown) should be used — using the dropdown avoids this.
- If `ModuleNotFoundError` occurs, activate the virtual environment and re-run `pip install -r requirements.txt`.
- Missing pickle files will cause file-open errors; place them in the project root.

## Optional Improvements
- Pin package versions in `requirements.txt` for reproducible installs.
- Add a small example `new_dataset_sample.pkl` for testing without the full dataset.

---
Generated README for the MOVIE recommender app.
