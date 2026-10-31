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
OUTPUT_PDF = os.path.join(DOCS_DIR, '01_Project_Description.pdf')

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
        doc_number_text="DOCUMENT 01",
        doc_title_text="SOFTWARE PROJECT DESCRIPTION",
        doc_desc_text="Comprehensive Technical & Statutory Specification of the Frontend Software\nSubmitted in Support of Copyright Registration (Form XIV)"
    ))
    
    # -------------------------------------------------------------------------
    # SECTION 1: STATUTORY CLASSIFICATION & METADATA
    # -------------------------------------------------------------------------
    story.append(Paragraph("1. STATUTORY SOFTWARE IDENTIFICATION & CLASSIFICATION", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    s1_text = (
        "This project description is formally submitted pursuant to Rule 70 of the Copyright Rules, 2013 "
        "accompanying Form XIV (Application for Registration of Copyright) before the Registrar of Copyrights, "
        "Department for Promotion of Industry and Internal Trade (DPIIT), New Delhi, India. "
        "The subject matter of registration is an original computer software work comprising the interactive "
        "frontend client application for enterprise telephony voice operations."
    )
    story.append(Paragraph(s1_text, styles['DocBody']))
    
    meta_table = [
        [Paragraph("Statutory Parameter", styles['TableHead']), Paragraph("Particulars / Formal Record", styles['TableHead'])],
        [Paragraph("<b>Title of the Work</b>", styles['TableCellBold']), Paragraph("ARB SoftTech AI Enterprise Voice Calling Agent Platform — Frontend Software", styles['TableCell'])],
        [Paragraph("<b>Statutory Category</b>", styles['TableCellBold']), Paragraph("Literary Work — Computer Software under Section 2(o) & Section 2(ffc) of the Copyright Act, 1957", styles['TableCell'])],
        [Paragraph("<b>Package Identifier</b>", styles['TableCellBold']), Paragraph("voxora-enterprise-ai-voice (Version 2.0.0 Production)", styles['TableCell'])],
        [Paragraph("<b>Primary Languages</b>", styles['TableCellBold']), Paragraph("TypeScript (v5.6.3), JavaScript (ES2022 / ECMAScript Modules), HTML5, CSS3", styles['TableCell'])],
        [Paragraph("<b>Core Architecture</b>", styles['TableCellBold']), Paragraph("Client-side Single Page Application (SPA) built on React 18.3.1 and Vite 6.0.5", styles['TableCell'])],
        [Paragraph("<b>Codebase Scope</b>", styles['TableCellBold']), Paragraph("118 original source files | 23,552 lines of code | 941 KB source size (excluding node_modules)", styles['TableCell'])],
        [Paragraph("<b>Jurisdiction & Location</b>", styles['TableCellBold']), Paragraph("Republic of India", styles['TableCell'])],
    ]
    t_meta = Table(meta_table, colWidths=[150, 373])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 2: PURPOSE OF THE SOFTWARE & EXECUTIVE OVERVIEW
    # -------------------------------------------------------------------------
    story.append(Paragraph("2. PURPOSE OF THE SOFTWARE & EXECUTIVE OVERVIEW", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    p2_desc = (
        "The <b>ARB SoftTech AI Enterprise Voice Calling Agent Platform (Frontend Software)</b> is an enterprise-grade "
        "web-based operational console designed to configure, monitor, dispatch, and analyze autonomous AI-driven "
        "PSTN telephone calls. The platform bridges complex telecommunications carrier trunks (VoBiz, Twilio) "
        "and conversational artificial intelligence models (Sarvam AI for multilingual Indic speech and Google Gemini "
        "for post-call lead qualification) into an intuitive, high-performance visual dashboard."
    )
    story.append(Paragraph(p2_desc, styles['DocBody']))
    
    p2_bullets = [
        "<b>Real-Time Telephonic Telemetry:</b> Sub-second polling and WebSocket state visualization for concurrent ongoing mobile/landline telephone calls across Indian and global PSTN networks.",
        "<b>Conversational Voice Agent Workspace:</b> Visual prompt engineering workbench allowing non-technical operators to create custom voice personas, tune speech temperature, set interruptibility delays, and assign Hindi (Devanagari) or Indic acoustic models.",
        "<b>Lead Intelligence Pipeline:</b> Automated visualization of post-call conversation analytics, extracting customer names, phone numbers, locations, budgets, and callback times, accompanied by hoverable AI reasoning chips.",
        "<b>Interactive Branching Questionnaire Builder:</b> Dynamic flowchart editor allowing business users to define multi-turn conversational question logic with bulk Excel (.xlsx) and Word (.docx) import capabilities.",
        "<b>Dual Look Visual Architecture:</b> A proprietary design system permitting seamless real-time switching between a corporate 'Classic Enterprise' layout and a futuristic 'Modern High-Tech' dark glassmorphic cockpit."
    ]
    for b in p2_bullets:
        story.append(Paragraph(f"• {b}", styles['DocBullet']))
    story.append(Spacer(1, 8))
    
    # -------------------------------------------------------------------------
    # SECTION 3: FUNCTIONAL MODULES SPECIFICATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("3. MAJOR FUNCTIONAL MODULES & SUBSYSTEMS", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    modules_info = [
        ("Module 1: Dashboard & Live Telemetry", "src/features/dashboard/, src/components/ui/MetricCard.tsx",
         "Presents high-level operational metrics including aggregate call volume, connection rates, total minutes consumed, and lead conversion rates. Features animated Recharts graphics, active agent popovers, and quick-dispatch call buttons."),
        ("Module 2: AI Voice Agent Studio", "src/features/agents/, AgentFormDrawer.tsx, AgentWorkspacePage.tsx",
         "A comprehensive workspace for authoring voice agents. Features multilingual TTS persona selectors (Sarvam AI Shubh, Ritu, Aditya), LLM prompt templates, barge-in sensitivity sliders, temperature tuning, and one-click PDF dossier export."),
        ("Module 3: Active Ongoing Calls Monitor", "src/features/calls/ActiveCallsPage.tsx, QueuePage.tsx",
         "Real-time visual console displaying active call channels, connection durations, caller phone numbers, and live audio waveform animations."),
        ("Module 4: Historical Call Detail Records & Drawer", "src/features/calls/CallsPage.tsx, CallDetailDrawer.tsx",
         "Full CDR audit table with text search, date filtering, and client-side Excel export. Opening any call launches a lateral drawer with turn-by-turn speaker-diarized transcripts, AI interest reasoning, and embedded 8kHz WAV audio player."),
        ("Module 5: Lead Intelligence & Intent Pipeline", "src/features/leads/LeadsPage.tsx",
         "Interactive sales qualification kanban/table displaying customer profiles extracted from transcripts (Name, Email, City, Budget, Preferred Callback Time). Features why-interested reason chips with hoverable evidence tooltips."),
        ("Module 6: Conversational Questionnaire Engine", "src/features/questionnaires/, QuestionnaireEditorPage.tsx",
         "Interactive visual flow editor for branching conversational trees. Includes specialized modal parsers for bulk question import from Microsoft Excel (.xlsx) and Microsoft Word (.docx) files."),
        ("Module 7: Outbound PSTN Quick-Dial Modal", "src/components/layout/QuickDialModal.tsx, src/utils/quickDial.ts",
         "Global dialer modal allowing instant outbound phone call initiation to any mobile/landline number via backend carrier proxy dispatch."),
        ("Module 8: Telephony Carrier & AI Settings", "src/features/settings/, SarvamSettings.tsx, VoBizTelephonySettings.tsx",
         "Secure credential management interfaces for Sarvam AI speech models, VoBiz carrier trunks, Twilio SIP trunks, and Google Gemini transcript intelligence APIs."),
        ("Module 9: Model Lab & Latency Diagnostic Suite", "src/features/model_lab/ModelLabPage.tsx",
         "Specialized testing workbench allowing live voice model benchmarking, STT/TTS latency profiling, and telephony audio stream inspection."),
        ("Module 10: Multi-Tenant Business Administration", "src/features/businesses/, BusinessProvider.tsx, BusinessSelector.tsx",
         "Multi-tenant workspace manager allowing operators to isolate telephony trunks, agents, and lead records by client entity, with PDF profile export."),
        ("Module 11: Follow-ups, Contacts & Invoicing", "src/features/followups/, src/features/contacts/, src/features/invoices/",
         "CRM contact book with DNC (Do-Not-Call) flags, scheduled callback task manager, and minute consumption invoicing module."),
        ("Module 12: Dual Look & Modern Visual Design System", "src/features/modern/, LookToggle.tsx, GlowProvider.tsx, ParticleStars.tsx",
         "Advanced styling engine providing 17 dedicated modern views, ambient radial gradients, interactive cursor glow effects, and HTML5 canvas particle stars.")
    ]
    
    for title, path_info, desc in modules_info:
        story.append(Paragraph(f"<b>{title}</b>", styles['DocH2']))
        story.append(Paragraph(f"<font color='#64748b' size=7.5>Source Path: {path_info}</font>", styles['DocBody']))
        story.append(Paragraph(desc, styles['DocBody']))
        story.append(Spacer(1, 2))
        
    story.append(PageBreak())
    
    # -------------------------------------------------------------------------
    # SECTION 4: TECHNOLOGY STACK & ARCHITECTURE
    # -------------------------------------------------------------------------
    story.append(Paragraph("4. TECHNOLOGY STACK & FRONTEND ARCHITECTURE", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    tech_table = [
        [Paragraph("Architectural Layer", styles['TableHead']), Paragraph("Technologies & Version", styles['TableHead']), Paragraph("Architectural Role & Justification", styles['TableHead'])],
        [Paragraph("<b>Language Runtime</b>", styles['TableCellBold']), Paragraph("TypeScript 5.6.3<br/>JavaScript (ES2022)", styles['TableCell']), Paragraph("Strongly-typed application logic, interface contracts, and compile-time AST validation.", styles['TableCell'])],
        [Paragraph("<b>UI Framework</b>", styles['TableCellBold']), Paragraph("React 18.3.1 (Virtual DOM)", styles['TableCell']), Paragraph("Declarative component hierarchy, concurrent rendering, and hook-based lifecycle.", styles['TableCell'])],
        [Paragraph("<b>Build & Bundler</b>", styles['TableCellBold']), Paragraph("Vite 6.0.5 + Rollup", styles['TableCell']), Paragraph("High-speed development server with HMR and optimized production bundle compilation.", styles['TableCell'])],
        [Paragraph("<b>Routing Engine</b>", styles['TableCellBold']), Paragraph("React Router DOM 6.28.1", styles['TableCell']), Paragraph("Client-side declarative routing, URL state synchronization, and dual-look page wrapping.", styles['TableCell'])],
        [Paragraph("<b>Server State</b>", styles['TableCellBold']), Paragraph("TanStack React Query 5.62.7", styles['TableCell']), Paragraph("Asynchronous caching, background telephony polling, and query invalidation.", styles['TableCell'])],
        [Paragraph("<b>Client State</b>", styles['TableCellBold']), Paragraph("Zustand 5.0.2 + React Context", styles['TableCell']), Paragraph("Global theme toggles, modal dialog triggers, and multi-tenant business context.", styles['TableCell'])],
        [Paragraph("<b>Design System</b>", styles['TableCellBold']), Paragraph("Tailwind CSS 3.4.17 + PostCSS", styles['TableCell']), Paragraph("Utility-first design tokens, custom dark-mode CSS variables, and glassmorphic styling.", styles['TableCell'])],
        [Paragraph("<b>Data Visualization</b>", styles['TableCellBold']), Paragraph("Recharts 2.15.0 + Lucide React", styles['TableCell']), Paragraph("Responsive SVG telephony graphs, call duration charts, and vector iconography.", styles['TableCell'])],
        [Paragraph("<b>Document Exports</b>", styles['TableCellBold']), Paragraph("jsPDF 4.2.1 + SheetJS (xlsx)", styles['TableCell']), Paragraph("Client-side dynamic generation of PDF agent dossiers and XLSX lead reports.", styles['TableCell'])],
        [Paragraph("<b>Deployment</b>", styles['TableCellBold']), Paragraph("Docker + Nginx Alpine", styles['TableCell']), Paragraph("Containerized production distribution with Nginx reverse proxy and SPA routing fallback.", styles['TableCell'])],
    ]
    t_tech = Table(tech_table, colWidths=[100, 130, 293])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_tech)
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 5: DEVELOPMENT METHODOLOGY & AI-ASSISTED DISCLOSURE
    # -------------------------------------------------------------------------
    story.append(Paragraph("5. DEVELOPMENT METHODOLOGY & AI-ASSISTED DISCLOSURE", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    dev_intro = (
        "In strict adherence to the principles of transparency and statutory compliance under the Indian Copyright "
        "Act, 1957, this section details the development methodology and the utilization of artificial intelligence "
        "tools during the engineering of the frontend client application."
    )
    story.append(Paragraph(dev_intro, styles['DocBody']))
    
    ai_callout = (
        "<b>STATUTORY DISCLOSURE ON GOOGLE ANTIGRAVITY USAGE:</b><br/>"
        "The frontend software was authored using <b>Google Antigravity</b>, an advanced agentic AI-assisted software "
        "engineering development environment.<br/><br/>"
        "<b>1. Status under Indian Copyright Law:</b> Under Section 2(d)(i) of the Indian Copyright Act, 1957, "
        "an author of a computer programme must be a natural human person. Google Antigravity is not claimed or "
        "identified as an author or co-author. It served strictly as a computational instrument and intelligent programming aid.<br/><br/>"
        "<b>2. Human Intellectual Effort & Originality:</b> Human software engineers conceived the product requirements, "
        "formulated architectural blueprints, designed user journeys, defined domain data models in <code>api.ts</code>, "
        "crafted customized natural language prompts, debugged integration failures, curated code outputs, and performed "
        "comprehensive end-to-end integration and verification. The creative selection, coordination, and arrangement of "
        "code elements reflect genuine human intellectual authorship protected under Section 13(1)(a)."
    )
    story.append(create_callout(ai_callout, styles, "AI-ASSISTED SOFTWARE AUTHORSHIP DISCLOSURE"))
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 6: THIRD-PARTY DEPENDENCIES & STATUTORY CARVE-OUTS
    # -------------------------------------------------------------------------
    story.append(Paragraph("6. THIRD-PARTY DEPENDENCIES & OPEN-SOURCE CARVE-OUTS", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    tp_text = (
        "The application integrates standardized open-source libraries (e.g. React, React Router, Vite, Axios, "
        "Tailwind CSS, Recharts) distributed under permissive open-source licenses (MIT, Apache 2.0). "
        "In compliance with Section 52 of the Indian Copyright Act, 1957 and official filing guidelines:<br/>"
        "• The Applicant <b>expressly disclaims</b> proprietary copyright over all third-party libraries.<br/>"
        "• Third-party code is excluded from the proprietary claim.<br/>"
        "• A complete inventory of all 19 runtime dependencies and 10 build tooling dependencies is recorded in "
        "<code>THIRD_PARTY_DEPENDENCIES.md</code>."
    )
    story.append(Paragraph(tp_text, styles['DocBody']))
    story.append(Spacer(1, 8))
    
    # -------------------------------------------------------------------------
    # SECTION 7: SCOPE OF COPYRIGHT CLAIMED
    # -------------------------------------------------------------------------
    story.append(Paragraph("7. SCOPE OF COPYRIGHT CLAIMED & LEGAL LIMITATIONS", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    scope_text = (
        "Copyright protection under Section 14(b) of the Indian Copyright Act, 1957 is claimed strictly over:<br/>"
        "1. <b>Original Source Code:</b> The original TypeScript, React, and CSS source code files authored for this platform.<br/>"
        "2. <b>User Interface Component Architecture:</b> The proprietary structural hierarchy of interactive components, modals, and drawers.<br/>"
        "3. <b>Telephony Integration Logic:</b> Custom state machines and REST/WebSocket integration routines managing PSTN voice operations.<br/>"
        "4. <b>Dynamic Visual Styling:</b> Custom ambient CSS animations, glow effects, and modern dual-look presentation layers.<br/>"
        "5. <b>Selection and Arrangement:</b> The creative coordination and compilation of modules into a unified enterprise voice calling platform."
    )
    story.append(Paragraph(scope_text, styles['DocBody']))
    story.append(Spacer(1, 16))
    
    # -------------------------------------------------------------------------
    # SECTION 8: FORM XIV MAPPING & STATUTORY DECLARATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("8. FORM XIV STATEMENT OF PARTICULARS REFERENCE MAPPING", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    form_mapping = [
        [Paragraph("Form XIV Column", styles['TableHead']), Paragraph("Statutory Query", styles['TableHead']), Paragraph("Formal Description / Document Reference", styles['TableHead'])],
        [Paragraph("<b>Col 2</b>", styles['TableCellBold']), Paragraph("Name & Address of Applicant", styles['TableCell']), Paragraph("Refer to Section 2 of 05_Development_Ownership_Declaration.pdf.", styles['TableCell'])],
        [Paragraph("<b>Col 4</b>", styles['TableCellBold']), Paragraph("Class & Description of Work", styles['TableCell']), Paragraph("Literary (Computer Software). Single Page Application for enterprise voice operations.", styles['TableCell'])],
        [Paragraph("<b>Col 5</b>", styles['TableCellBold']), Paragraph("Title of Work", styles['TableCell']), Paragraph("ARB SoftTech AI Enterprise Voice Calling Agent Platform — Frontend Software", styles['TableCell'])],
        [Paragraph("<b>Col 6</b>", styles['TableCellBold']), Paragraph("Language of Work", styles['TableCell']), Paragraph("TypeScript (v5.6.3), JavaScript (ES2022), HTML5, CSS3", styles['TableCell'])],
        [Paragraph("<b>Col 7</b>", styles['TableCellBold']), Paragraph("Name & Nationality of Author", styles['TableCell']), Paragraph("Natural human software engineer(s). Refer to Document 05.", styles['TableCell'])],
        [Paragraph("<b>Col 8 & 9</b>", styles['TableCellBold']), Paragraph("Publication Status", styles['TableCell']), Paragraph("Unpublished proprietary software / Completed October 2026 in India.", styles['TableCell'])],
        [Paragraph("<b>SoFP Col 1</b>", styles['TableCellBold']), Paragraph("Originality of Work", styles['TableCell']), Paragraph("Yes, an original computer software literary work authored for the applicant.", styles['TableCell'])],
        [Paragraph("<b>SoFP Col 3</b>", styles['TableCellBold']), Paragraph("Third-Party Materials", styles['TableCell']), Paragraph("Permissive open-source dependencies disclaimed under Section 52.", styles['TableCell'])],
    ]
    t_map = Table(form_mapping, colWidths=[80, 150, 293])
    t_map.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_map)
    story.append(Spacer(1, 20))
    
    # Signature block
    sig_block = [
        [Paragraph("<b>Prepared by:</b>", styles['TableCellBold']), Paragraph("<b>Verified on behalf of Applicant:</b>", styles['TableCellBold'])],
        [Spacer(1, 35), Spacer(1, 35)],
        [
            Paragraph("____________________________________________<br/>Senior Software Documentation Engineer<br/>Date: 31st October 2026", styles['TableCell']),
            Paragraph("____________________________________________<br/>Authorized Officer / Signatory<br/>For: ARB SoftTech", styles['TableCell'])
        ]
    ]
    t_sig = Table(sig_block, colWidths=[261, 262])
    t_sig.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_sig)
    
    class DescNumberedCanvas(NumberedCanvas):
        doc_header_title = "DOCUMENT 01: SOFTWARE PROJECT DESCRIPTION"
        
    doc.build(story, canvasmaker=DescNumberedCanvas)
    print(f"Generated 01_Project_Description.pdf successfully at {OUTPUT_PDF}")

if __name__ == '__main__':
    generate_pdf()

