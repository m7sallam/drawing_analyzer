import frappe
import cv2
import numpy as np
import os

@frappe.whitelist()
def calculate_area(file_url, scale_factor=1.0):
    # Get the physical path of the file on the server
    site_path = frappe.get_site_path()
    file_path = os.path.join(site_path, file_url.strip("/"))

    if not os.path.exists(file_path):
        frappe.throw(f"File not found at: {file_path}")

    # Load image for processing
    img = cv2.imread(file_path)
    if img is None:
        frappe.throw("OpenCV could not read the image. Use JPG or PNG.")

    # Image Processing (Grayscale -> Blur -> Edges)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    # Find the outlines
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return {"area": 0, "message": "No distinct shapes detected."}

    # Identify the largest closed shape
    largest_contour = max(contours, key=cv2.contourArea)
    pixel_area = cv2.contourArea(largest_contour)
    
    # Area = Pixels * (Scale Factor)^2
    real_area = pixel_area * (float(scale_factor) ** 2)

    return {
        "pixel_area": pixel_area,
        "real_area": round(real_area, 2),
        "message": "Area calculated successfully"
    }
