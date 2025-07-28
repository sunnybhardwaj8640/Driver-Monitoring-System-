from fpdf import FPDF
from datetime import datetime
import os

def generate_report(distractions, duration):
    # ✅ Ensure the folder exists before saving the PDF
    output_dir = "report_output"
    os.makedirs(output_dir, exist_ok=True)

    focus_score = max(100 - distractions * 5, 0)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Driver Monitoring Report", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.cell(200, 10, txt=f"Monitoring Duration: {duration} seconds", ln=True)
    pdf.cell(200, 10, txt=f"Distractions Detected: {distractions}", ln=True)
    pdf.cell(200, 10, txt=f"Focus Score: {focus_score}/100", ln=True)

    output_path = os.path.join(output_dir, "driver_report.pdf")
    pdf.output(output_path)
    print(f"[INFO] Report saved to {output_path}")
