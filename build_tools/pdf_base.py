import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.saveState()
                self.setFont('Helvetica', 7.5)
                self.setFillColor(colors.HexColor('#64748b'))
                
                # Running Header
                doc_title = getattr(self, 'doc_header_title', 'COPYRIGHT REGISTRATION DOCUMENTATION')
                self.drawString(36, 810, doc_title.upper())
                self.drawRightString(559, 810, "ARB SOFTTECH • ENTERPRISE VOICE AI (FRONTEND)")
                
                self.setStrokeColor(colors.HexColor('#cbd5e1'))
                self.setLineWidth(0.5)
                self.line(36, 804, 559, 804)
                
                # Running Footer
                self.line(36, 38, 559, 38)
                self.drawString(36, 26, "GOVERNMENT OF INDIA • COPYRIGHT OFFICE • FORM XIV STATUTORY DEPOSIT")
                page_str = f"Page {self._pageNumber} of {num_pages}"
                self.drawRightString(559, 26, page_str)
                self.restoreState()
            super().showPage()
        super().save()

def get_copyright_styles():
    styles = getSampleStyleSheet()
    
    # Custom Palette
    c_primary = colors.HexColor('#0f172a')
    c_accent = colors.HexColor('#1e40af')
    c_body = colors.HexColor('#1e293b')
    c_muted = colors.HexColor('#64748b')
    
    styles.add(ParagraphStyle(
        name='CoverPreTitle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2563eb'),
        alignment=1, # Center
        spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        name='CoverTitle',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=c_primary,
        alignment=1,
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name='CoverSubTitle',
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=c_muted,
        alignment=1,
        spaceAfter=20
    ))
    styles.add(ParagraphStyle(
        name='DocH1',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=c_primary,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='DocH2',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=c_accent,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='DocH3',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=c_body,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='DocBody',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=c_body,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='DocBodyBold',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=c_body,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='DocBullet',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=c_body,
        leftIndent=15,
        spaceAfter=3
    ))
    styles.add(ParagraphStyle(
        name='CalloutText',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0f172a')
    ))
    styles.add(ParagraphStyle(
        name='CodeListing',
        fontName='Courier',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#0f172a'),
        leftIndent=0,
        rightIndent=0
    ))
    styles.add(ParagraphStyle(
        name='CodeHeader',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#1e40af'),
        spaceBefore=4,
        spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        name='TableHead',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=0
    ))
    styles.add(ParagraphStyle(
        name='TableCell',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=c_body,
        alignment=0
    ))
    styles.add(ParagraphStyle(
        name='TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=c_body,
        alignment=0
    ))
    
    return styles

def create_callout(text, styles, title="STATUTORY DISCLOSURE / LEGAL NOTICE"):
    content = [
        Paragraph(f"<b>{title}</b>", styles['DocH3']),
        Spacer(1, 2),
        Paragraph(text, styles['CalloutText'])
    ]
    t = Table([[content]], colWidths=[523])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('LINELEFT', (0,0), (0,-1), 3.5, colors.HexColor('#2563eb')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

def create_cover_page(styles, doc_number_text, doc_title_text, doc_desc_text):
    elements = []
    elements.append(Spacer(1, 40))
    elements.append(Paragraph("GOVERNMENT OF INDIA • COPYRIGHT OFFICE", styles['CoverPreTitle']))
    elements.append(Paragraph("DEPARTMENT FOR PROMOTION OF INDUSTRY AND INTERNAL TRADE (DPIIT)", styles['CoverPreTitle']))
    elements.append(Spacer(1, 15))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceBefore=0, spaceAfter=25))
    
    elements.append(Paragraph("APPLICATION FOR COPYRIGHT REGISTRATION — FORM XIV", styles['CoverPreTitle']))
    elements.append(Paragraph(doc_number_text.upper(), styles['DocH2']))
    elements.append(Paragraph(doc_title_text, styles['CoverTitle']))
    elements.append(Paragraph(doc_desc_text, styles['CoverSubTitle']))
    
    elements.append(HRFlowable(width="60%", thickness=2, color=colors.HexColor('#2563eb'), spaceBefore=10, spaceAfter=25))
    
    meta_table_data = [
        [Paragraph("<b>Statutory Category:</b>", styles['TableCellBold']), Paragraph("Computer Software / Literary Work (Section 2(o), Copyright Act, 1957)", styles['TableCell'])],
        [Paragraph("<b>Software Title:</b>", styles['TableCellBold']), Paragraph("ARB SoftTech AI Enterprise Voice Calling Agent Platform — Frontend Software", styles['TableCell'])],
        [Paragraph("<b>Application Package:</b>", styles['TableCellBold']), Paragraph("voxora-enterprise-ai-voice (Version 2.0.0 Production)", styles['TableCell'])],
        [Paragraph("<b>Languages & Tech:</b>", styles['TableCellBold']), Paragraph("TypeScript (v5.6.3), JavaScript (ES2022), React 18.3.1, Vite 6, Tailwind CSS", styles['TableCell'])],
        [Paragraph("<b>Target Authority:</b>", styles['TableCellBold']), Paragraph("Registrar of Copyrights, Copyright Office, New Delhi, India", styles['TableCell'])],
        [Paragraph("<b>Statutory Mandate:</b>", styles['TableCellBold']), Paragraph("Deposit under Rule 70(5), Copyright Rules, 2013 (First 10 & Last 10 Pages Format)", styles['TableCell'])],
        [Paragraph("<b>Date of Compilation:</b>", styles['TableCellBold']), Paragraph("October 2026", styles['TableCell'])],
    ]
    t = Table(meta_table_data, colWidths=[150, 373])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(t)
    
    elements.append(Spacer(1, 40))
    legal_warning = (
        "CONFIDENTIAL STATUTORY SUBMISSION: This official documentation package is prepared strictly for submission "
        "to the Registrar of Copyrights, Government of India, under Section 45 of the Copyright Act, 1957. "
        "All proprietary source code, user interface designs, and architecture representations herein reflect "
        "original works of authorship. Third-party open-source libraries are disclaimed under Section 52."
    )
    elements.append(create_callout(legal_warning, styles, "OFFICIAL NOTICE OF COPYRIGHT DEPOSIT"))
    elements.append(PageBreak())
    return elements

