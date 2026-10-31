import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, PageBreak, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from pdf_base import NumberedCanvas, get_copyright_styles, create_callout, create_cover_page

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DOCS_DIR = os.path.join(ROOT_DIR, 'COPYRIGHT_DOCUMENTATION')
OUTPUT_PDF = os.path.join(DOCS_DIR, '05_Development_Ownership_Declaration.pdf')

def generate_pdf():
    styles = get_copyright_styles()
    
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=38,
        bottomMargin=42
    )
    
    story = []
    
    # -------------------------------------------------------------------------
    # COVER PAGE
    # -------------------------------------------------------------------------
    story.extend(create_cover_page(
        styles,
        doc_number_text="DOCUMENT 05",
        doc_title_text="DEVELOPMENT & OWNERSHIP DECLARATION",
        doc_desc_text="Statutory Ownership, Human Authorship Identification, AI-Assisted Tool Disclosure,\nand Formal Verification Statement for Form XIV Registration"
    ))
    
    # -------------------------------------------------------------------------
    # SECTION 1: SOFTWARE & APPLICATION PARTICULARS
    # -------------------------------------------------------------------------
    story.append(Paragraph("1. SOFTWARE APPLICATION PARTICULARS", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    p1 = (
        "This structured statutory declaration is executed in connection with the Application for Registration of "
        "Copyright (Form XIV) submitted to the Registrar of Copyrights, Government of India, under the Copyright Act, "
        "1957 and Copyright Rules, 2013 (as amended)."
    )
    story.append(Paragraph(p1, styles['DocBody']))
    
    t1_data = [
        [Paragraph("Parameter", styles['TableHead']), Paragraph("Particulars / Formal Record", styles['TableHead'])],
        [Paragraph("<b>Title of the Work</b>", styles['TableCellBold']), Paragraph("ARB SoftTech AI Enterprise Voice Calling Agent Platform — Frontend Software", styles['TableCell'])],
        [Paragraph("<b>Package Identifier</b>", styles['TableCellBold']), Paragraph("voxora-enterprise-ai-voice (Version 2.0.0 Production)", styles['TableCell'])],
        [Paragraph("<b>Statutory Category</b>", styles['TableCellBold']), Paragraph("Literary Work — Computer Software (Section 2(o) & Section 2(ffc), Copyright Act, 1957)", styles['TableCell'])],
        [Paragraph("<b>Nature of Software</b>", styles['TableCellBold']), Paragraph("Interactive Frontend Web Client / Telephony Voice Operations Console", styles['TableCell'])],
        [Paragraph("<b>Target Jurisdiction</b>", styles['TableCellBold']), Paragraph("Republic of India", styles['TableCell'])],
    ]
    t1 = Table(t1_data, colWidths=[150, 373])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t1)
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 2: CHRONOLOGICAL DEVELOPMENT TIMELINE & LOCATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("2. CHRONOLOGICAL DEVELOPMENT TIMELINE & GEOGRAPHIC LOCATION", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    timeline_note = (
        "<b>INSTRUCTIONS FOR APPLICANT:</b> Verify and insert the exact historical calendar dates and physical "
        "office address where development was undertaken. Do not alter without verifying employment/contract records."
    )
    story.append(create_callout(timeline_note, styles, "VERIFICATION MANDATE"))
    story.append(Spacer(1, 6))
    
    t2_data = [
        [Paragraph("Milestone / Parameter", styles['TableHead']), Paragraph("Declared Details (To be Verified / Completed by Applicant)", styles['TableHead'])],
        [Paragraph("<b>Date of Commencement</b>", styles['TableCellBold']), Paragraph("[___ / ___ / 2026] (e.g., 01st August 2026 — Date coding commenced)", styles['TableCell'])],
        [Paragraph("<b>Date of Completion</b>", styles['TableCellBold']), Paragraph("[30th October 2026] (Date production build v2.0.0 finalized)", styles['TableCell'])],
        [Paragraph("<b>Publication Status</b>", styles['TableCellBold']), Paragraph("[  ] Unpublished Proprietary Software    [  ] Published Software", styles['TableCell'])],
        [Paragraph("<b>Date of First Publication</b>", styles['TableCellBold']), Paragraph("[___ / ___ / 2026] (Applicable only if work is publicly distributed/published)", styles['TableCell'])],
        [Paragraph("<b>Country of First Publication</b>", styles['TableCellBold']), Paragraph("Republic of India", styles['TableCell'])],
        [Paragraph("<b>Development Location</b>", styles['TableCellBold']), Paragraph("[Registered Office / Lab Address, City, State, PIN Code, India]", styles['TableCell'])],
    ]
    t2 = Table(t2_data, colWidths=[150, 373])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t2)
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 3: HUMAN AUTHORSHIP IDENTIFICATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("3. HUMAN AUTHORSHIP IDENTIFICATION & CONTRIBUTION DETAILS", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    author_legal_basis = (
        "Under Section 2(d)(i) of the Indian Copyright Act, 1957, the 'author' of a literary work (including a computer programme) "
        "must be a <b>natural human person</b>. Autonomous AI systems (such as Google Antigravity) cannot be named as legal authors. "
        "The human engineer(s) who exercised intellectual direction, architectural conception, and creative selection must be "
        "enumerated below:"
    )
    story.append(Paragraph(author_legal_basis, styles['DocBody']))
    story.append(Spacer(1, 4))
    
    t3_data = [
        [Paragraph("Author Particulars Field", styles['TableHead']), Paragraph("Author 1 Details [To be Completed by Applicant]", styles['TableHead'])],
        [Paragraph("<b>Full Legal Name</b>", styles['TableCellBold']), Paragraph("[Full Legal Name of Software Engineer / Architect]", styles['TableCell'])],
        [Paragraph("<b>Designation / Role</b>", styles['TableCellBold']), Paragraph("[e.g., Lead Frontend Architect / Senior Software Engineer]", styles['TableCell'])],
        [Paragraph("<b>Residential Address</b>", styles['TableCellBold']), Paragraph("[Complete Residential Address, City, State, PIN Code]", styles['TableCell'])],
        [Paragraph("<b>Nationality</b>", styles['TableCellBold']), Paragraph("Indian [or state other nationality]", styles['TableCell'])],
        [Paragraph("<b>PAN / Identification No.</b>", styles['TableCellBold']), Paragraph("[Permanent Account Number / Govt ID Number]", styles['TableCell'])],
        [Paragraph("<b>Nature of Contribution</b>", styles['TableCellBold']), Paragraph("Conception of frontend architecture, prompt engineering, integration of telephony state, design of dual-look layout, and code verification.", styles['TableCell'])],
    ]
    t3 = Table(t3_data, colWidths=[150, 373])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t3)
    story.append(PageBreak())
    
    # -------------------------------------------------------------------------
    # SECTION 4: APPLICANT / PROPOSED COPYRIGHT OWNER DETAILS
    # -------------------------------------------------------------------------
    story.append(Paragraph("4. APPLICANT / PROPOSED COPYRIGHT OWNER DETAILS (FORM XIV COL 2)", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    t4_data = [
        [Paragraph("Applicant Entity Parameter", styles['TableHead']), Paragraph("Entity Record Details [To be Completed by Applicant]", styles['TableHead'])],
        [Paragraph("<b>Full Name of Applicant Entity</b>", styles['TableCellBold']), Paragraph("[e.g., ARB SoftTech Private Limited / Firm / Individual Name]", styles['TableCell'])],
        [Paragraph("<b>Legal Constitution</b>", styles['TableCellBold']), Paragraph("[Private Limited Company / LLP / Partnership / Sole Proprietorship]", styles['TableCell'])],
        [Paragraph("<b>Registered Office Address</b>", styles['TableCellBold']), Paragraph("[Complete Registered Office Address, City, State, PIN Code, India]", styles['TableCell'])],
        [Paragraph("<b>Corporate Identity No. (CIN)</b>", styles['TableCellBold']), Paragraph("[CIN / Registration Number / MSME Udyam Number]", styles['TableCell'])],
        [Paragraph("<b>GSTIN / Entity PAN</b>", styles['TableCellBold']), Paragraph("[Goods and Services Tax Identification Number / PAN]", styles['TableCell'])],
        [Paragraph("<b>Authorized Signatory Name</b>", styles['TableCellBold']), Paragraph("[Name of Director / Managing Partner / Authorized Officer]", styles['TableCell'])],
        [Paragraph("<b>Official Contact Email & Phone</b>", styles['TableCellBold']), Paragraph("[Official Email ID] | [Official Mobile Phone Number]", styles['TableCell'])],
    ]
    t4 = Table(t4_data, colWidths=[150, 373])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t4)
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 5: NATURE OF OWNERSHIP & ASSIGNMENT (CHAIN OF TITLE)
    # -------------------------------------------------------------------------
    story.append(Paragraph("5. NATURE OF OWNERSHIP & ASSIGNMENT (CHAIN OF TITLE)", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    ownership_text = (
        "The Applicant holds proprietary copyright ownership in the software through the following statutory mechanism "
        "(check the applicable statutory ground):<br/><br/>"
        "<b>[  ] GROUND A: WORK MADE FOR HIRE UNDER SECTION 17(c) OF THE COPYRIGHT ACT, 1957</b><br/>"
        "The human author(s) created the software in the course of their regular employment with the Applicant "
        "under a contract of service. Under Section 17(c), the Applicant is the first owner of the copyright.<br/><br/>"
        "<b>[  ] GROUND B: ASSIGNMENT DEED UNDER SECTION 19 OF THE COPYRIGHT ACT, 1957</b><br/>"
        "The human author(s) executed a formal, written Copyright Assignment Deed transferring all intellectual property "
        "rights, title, and interest in the software to the Applicant in exchange for lawful consideration.<br/><br/>"
        "<b>[  ] GROUND C: INDIVIDUAL OWNERSHIP</b><br/>"
        "The author is applying directly in their individual capacity as sole proprietor/owner.<br/><br/>"
        "<b>MANDATORY ENCLOSURE:</b> An executed No Objection Certificate (NOC) from the author(s) in Form XIV format "
        "must accompany this submission when filing under Ground A or Ground B."
    )
    story.append(Paragraph(ownership_text, styles['DocBody']))
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 6: STATUTORY AI-ASSISTED DEVELOPMENT DISCLOSURE
    # -------------------------------------------------------------------------
    story.append(Paragraph("6. STATUTORY AI-ASSISTED DEVELOPMENT DISCLOSURE", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    ai_disclosure_formal = (
        "<b>FORMAL STATUTORY DECLARATION REGARDING GOOGLE ANTIGRAVITY:</b><br/>"
        "1. The Applicant and Author(s) hereby solemnly affirm and disclose that <b>Google Antigravity</b>, an advanced "
        "agentic AI coding tool, was utilized during the development of this frontend software application.<br/>"
        "2. Google Antigravity operated strictly as a computational development tool under human supervision and prompt guidance.<br/>"
        "3. The human author(s) formulated the technical blueprints, system requirements, component architecture, data contracts, "
        "and prompt logic; directed code synthesis; reviewed, curated, and debugged all generated code; and performed integration testing.<br/>"
        "4. In strict compliance with Indian Copyright Office circulars, copyright is claimed exclusively by the human creator(s) and "
        "their employer/assignee over the original creative selection, coordination, and arrangement of instructions."
    )
    story.append(create_callout(ai_disclosure_formal, styles, "STATUTORY AI-TOOL DISCLOSURE"))
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 7: THIRD-PARTY OPEN-SOURCE DISCLAIMER
    # -------------------------------------------------------------------------
    story.append(Paragraph("7. THIRD-PARTY DEPENDENCIES & OPEN-SOURCE CARVE-OUTS", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    os_text = (
        "The Applicant and Author(s) confirm that all third-party libraries (including React, Vite, Tailwind CSS, Recharts, "
        "Axios, and date-fns) are incorporated under their respective permissive open-source licenses (MIT/Apache 2.0). "
        "The Applicant expressly disclaims proprietary copyright over all third-party libraries, in conformity with Section 52 "
        "of the Copyright Act, 1957. Detailed license records are set forth in <code>THIRD_PARTY_DEPENDENCIES.md</code>."
    )
    story.append(Paragraph(os_text, styles['DocBody']))
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 8: SOLEMN AFFIRMATION & SIGNATURE VERIFICATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("8. SOLEMN AFFIRMATION & VERIFICATION BLOCK", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    affidavit_text = (
        "I/We, the undersigned, do hereby solemnly affirm, state, and declare that the contents of this declaration "
        "are true and correct to the best of my/our knowledge, information, and belief; that no material fact has been "
        "concealed or misrepresented; that the software described herein is an original work of computer software; "
        "and that the Applicant is entitled to proprietary registration under the Indian Copyright Act, 1957."
    )
    story.append(Paragraph(affidavit_text, styles['DocBody']))
    story.append(Spacer(1, 15))
    
    sig_table = [
        [Paragraph("<b>SOLEMNLY AFFIRMED BY AUTHOR(S):</b>", styles['TableCellBold']), Paragraph("<b>SIGNED FOR & ON BEHALF OF APPLICANT:</b>", styles['TableCellBold'])],
        [Spacer(1, 40), Spacer(1, 40)],
        [
            Paragraph("____________________________________________<br/><b>Signature of Human Author</b><br/>Name: [Author Full Legal Name]<br/>Date: [DD / MM / 2026]<br/>Place: [City, State, India]", styles['TableCell']),
            Paragraph("____________________________________________<br/><b>Signature of Authorized Signatory</b><br/>Name: [Signatory Full Name]<br/>Designation: [Director / Partner]<br/>Seal of Entity / Company<br/>Date: [DD / MM / 2026]", styles['TableCell'])
        ]
    ]
    t_sig = Table(sig_table, colWidths=[261, 262])
    t_sig.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_sig)
    
    class OwnNumberedCanvas(NumberedCanvas):
        doc_header_title = "DOCUMENT 05: DEVELOPMENT & OWNERSHIP DECLARATION"
        
    doc.build(story, canvasmaker=OwnNumberedCanvas)
    print(f"Generated 05_Development_Ownership_Declaration.pdf successfully at {OUTPUT_PDF}")

if __name__ == '__main__':
    generate_pdf()

