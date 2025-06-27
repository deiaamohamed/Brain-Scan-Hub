# Brain Scan Hub - MRI Analysis Web Application

Brain Scan Hub is a Django-based web application for MRI image analysis, patient management, and automated radiology report generation. It integrates machine learning models for image segmentation and report generation, providing a modern, user-friendly interface for doctors and staff.

---

## Features

- User Authentication: Role-based login for doctors and reception/admin staff.
- Patient Management: Register, view, and manage patient data and MRI history.
- MRI Analysis: Upload MRI images, run ML-based segmentation, and generate AI-powered radiology reports.
- Result Dashboard: View analysis results with MRI images and downloadable/printable reports.
- Contact & Issue Reporting: Built-in contact form for staff to report issues or request features.
- Modern UI: Responsive, dark-mode-enabled dashboard with loading overlays and print-friendly pages.

---

## Project Structure

```
```
check https://github.com/deiaamohamed/Brain-Scan-Hub/blob/main/SYSTEM_FLOW_DIAGRAM_CLEAN.md for more details
```
Brain Scan Hub/
│
├── BrainProject/                # Django project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── Brainapp/                    # Main Django app
│   ├── models.py                # User, Patient, MRI_Image, Result, etc.
│   ├── views.py                 # All view logic
│   ├── urls.py                  # App-specific routes
│   ├── admin.py                 # Admin customizations
│   ├── migrations/              # Database migrations
│   ├── ML/                      # ML scripts and configs
│   │   ├── Prediction_Script.py
│   │   ├── report_generator.py
│   │   ├── biomedclip.py
│   │   ├── predictor_setup.py
│   │   └── config.yaml
│   ├── segmentation_model/      # Trained ML model (PyTorch .pth)
│   ├── static/                  # CSS, JS, and static assets
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       └── Brainapp/            # HTML templates
│           ├── index.html
│           ├── mri-analysis.html
│           ├── analysis_result.html
│           ├── patient-data.html
│           ├── doctor-home.html
│           ├── receptionist-home.html
│           ├── signup-patient.html
│           ├── contact-dev.html
│           └── ...
│
├── db.sqlite3                   # SQLite database
├── media/                       # Uploaded MRI images and results
├── image/                       # Processed images/results
├── staticfiles/                 # Collected static files
├── manage.py                    # Django management script
├── README.md
└── .gitignore
```

---

## Getting Started

### 1. Set Up Virtual Environment
```sh
python -m venv env
env\Scripts\activate  # On Windows
# or
source env/bin/activate  # On Mac/Linux
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
# Or manually:
pip install django pillow django-extensions
```

### 3. Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)
```sh
python manage.py createsuperuser
```

### 5. Run the Development Server
```sh
python manage.py runserver
```
Visit: http://127.0.0.1:8000

---

## Machine Learning Integration

- ML scripts are in `Brainapp/ML/`.
- Trained model is in `Brainapp/segmentation_model/model_final.pth`.
- MRI images are uploaded to `/media/` and processed results are saved in `/image/`.

---

## Notes

- Media files: Make sure `/media/` is writable for image uploads.
- Static files: Use `python manage.py collectstatic` for production.
- Admin panel: http://127.0.0.1:8000/admin
- Entity-Relationship Diagrams: See `clean_erd.png` and `erd.png` for database structure.

---

## Resources

- https://docs.djangoproject.com/en/5.1/
- https://pillow.readthedocs.io/
- https://django-extensions.readthedocs.io/

---
