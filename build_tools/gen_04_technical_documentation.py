import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, PageBreak, Spacer, Table, TableStyle, HRFlowable, Preformatted
)
from pdf_base import NumberedCanvas, get_copyright_styles, create_callout, create_cover_page

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DOCS_DIR = os.path.join(ROOT_DIR, 'COPYRIGHT_DOCUMENTATION')
OUTPUT_PDF = os.path.join(DOCS_DIR, '04_Technical_Documentation.pdf')

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
        doc_number_text="DOCUMENT 04",
        doc_title_text="SOFTWARE TECHNICAL DOCUMENTATION",
        doc_desc_text="Comprehensive Engineering Architecture, Component Hierarchy, Routing,\nState Management, and Telephony Integration Specification"
    ))
    
    # -------------------------------------------------------------------------
    # SECTION 1: ARCHITECTURAL SYSTEM DESIGN
    # -------------------------------------------------------------------------
    story.append(Paragraph("1. HIGH-LEVEL SOFTWARE ARCHITECTURAL DESIGN", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    arch_desc = (
        "The frontend application of the <b>ARB SoftTech AI Enterprise Voice Calling Agent Platform</b> is architected "
        "as a high-throughput, reactive Single Page Application (SPA) powered by React 18 and Vite 6. "
        "It acts as the presentation, orchestration, and telemetry layer for the underlying telecommunications "
        "backend (FastAPI, Sarvam AI telephony engine, and VoBiz/Twilio PSTN carriers)."
    )
    story.append(Paragraph(arch_desc, styles['DocBody']))
    
    arch_diagram = """
    +---------------------------------------------------------------------------------------+
    |                         CLIENT BROWSER LAYER (React 18 / SPA)                         |
    |                                                                                       |
    |  [Dual-Look View Engine] <======> [AppShell / ModernShell Navigation]                 |
    |          |                                      |                                     |
    |  [Feature Pages & Modals]             [Reusable UI Component Library]                 |
    |  (Agents, Calls, Leads, etc.)         (AudioPlayer, DataTable, Cards, Modals)         |
    |          |                                      |                                     |
    |  +---------------------------------------------------------------------------------+  |
    |  |                    STATE & TELEMETRY ORCHESTRATION LAYER                        |  |
    |  |  • AuthProvider (JWT Sessions)          • BusinessProvider (Multi-Tenant Org)   |  |
    |  |  • TanStack React Query (Server Cache)  • Zustand Store (UI Modals & Tabs)      |  |
    |  +---------------------------------------------------------------------------------+  |
    |          |                                      |                                     |
    |  [Axios REST Client / HTTP]              [WAV Audio Streamer / WebSockets]            |
    +----------|--------------------------------------|-------------------------------------+
               |                                      |
               v                                      v
    +---------------------------------------------------------------------------------------+
    |           BACKEND TELEPHONY & AI ENGINE (FastAPI / Sarvam AI / Carrier Trunks)        |
    +---------------------------------------------------------------------------------------+
    """
    code_box_style = styles['CodeListing']
    story.append(Preformatted(arch_diagram, code_box_style))
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 2: DIRECTORY & CODEBASE ORGANIZATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("2. FRONTEND DIRECTORY STRUCTURE & CODEBASE ORGANIZATION", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    dir_summary = [
        [Paragraph("Directory Path", styles['TableHead']), Paragraph("Module Role", styles['TableHead']), Paragraph("Key Files / Submodules", styles['TableHead'])],
        [Paragraph("src/app/", styles['TableCellBold']), Paragraph("Application Root & Routing", styles['TableCell']), Paragraph("App.tsx, router.tsx, providers/ (Auth, Business, Theme, Query, Toast)", styles['TableCell'])],
        [Paragraph("src/components/layout/", styles['TableCellBold']), Paragraph("Layout Shells & Navigation", styles['TableCell']), Paragraph("AppShell.tsx, Sidebar.tsx, Header.tsx, LookToggle.tsx, QuickDialModal.tsx", styles['TableCell'])],
        [Paragraph("src/components/ui/", styles['TableCellBold']), Paragraph("Atomic UI Library (21 components)", styles['TableCell']), Paragraph("AudioPlayer, Badge, Button, Card, DataTable, Drawer, Modal, Tabs, Select", styles['TableCell'])],
        [Paragraph("src/components/effects/", styles['TableCellBold']), Paragraph("Modern Visual Effects", styles['TableCell']), Paragraph("AmbientBackground.tsx, GlowProvider.tsx, ParticleStars.tsx, ambient.css", styles['TableCell'])],
        [Paragraph("src/features/agents/", styles['TableCellBold']), Paragraph("AI Voice Agent Studio", styles['TableCell']), Paragraph("AgentsPage.tsx, AgentFormDrawer.tsx, AgentWorkspacePage.tsx", styles['TableCell'])],
        [Paragraph("src/features/calls/", styles['TableCellBold']), Paragraph("Telephony Call Monitoring", styles['TableCell']), Paragraph("CallsPage.tsx, ActiveCallsPage.tsx, CallDetailDrawer.tsx, QueuePage.tsx", styles['TableCell'])],
        [Paragraph("src/features/leads/", styles['TableCellBold']), Paragraph("AI Lead Intelligence Pipeline", styles['TableCell']), Paragraph("LeadsPage.tsx (Gemini intent scores, customer details, why-reasons)", styles['TableCell'])],
        [Paragraph("src/features/questionnaires/", styles['TableCellBold']), Paragraph("Conversational Questionnaire Flow", styles['TableCell']), Paragraph("QuestionnairesPage.tsx, QuestionnaireEditorPage.tsx, Excel/Docx Import Modals", styles['TableCell'])],
        [Paragraph("src/features/modern/", styles['TableCellBold']), Paragraph("Modern High-Tech Design Suite", styles['TableCell']), Paragraph("ModernDashboard.tsx, ModernCalls.tsx, ModernLeads.tsx, ui.tsx (17 views)", styles['TableCell'])],
        [Paragraph("src/features/settings/", styles['TableCellBold']), Paragraph("Telephony & AI Credentials", styles['TableCell']), Paragraph("SarvamSettings.tsx, VoBizTelephonySettings.tsx, TwilioTelephonySettings.tsx", styles['TableCell'])],
        [Paragraph("src/services/api/", styles['TableCellBold']), Paragraph("REST & WebSocket Client Services", styles['TableCell']), Paragraph("client.ts (Axios), calls.ts, agents.ts, leads.ts, telephony.ts (17 services)", styles['TableCell'])],
        [Paragraph("src/types/", styles['TableCellBold']), Paragraph("Enterprise TypeScript Schemas", styles['TableCell']), Paragraph("api.ts (Exhaustive domain models, API schemas, and response interfaces)", styles['TableCell'])],
        [Paragraph("src/utils/", styles['TableCellBold']), Paragraph("Export Engines & Formatters", styles['TableCell']), Paragraph("agentPdfExport.ts, businessPdfExport.ts, excelExport.ts, quickDial.ts", styles['TableCell'])],
    ]
    t_dir = Table(dir_summary, colWidths=[120, 130, 273])
    t_dir.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_dir)
    story.append(PageBreak())
    
    # -------------------------------------------------------------------------
    # SECTION 3: ROUTING STRUCTURE & NAVIGATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("3. DECLARATIVE ROUTING STRUCTURE & DUAL LOOK ARCHITECTURE", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    routing_text = (
        "The application utilizes <code>react-router-dom</code> (v6.28.1) via <code>createBrowserRouter</code>. "
        "A hallmark architectural feature is the <b>Dual Look Engine</b>: routes are encapsulated within a "
        "<code>LookPage</code> component that dynamically renders either the classic enterprise view or the "
        "futuristic modern view depending on operator selection."
    )
    story.append(Paragraph(routing_text, styles['DocBody']))
    
    routes_table = [
        [Paragraph("URL Route Path", styles['TableHead']), Paragraph("Classic Component", styles['TableHead']), Paragraph("Modern Component", styles['TableHead']), Paragraph("Functional Scope", styles['TableHead'])],
        [Paragraph("<b>/</b>", styles['TableCellBold']), Paragraph("DashboardPage", styles['TableCell']), Paragraph("ModernDashboard", styles['TableCell']), Paragraph("Operational Telephony Cockpit & KPIs", styles['TableCell'])],
        [Paragraph("<b>/calls</b>", styles['TableCellBold']), Paragraph("CallsPage", styles['TableCell']), Paragraph("ModernCalls", styles['TableCell']), Paragraph("Historical Call Records & Audio Player", styles['TableCell'])],
        [Paragraph("<b>/active-calls</b>", styles['TableCellBold']), Paragraph("ActiveCallsPage", styles['TableCell']), Paragraph("ModernActiveCalls", styles['TableCell']), Paragraph("Real-Time Ongoing Call Waveforms", styles['TableCell'])],
        [Paragraph("<b>/agents</b>", styles['TableCellBold']), Paragraph("AgentsPage", styles['TableCell']), Paragraph("ModernAgents", styles['TableCell']), Paragraph("Conversational Voice Agent Studio", styles['TableCell'])],
        [Paragraph("<b>/agents/:id</b>", styles['TableCellBold']), Paragraph("AgentWorkspacePage", styles['TableCell']), Paragraph("AgentWorkspacePage", styles['TableCell']), Paragraph("Prompt Engineering & Tuning Workbench", styles['TableCell'])],
        [Paragraph("<b>/leads</b>", styles['TableCellBold']), Paragraph("LeadsPage", styles['TableCell']), Paragraph("ModernLeads", styles['TableCell']), Paragraph("AI Lead Intelligence & Qualification", styles['TableCell'])],
        [Paragraph("<b>/questionnaires</b>", styles['TableCellBold']), Paragraph("QuestionnairesPage", styles['TableCell']), Paragraph("ModernQuestionnaires", styles['TableCell']), Paragraph("Conversational Flow Editor & Importers", styles['TableCell'])],
        [Paragraph("<b>/businesses</b>", styles['TableCellBold']), Paragraph("BusinessesPage", styles['TableCell']), Paragraph("ModernBusinesses", styles['TableCell']), Paragraph("Multi-Tenant Enterprise Organizations", styles['TableCell'])],
        [Paragraph("<b>/followups</b>", styles['TableCellBold']), Paragraph("FollowupsPage", styles['TableCell']), Paragraph("ModernFollowups", styles['TableCell']), Paragraph("Scheduled Customer Callbacks & Tasks", styles['TableCell'])],
        [Paragraph("<b>/reports</b>", styles['TableCellBold']), Paragraph("ReportsPage", styles['TableCell']), Paragraph("ModernReports", styles['TableCell']), Paragraph("Business Intelligence & Analytics", styles['TableCell'])],
        [Paragraph("<b>/settings</b>", styles['TableCellBold']), Paragraph("SettingsPage", styles['TableCell']), Paragraph("ModernSettings", styles['TableCell']), Paragraph("Sarvam, VoBiz, Twilio, Gemini Config", styles['TableCell'])],
    ]
    t_routes = Table(routes_table, colWidths=[90, 110, 110, 213])
    t_routes.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_routes)
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 4: STATE MANAGEMENT & DATA FLOW
    # -------------------------------------------------------------------------
    story.append(Paragraph("4. STATE MANAGEMENT & PROVIDER CASCADE", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    state_desc = (
        "State management in the application is architected across three distinct tiers:<br/>"
        "1. <b>Server State (TanStack React Query v5):</b> Handles asynchronous API fetching, automated polling of active calls, "
        "intelligent stale-time caching, and optimistic UI mutations.<br/>"
        "2. <b>Domain & Session Context (React Context Hierarchy):</b> Defined in <code>src/app/providers/</code>:<br/>"
        "   • <code>ThemeProvider:</code> Manages dark/light appearance tokens.<br/>"
        "   • <code>QueryProvider:</code> Encapsulates the master React Query client.<br/>"
        "   • <code>AuthProvider:</code> Stores operator authentication tokens, role permissions, and login modal states.<br/>"
        "   • <code>BusinessProvider:</code> Manages multi-tenant organization switching, persisting active business ID in local storage.<br/>"
        "   • <code>ToastProvider:</code> Global notification queue for feedback alerts.<br/>"
        "3. <b>Ephemeral UI State (Zustand v5):</b> Controls lightweight, rapid-toggle interface states such as drawer expansions and tab switches."
    )
    story.append(Paragraph(state_desc, styles['DocBody']))
    story.append(Spacer(1, 8))
    
    # -------------------------------------------------------------------------
    # SECTION 5: TELEPHONY INTEGRATION & AUDIO PLAYBACK ENGINE
    # -------------------------------------------------------------------------
    story.append(Paragraph("5. TELEPHONY INTEGRATION & AUDIO PLAYBACK SUBSYSTEM", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    telephony_desc = (
        "The frontend interfaces directly with telecommunications hardware and carrier trunks via backend proxy endpoints:<br/>"
        "• <b>Real-Time Audio Player (<code>AudioPlayer.tsx</code>):</b> Built to stream lossless 8,000Hz 16-bit PCM WAV audio "
        "recorded directly from live telephony channels. Supports play/pause, seek scrubbers, volume controls, and turn synchronization.<br/>"
        "• <b>Live Telephony Polling (<code>useActiveCalls.ts</code>):</b> Automatically polls <code>/api/calls/active</code> "
        "every 2,000 milliseconds, calculating dynamic call elapsed time and displaying animated waveform pulses.<br/>"
        "• <b>Turn-by-Turn Transcript Synchronization:</b> Diarizes conversation dialogue into structured chat bubbles distinguishing "
        "the AI Voice Agent and the Customer, accompanied by speech recognition confidence and latency markers."
    )
    story.append(Paragraph(telephony_desc, styles['DocBody']))
    story.append(PageBreak())
    
    # -------------------------------------------------------------------------
    # SECTION 6: BUILD, OPTIMIZATION & CONTAINERIZED DEPLOYMENT
    # -------------------------------------------------------------------------
    story.append(Paragraph("6. BUILD, OPTIMIZATION & DEPLOYMENT INFRASTRUCTURE", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    deploy_desc = (
        "The project is engineered for production-ready, zero-downtime enterprise deployment. "
        "The compilation and delivery pipeline consists of three core components:"
    )
    story.append(Paragraph(deploy_desc, styles['DocBody']))
    
    pipeline_steps = [
        "<b>TypeScript Build Verification (<code>npm run build</code>):</b> Runs <code>tsc -b</code> (strict TypeScript compiler verification) followed by <code>vite build</code>. Rollup bundles and tree-shakes all modular source files into optimized distribution chunks in <code>dist/assets/</code>.",
        "<b>Multi-Stage Docker Containerization (<code>Dockerfile</code>):</b><br/>"
        "  • <i>Stage 1 (Builder):</i> Node.js 20 Alpine environment installs dependencies and compiles static bundles.<br/>"
        "  • <i>Stage 2 (Production Runner):</i> High-performance Nginx Alpine image receives only the compiled <code>dist/</code> artifacts, reducing final container footprint to under 25 megabytes.",
        "<b>Production Nginx Reverse Proxy (<code>nginx.conf</code>):</b> Directs static asset requests with long-term cache headers while proxying <code>/api/*</code> and telephony WebSocket streams to the backend engine on port 8001. Implements Single Page Application fallback routing (<code>try_files $uri $uri/ /index.html</code>)."
    ]
    for s in pipeline_steps:
        story.append(Paragraph(f"• {s}", styles['DocBullet']))
    story.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 7: SECURITY, CREDENTIALS & SENSITIVE DATA EXCLUSION
    # -------------------------------------------------------------------------
    story.append(Paragraph("7. SECURITY CONTROLS & EXCLUSION OF SENSITIVE CREDENTIALS", styles['DocH1']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=8))
    
    security_text = (
        "In accordance with software security best practices and statutory filing standards:<br/>"
        "1. <b>Zero Hardcoded Secrets:</b> All carrier credentials (VoBiz Auth IDs, Twilio Account SIDs, Sarvam AI API keys, "
        "and Google Gemini API keys) are configured dynamically through UI input forms and transmitted securely to "
        "the backend via HTTP POST/PUT requests.<br/>"
        "2. <b>Exclusion from Copyright Deposit:</b> Environment configuration files (<code>.env</code>, <code>.env.local</code>), "
        "private authentication tokens, and server passwords have been strictly excluded from this documentation package "
        "to prevent any compromise of operational credentials."
    )
    story.append(Paragraph(security_text, styles['DocBody']))
    story.append(Spacer(1, 18))
    
    # Verification block
    sig_block = [
        [Paragraph("<b>Technical Architect / Engineer:</b>", styles['TableCellBold']), Paragraph("<b>Verified for Copyright Submission:</b>", styles['TableCellBold'])],
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
    
    class TechNumberedCanvas(NumberedCanvas):
        doc_header_title = "DOCUMENT 04: SOFTWARE TECHNICAL DOCUMENTATION"
        
    doc.build(story, canvasmaker=TechNumberedCanvas)
    print(f"Generated 04_Technical_Documentation.pdf successfully at {OUTPUT_PDF}")

if __name__ == '__main__':
    generate_pdf()

