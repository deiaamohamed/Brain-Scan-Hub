# 🧠 Brain Scan Hub - System Flow Diagram

## 📋 System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        BRAIN SCAN HUB                          │
│                    MRI Analysis System                          │
└─────────────────────────────────────────────────────────────────┘
```

## 👥 User Roles & Access

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     ADMIN       │    │     DOCTOR      │    │    PATIENT      │
│   (Reception)   │    │   (Radiologist) │    │   (End User)    │
│                 │    │                 │    │                 │
│ • Patient Reg   │    │ • MRI Analysis  │    │ • Receive Email │
│ • View Reports  │    │ • View Results  │    │ • View Reports  │
│ • Contact Dev   │    │ • Send Reports  │    │ • Contact Info  │
│ • Dashboard     │    │ • Dashboard     │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔐 Authentication Flow

```
┌─────────────────┐
│   Login Page    │
│   (index.html)  │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Enter Creds    │
│ • National ID   │
│ • Name          │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Validate Role  │
│ • D### = Doctor │
│ • R### = Admin  │
│ • 14 digits =   │
│   Patient (❌)  │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Redirect Based │
│  on Role        │
└─────────┬───────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌─────────┐ ┌─────────┐
│ Doctor  │ │ Admin   │
│Dashboard│ │Dashboard│
└─────────┘ └─────────┘
```

## 🏥 Doctor Workflow

```
┌─────────────────┐
│ Doctor Dashboard│
│(doctor-home.html)│
└─────────┬───────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌─────────┐ ┌─────────┐
│ MRI     │ │ Patient │
│Analysis │ │ Data    │
└─────────┘ └─────────┘
    │           │
    ▼           ▼
┌─────────────────────────────────┐
│        MRI Analysis             │
│      (mri-analysis.html)        │
│                                 │
│ 1. Enter Patient ID             │
│ 2. Upload MRI Image             │
│ 3. Click "Analyze MRI"          │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      Backend Processing         │
│                                 │
│ 1. Validate Input               │
│ 2. Save MRI Image               │
│ 3. Run ML Prediction            │
│ 4. Generate Caption (BioMedCLIP)│
│ 5. Generate Report (Mistral)    │
│ 6. Save Results                 │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│     Analysis Result Page        │
│    (analysis_result.html)       │
│                                 │
│ • Patient Information           │
│ • Doctor Information            │
│ • MRI Image                     │
│ • Medical Report                │
│ • Print to PDF Button           │
│ • Send to Patient Button        │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      Email System               │
│                                 │
│ 1. Click "Send to Patient"      │
│ 2. Confirm Action               │
│ 3. Generate HTML Email          │
│ 4. Send via Gmail SMTP          │
│ 5. Patient Receives Report      │
└─────────────────────────────────┘
```

## 👨‍⚕️ Admin Workflow

```
┌─────────────────┐
│ Admin Dashboard │
│(receptionist-   │
│ home.html)      │
└─────────┬───────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌─────────┐ ┌─────────┐
│ Patient │ │ Contact │
│ Signup  │ │ Dev     │
└─────────┘ └─────────┘
    │           │
    ▼           ▼
