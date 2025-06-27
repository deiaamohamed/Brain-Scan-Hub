#!/usr/bin/env python
"""
Test Email Configuration for Brain Scan Hub
Run this script to test if your email settings are working correctly.
"""

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BrainProject.settings')
django.setup()

from django.core.mail import send_mail

def test_email_configuration():
    """Test the email configuration"""
    print("🧠 Testing Brain Scan Hub Email Configuration")
    print("=" * 50)
    
    # Check email settings
    print(f"Email Backend: {settings.EMAIL_BACKEND}")
    print(f"Email Host: {settings.EMAIL_HOST}")
    print(f"Email Port: {settings.EMAIL_PORT}")
    print(f"Email User: {settings.EMAIL_HOST_USER}")
    print(f"Use TLS: {settings.EMAIL_USE_TLS}")
    print(f"From Email: {settings.DEFAULT_FROM_EMAIL}")
    print()
    
    # Test email sending
    try:
        print("📧 Sending test email...")
        
        # Create a simple test email
        subject = "🧠 Brain Scan Hub - Email Test"
        message = """
        This is a test email from Brain Scan Hub.
        
        If you receive this email, your email configuration is working correctly!
        
        Best regards,
        Brain Scan Hub Team
        """
        
        # Send test email to yourself
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['brainscanhub001@gmail.com'],  # Send to yourself
            fail_silently=False,
        )
        
        print("✅ Test email sent successfully!")
        print("📬 Check your inbox: brainscanhub001@gmail.com")
        
    except Exception as e:
        print(f"❌ Error sending test email: {str(e)}")
        print()
        print("🔧 Troubleshooting tips:")
        print("1. Check your email credentials in settings.py")
        print("2. For Gmail, make sure you're using an App Password")
        print("3. Enable 2-Factor Authentication on your Gmail account")
        print("4. Check if your email provider allows SMTP access")
        print("5. Try using a different email provider")

if __name__ == "__main__":
    test_email_configuration() 