┌─────────────────────────────────┐
│      Patient Registration       │
│      (signup-patient.html)      │
│                                 │
│ 1. Enter Patient Details        │
│    • National ID (14 digits)    │
│    • Name                       │
│    • Age                        │
│    • Gender                     │
│    • Email                      │
│    • Phone                      │
│ 2. Click "Register Patient"     │
│ 3. Patient Added to Database    │
└─────────────────────────────────┘
```

## 📧 Email System Flow

```
┌─────────────────────────────────┐
│      Email Configuration        │
│                                 │
│ • Gmail: brainscanhub001@gmail.com│
│ • App Password: qvtj tusr ctgb wtwo│
│ • SMTP: smtp.gmail.com:587      │
│ • TLS: Enabled                  │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      Email Template             │
│   (email_report_template.html)  │
│                                 │
│ • Brain Scan Hub Header         │
│ • Patient Information           │
│ • Analysis Details              │
│ • Medical Report                │
│ • Sender Information            │
│ • Contact Buttons               │
│ • Medical Disclaimer            │
│ • Professional Footer           │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      Email Sending Process      │
│                                 │
│ 1. Doctor clicks "Send to Patient"│
│ 2. System checks patient email  │
│ 3. Generates HTML email         │
│ 4. Creates plain text version   │
│ 5. Sends via Django send_mail() │
│ 6. Gmail SMTP delivers email    │
│ 7. Patient receives report      │
└─────────────────────────────────┘
```

## 🤖 Machine Learning Pipeline

```
┌─────────────────────────────────┐
│      MRI Image Upload           │
│                                 │
│ • User uploads MRI image        │
│ • Image saved to media/         │
│ • File path: mri.image.path     │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      Image Prediction           │
│    (Prediction_Script.py)       │
│                                 │
│ • Load trained PyTorch model    │
│ • Preprocess MRI image          │
│ • Run segmentation              │
│ • Return processed image        │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      BioMedCLIP Caption         │
│       (biomedclip.py)           │
│                                 │
│ • Load BioMedCLIP model         │
│ • Process segmented image       │
│ • Generate medical caption      │
│ • Return text description       │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      Report Generation          │
│    (report_generator.py)        │
│                                 │
│ • Use OpenRouter API            │
│ • Model: mistral-7b-instruct    │
│ • Fallback: devstral-small:free │
│ • Generate medical report       │
│ • No doctor info in report      │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│      Database Storage           │
│                                 │
│ • Save MRI_Image record         │
│ • Save Result record            │
│ • Link to patient & doctor      │
│ • Store report text             │
└─────────────────────────────────┘
```

## 🗄️ Database Schema

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│      User       │    │     Doctor      │    │     Patient     │
│                 │    │                 │    │                 │
│ • national_id   │◄───┤ • user (FK)     │    │ • user (FK)     │
│ • name          │    │ • specialty     │◄───┤ • doctor (FK)   │
│ • email         │    │                 │    │ • gender        │
│ • role          │    │                 │    │ • Age           │
│ • Ph_No         │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   MRI_Image     │    │     Result      │    │   ContactUs     │
│                 │    │                 │    │                 │
│ • doctor (FK)   │    │ • mri_image (FK)│    │ • user (FK)     │
│ • patient (FK)  │    │ • patient (FK)  │    │ • issue_type    │
│ • image         │    │ • doctor (FK)   │    │ • issue_title   │
│ • date          │    │ • report        │    │ • priority_level│
│                 │    │ • date          │    │ • message       │
│                 │    │                 │    │ • date          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔄 Complete User Journey

```
┌─────────────────┐
│   User Login    │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Role Check     │
└─────────┬───────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌─────────┐ ┌─────────┐
│ Doctor  │ │ Admin   │
│Journey  │ │Journey  │
└─────────┘ └─────────┘
    │           │
    ▼           ▼
┌─────────┐ ┌─────────┐
│ MRI     │ │ Patient │
│Analysis │ │ Signup  │
└─────────┘ └─────────┘
    │           │
    ▼           ▼
┌─────────┐ ┌─────────┐
│ Upload  │ │ Enter   │
│ Image   │ │ Details │
└─────────┘ └─────────┘
    │           │
    ▼           ▼
┌─────────┐ ┌─────────┐
│ Process │ │ Save    │
│ Analysis│ │ Patient │
└─────────┘ └─────────┘
    │           │
    ▼           ▼
┌─────────┐ ┌─────────┐
│ View    │ │ Success │
│ Results │ │ Message │
└─────────┘ └─────────┘
    │           │
    ▼           ▼
┌─────────┐ ┌─────────┐
│ Send    │ │ Back to │
│ Email   │ │ Dashboard│
└─────────┘ └─────────┘
    │
    ▼
┌─────────┐
│ Patient │
│ Receives│
│ Email   │
└─────────┘
```

## 🛡️ Security & Validation

```
┌─────────────────────────────────┐
│      Security Measures          │
│                                 │
│ • @login_required decorator     │
│ • Role-based access control     │
│ • CSRF protection               │
│ • Input validation              │
│ • File upload restrictions      │
│ • Email validation              │
│ • Error handling                │
└─────────────────────────────────┘
```

## 📱 File Structure

```
Brain Scan Hub/
├── BrainProject/                 # Django project
│   ├── settings.py              # Email config, database
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # WSGI configuration
├── Brainapp/                    # Main Django app
│   ├── models.py                # Database models
│   ├── views.py                 # All view logic
│   ├── urls.py                  # App URL routing
│   ├── ML/                      # Machine Learning
│   │   ├── Prediction_Script.py # Image segmentation
│   │   ├── biomedclip.py        # Image captioning
│   │   └── report_generator.py  # Report generation
│   ├── static/                  # CSS, JS, images
│   │   ├── css/
│   │   └── js/
│   └── templates/Brainapp/      # HTML templates
│       ├── index.html           # Login page
│       ├── doctor-home.html     # Doctor dashboard
│       ├── mri-analysis.html    # MRI upload form
│       ├── analysis_result.html # Results display
│       └── email_report_template.html # Email template
├── media/                       # Uploaded images
├── image/                       # Processed images
└── manage.py                    # Django management
```

## 🎯 Key Features Summary

- **🔐 Multi-role Authentication**: Admin, Doctor, Patient roles
- **🤖 AI-Powered Analysis**: ML segmentation + BioMedCLIP + Mistral
- **📧 Email Integration**: Professional HTML email reports
- **📊 Patient Management**: Registration and data tracking
- **🖨️ Report Generation**: Print-friendly PDF reports
- **📱 Responsive Design**: Works on all devices
- **🛡️ Security**: Role-based access, CSRF protection
- **💾 Database**: SQLite with proper relationships

This system provides a complete MRI analysis workflow from patient registration to report delivery via email! 