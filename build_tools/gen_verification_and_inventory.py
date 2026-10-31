import os
import hashlib
import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FRONTEND_DIR = os.path.join(ROOT_DIR, 'frontend_1')
SRC_DIR = os.path.join(FRONTEND_DIR, 'src')
DIST_DIR = os.path.join(FRONTEND_DIR, 'dist')
DOCS_DIR = os.path.join(ROOT_DIR, 'COPYRIGHT_DOCUMENTATION')
VERIF_DIR = os.path.join(DOCS_DIR, 'verification')

os.makedirs(VERIF_DIR, exist_ok=True)

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def classify_module(rel_path):
    parts = rel_path.replace('\\', '/').split('/')
    if len(parts) >= 3 and parts[1] == 'features':
        return f"features/{parts[2]}"
    elif len(parts) >= 3 and parts[1] == 'components':
        return f"components/{parts[2]}"
    elif len(parts) >= 3 and parts[1] == 'app':
        return f"app/{parts[2]}"
    elif len(parts) >= 3 and parts[1] == 'services':
        return f"services/{parts[2]}"
    elif len(parts) >= 2:
        return parts[1]
    return "root"

def classify_authorship(rel_path):
    p = rel_path.replace('\\', '/')
    if p.startswith('src/features/'):
        return "Original Frontend Feature Logic"
    elif p.startswith('src/components/ui/'):
        return "Custom UI Component System"
    elif p.startswith('src/components/layout/'):
        return "Application Layout & Navigation"
    elif p.startswith('src/components/effects/'):
        return "Custom Visual & Ambient Effects"
    elif p.startswith('src/services/api/'):
        return "REST/WebSocket API Telemetry Services"
    elif p.startswith('src/app/providers/'):
        return "State & Context Provider Infrastructure"
    elif p.startswith('src/utils/'):
        return "Domain Utility & Export Engines"
    elif p.startswith('src/types/'):
        return "Data Contracts & Type Schemas"
    elif p.startswith('src/hooks/'):
        return "Custom React Hooks"
    elif p.startswith('src/styles/'):
        return "Custom CSS & Theme Stylesheets"
    else:
        return "Application Configuration & Entry Point"

def get_functional_description(rel_path):
    descriptions = {
        'src/main.tsx': 'Application bootstrap, DOM mounting, and stale service-worker/cache clearance.',
        'src/vite-env.d.ts': 'TypeScript environment type definitions for Vite client runtime.',
        'src/app/App.tsx': 'Master application root with hierarchical context providers (Theme, Query, Auth, Business, Toast).',
        'src/app/router.tsx': 'Central declarative router configuration with Dual-Look (Classic vs Modern) page mapping.',
        'src/app/providers/AuthProvider.tsx': 'Authentication state management, JWT session persistence, and login modals.',
        'src/app/providers/BusinessProvider.tsx': 'Multi-tenant organization context, active business switcher, and metadata persistence.',
        'src/app/providers/QueryProvider.tsx': 'TanStack React Query client initialization and cache management configuration.',
        'src/app/providers/ThemeProvider.tsx': 'Dynamic dark/light mode toggle with HTML root class management.',
        'src/app/providers/ToastProvider.tsx': 'Interactive user notification alert system with queue management.',
        'src/components/effects/ambient.css': 'Custom CSS keyframes and utility styling for radiant background lighting.',
        'src/components/effects/AmbientBackground.tsx': 'Animated ambient gradient backdrop component for modern enterprise look.',
        'src/components/effects/glow.css': 'Glowing border, glassmorphism, and neon pulse CSS animations.',
        'src/components/effects/GlowProvider.tsx': 'Interactive cursor-following glow coordinate provider.',
        'src/components/effects/ParticleStars.tsx': 'Interactive HTML5 Canvas particle starfield simulation.',
        'src/components/layout/AppShell.tsx': 'Primary classic application shell with responsive sidebar, header, and content viewport.',
        'src/components/layout/AuthModal.tsx': 'Modal dialog for enterprise operator sign-in and session authentication.',
        'src/components/layout/Header.tsx': 'Top application navigation bar with business switcher, look toggle, and status alerts.',
        'src/components/layout/LookToggle.tsx': 'Interactive switch toggling between Classic Enterprise and Modern visual designs.',
        'src/components/layout/PageHeader.tsx': 'Standardized header banner for feature views with action button slots.',
        'src/components/layout/QuickDialModal.tsx': 'Global modal allowing direct manual dialing of PSTN phone numbers via carrier trunks.',
        'src/components/layout/Sidebar.tsx': 'Collapsible navigation sidebar with route indicators and badge counters.',
        'src/components/ui/AudioPlayer.tsx': 'Custom audio player component for streaming authentic 8kHz PCM WAV call recordings.',
        'src/components/ui/Badge.tsx': 'Reusable status pill component with variant colors and glowing borders.',
        'src/components/ui/BrandMark.tsx': 'Vector branding mark component representing the platform identity.',
        'src/components/ui/BusinessSelector.tsx': 'Dropdown selector for active multi-tenant enterprise business switching.',
        'src/components/ui/Button.tsx': 'Standardized interactive button with loading states, sizes, and variants.',
        'src/components/ui/Card.tsx': 'Container card with glassmorphism, elevated shadows, and border highlights.',
        'src/components/ui/ConfirmDialog.tsx': 'Modal confirmation dialog for destructive actions.',
        'src/components/ui/DataTable.tsx': 'Generic data table with search, client-side pagination, sorting, and row selection.',
        'src/components/ui/Drawer.tsx': 'Slide-out lateral sheet component for detail views and side panels.',
        'src/components/ui/EmptyState.tsx': 'Placeholder visual displayed when tables or collections have zero data.',
        'src/components/ui/ErrorAlert.tsx': 'Visual alert banner displaying technical error messages and recovery prompts.',
        'src/components/ui/Input.tsx': 'Form input field with label, validation error feedback, and adornments.',
        'src/components/ui/MetricCard.tsx': 'Dashboard KPI metric card with percentage delta indicator and trend iconography.',
        'src/components/ui/Modal.tsx': 'Accessible modal backdrop and container with ESC key listener.',
        'src/components/ui/ModelModeSwitcher.tsx': 'Selector for switching AI model inference modes (Fast vs Quality).',
        'src/components/ui/Select.tsx': 'Custom styled dropdown selection input with options rendering.',
        'src/components/ui/Skeleton.tsx': 'Animated skeleton loader placeholder for asynchronous data loading states.',
        'src/components/ui/StatusIndicator.tsx': 'Glowing status dot indicator for live telephony channel connection states.',
        'src/components/ui/Switch.tsx': 'Accessible toggle switch component for binary settings.',
        'src/components/ui/Tabs.tsx': 'Tabbed navigation container with active indicator pill.',
        'src/components/ui/TimeFilterAndExport.tsx': 'Time-range filter selector (Day/Week/Month) with Excel export triggers.',
        'src/features/agents/AgentFormDrawer.tsx': 'Comprehensive drawer for creating/editing AI voice agents, prompts, and voices.',
        'src/features/agents/AgentsPage.tsx': 'Catalog page listing configured conversational AI telephony agents.',
        'src/features/agents/AgentWorkspacePage.tsx': 'Dedicated studio workspace for tuning agent prompts, testing audio, and PDF dossier export.',
        'src/features/businesses/BusinessDetailPage.tsx': 'Detailed profile view for an enterprise tenant business.',
        'src/features/businesses/BusinessesPage.tsx': 'Administration page listing all tenant businesses and telephony trunks.',
        'src/features/businesses/BusinessFormModal.tsx': 'Modal dialog for creating and updating tenant business profiles.',
        'src/features/calls/ActiveCallsPage.tsx': 'Real-time telemetry monitor showing active ongoing phone conversations.',
        'src/features/calls/CallDetailDrawer.tsx': 'Lateral drawer displaying turn-by-turn transcripts, sentiment, audio player, and AI reasoning.',
        'src/features/calls/CallsPage.tsx': 'Historical call detail records (CDR) table with search, filtering, and audio triggers.',
        'src/features/calls/QueuePage.tsx': 'Outbound dialer queue status and pending call dispatch monitor.',
        'src/features/campaigns/CampaignsPage.tsx': 'Telephony outbound broadcast campaign management dashboard.',
        'src/features/campaigns/CampaignWizardModal.tsx': 'Multi-step wizard for configuring and launching automated voice campaigns.',
        'src/features/contacts/ContactsPage.tsx': 'CRM contact directory with call turn counts, lead scores, and DNC flags.',
        'src/features/contacts/CsvImportModal.tsx': 'Client-side CSV bulk contact uploader with column mapping.',
        'src/features/dashboard/AgentSelectPopover.tsx': 'Quick-selection popover for switching active voice agents.',
        'src/features/dashboard/DashboardPage.tsx': 'Master enterprise dashboard featuring real-time call telemetry and KPI charts.',
        'src/features/followups/FollowupsPage.tsx': 'Scheduled callback and lead follow-up task management interface.',
        'src/features/health/HealthPage.tsx': 'System infrastructure diagnostic page monitoring DB, Redis, MinIO, and GPU status.',
        'src/features/invoices/InvoicesPage.tsx': 'Telephony billing, minute consumption tracker, and PDF invoice generator.',
        'src/features/leads/LeadsPage.tsx': 'AI lead qualification pipeline with extracted customer data, budget, and why-interested reasoning chips.',
        'src/features/models/ModelConfigPage.tsx': 'AI model provider credentials configuration and schema validation.',
        'src/features/model_lab/ModelLabPage.tsx': 'Voice latency testing workbench, STT/TTS benchmarks, and live audio diagnostics.',
        'src/features/modern/LookPage.tsx': 'View wrapper dynamically rendering Classic or Modern design based on user preference.',
        'src/features/modern/ModernActiveCalls.tsx': 'Futuristic glassmorphic active calls monitor with animated sound waves.',
        'src/features/modern/ModernAgents.tsx': 'Modern grid layout for voice agent selection and deployment.',
        'src/features/modern/ModernBusinesses.tsx': 'Modern tenant business cards with usage metrics and neon accents.',
        'src/features/modern/ModernCalendar.tsx': 'Interactive calendar view for scheduled callbacks and call appointments.',
        'src/features/modern/ModernCalls.tsx': 'Modernized call records view with inline player and status badges.',
        'src/features/modern/ModernCampaigns.tsx': 'Modern outbound campaign progress monitor with circular gauges.',
        'src/features/modern/ModernContacts.tsx': 'Modern contact book with lead score tags and quick-dial buttons.',
        'src/features/modern/ModernDashboard.tsx': 'High-tech dark telemetry cockpit with glowing SVG metric graphs.',
        'src/features/modern/ModernFollowups.tsx': 'Modern kanban/card view for scheduled lead callbacks.',
        'src/features/modern/ModernInvoices.tsx': 'Modern billing overview with expenditure graphs and invoice cards.',
        'src/features/modern/ModernLeads.tsx': 'Modernized sales lead pipeline with AI qualification tags and sentiment radar.',
        'src/features/modern/ModernQuestionnaires.tsx': 'Modern questionnaire card view with response statistics.',
        'src/features/modern/ModernReports.tsx': 'Modern graphical analytics report generator with export controls.',
        'src/features/modern/ModernSettings.tsx': 'Modern tabbed settings panel for telephony and AI credentials.',
        'src/features/modern/ModernShell.tsx': 'Futuristic navigation shell with glowing borders and ambient lighting.',
        'src/features/modern/ui.tsx': 'Modern UI design system building blocks (GlowCard, ModernBadge, NeonButton).',
        'src/features/questionnaires/DocxImportModal.tsx': 'Document importer parsing questionnaire questions from Word (.docx) files.',
        'src/features/questionnaires/ExcelImportModal.tsx': 'Spreadsheet importer parsing questionnaire trees from Excel (.xlsx) files.',
        'src/features/questionnaires/QuestionnaireEditorPage.tsx': 'Interactive visual question branching and dynamic flow editor.',
        'src/features/questionnaires/QuestionnairesPage.tsx': 'Directory of structured question flows for telephony agents.',
        'src/features/reports/ReportsPage.tsx': 'Business analytics and call performance reporting dashboard.',
        'src/features/settings/SarvamSettings.tsx': 'Sarvam AI telephony configuration panel for API keys and voice models.',
        'src/features/settings/SettingsPage.tsx': 'Master configuration hub with tabs for Telephony, Transcripts, and Workspaces.',
        'src/features/settings/TranscriptApiSettings.tsx': 'Google Gemini API key and prompt parameters setup for lead intelligence.',
        'src/features/settings/TwilioTelephonySettings.tsx': 'Twilio SIP trunk, Account SID, and Auth Token configuration interface.',
        'src/features/settings/VoBizTelephonySettings.tsx': 'VoBiz PSTN trunk credentials and caller ID phone number management.',
        'src/hooks/useActiveCalls.ts': 'Custom React hook for polling ongoing calls with auto-refresh intervals.',
        'src/hooks/useRealTimeStats.ts': 'Custom React hook subscribing to aggregate telephony telemetry data.',
        'src/services/api/agents.ts': 'API service module for creating, updating, and fetching voice agents.',
        'src/services/api/businesses.ts': 'API service module for tenant business CRUD operations and trunk binding.',
        'src/services/api/calendar.ts': 'API service module for fetching scheduled call appointments.',
        'src/services/api/calls.ts': 'API service module for CDR retrieval, live interest analysis, and audio streaming.',
        'src/services/api/campaigns.ts': 'API service module for outbound voice campaign execution.',
        'src/services/api/client.ts': 'Axios HTTP client instance with baseURL resolution and error interceptors.',
        'src/services/api/contacts.ts': 'API service module for contact directory and DNC updates.',
        'src/services/api/followups.ts': 'API service module for callback scheduling and task resolution.',
        'src/services/api/health.ts': 'API service module for system infrastructure health checks.',
        'src/services/api/leads.ts': 'API service module for AI qualified lead retrieval and status editing.',
        'src/services/api/modelConfig.ts': 'API service module for AI provider model configurations.',
        'src/services/api/modelLab.ts': 'API service module for latency benchmarking and audio diagnostic tests.',
        'src/services/api/questionnaires.ts': 'API service module for conversational questionnaire trees.',
        'src/services/api/reports.ts': 'API service module for aggregate call reports and CSV export.',
        'src/services/api/stats.ts': 'API service module for dashboard telemetry metrics.',
        'src/services/api/telephony.ts': 'API service module for carrier trunk diagnostic status and health checks.',
        'src/services/api/voice.ts': 'API service module for voice synthesis parameters and testing.',
        'src/styles/index.css': 'Global application styles, Tailwind directives, and CSS reset.',
        'src/styles/modern.css': 'Styling specifications for the Modern futuristic theme layout.',
        'src/styles/themes.css': 'CSS custom properties / design tokens for dark and light palettes.',
        'src/types/api.ts': 'Comprehensive TypeScript data models, schemas, and API response contracts.',
        'src/utils/agentPdfExport.ts': 'Client-side PDF generator synthesizing complete agent configuration dossiers.',
        'src/utils/businessPdfExport.ts': 'Client-side PDF generator exporting enterprise business profile reports.',
        'src/utils/excelExport.ts': 'Client-side spreadsheet generation utility for leads, calls, and follow-ups.',
        'src/utils/quickDial.ts': 'Telephone number normalizer and quick-dial helper utility.',
        'index.html': 'Single Page Application HTML5 entry document loading web fonts and root div.',
        'vite.config.ts': 'Vite build tool configuration, reverse proxies for backend APIs, and path aliases.',
        'tailwind.config.js': 'Tailwind CSS design tokens, custom colors, animations, and typography rules.',
        'postcss.config.js': 'PostCSS configuration enabling Tailwind and Autoprefixer transformations.',
        'tsconfig.json': 'TypeScript compiler options, module resolution, and strict type-checking flags.',
        'tsconfig.node.json': 'TypeScript compilation rules for Vite configuration script.',
        'package.json': 'Project npm manifest defining dependencies, versions, and build scripts.',
        'nginx.conf': 'Production Nginx reverse proxy routing web requests and SPA fallback.',
        'Dockerfile': 'Multi-stage container build recipe compiling frontend and serving via Nginx.',
        'port_forwarder.cjs': 'Development utility proxying local ports for telephony testing.'
    }
    return descriptions.get(rel_path, f"Frontend source code component implementing {os.path.basename(rel_path)}.")

# Collect files
all_files = []
for root, dirs, files in os.walk(SRC_DIR):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, FRONTEND_DIR).replace('\\', '/')
        size = os.path.getsize(full_path)
        sha = sha256_file(full_path)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
            line_count = len(fp.readlines())
        ext = os.path.splitext(f)[1].lower()
        all_files.append({
            'rel_path': rel_path,
            'filename': f,
            'size': size,
            'lines': line_count,
            'sha256': sha,
            'ext': ext,
            'module': classify_module(rel_path),
            'authorship': classify_authorship(rel_path),
            'description': get_functional_description(rel_path)
        })

# Root config files
root_configs = ['index.html', 'vite.config.ts', 'tailwind.config.js', 'postcss.config.js', 'tsconfig.json', 'tsconfig.node.json', 'package.json', 'nginx.conf', 'Dockerfile', 'port_forwarder.cjs']
for f in root_configs:
    full_path = os.path.join(FRONTEND_DIR, f)
    if os.path.exists(full_path):
        size = os.path.getsize(full_path)
        sha = sha256_file(full_path)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
            line_count = len(fp.readlines())
        ext = os.path.splitext(f)[1].lower()
        all_files.append({
            'rel_path': f,
            'filename': f,
            'size': size,
            'lines': line_count,
            'sha256': sha,
            'ext': ext,
            'module': 'config',
            'authorship': 'Application Configuration & Build Pipeline',
            'description': get_functional_description(f)
        })

# Sort files alphabetically
all_files.sort(key=lambda x: x['rel_path'])

# Determine First 10 and Last 10 Pages mapping
# As planned, First 10 Pages in PDF 02 cover the initial bootstrap and core application sequence
# Last 10 Pages cover utils and domain types
first_10_paths = [
    'src/main.tsx',
    'src/app/App.tsx',
    'src/app/router.tsx',
    'src/app/providers/AuthProvider.tsx',
    'src/app/providers/BusinessProvider.tsx',
    'src/app/providers/ToastProvider.tsx',
    'src/app/providers/ThemeProvider.tsx',
    'src/components/layout/AppShell.tsx'
]
last_10_paths = [
    'src/utils/agentPdfExport.ts',
    'src/utils/businessPdfExport.ts',
    'src/utils/excelExport.ts',
    'src/utils/quickDial.ts',
    'src/types/api.ts'
]

for item in all_files:
    if item['rel_path'] in first_10_paths:
        item['submission_status'] = 'Included in PDF (First 10 Pages Deposit)'
    elif item['rel_path'] in last_10_paths:
        item['submission_status'] = 'Included in PDF (Last 10 Pages Deposit)'
    else:
        item['submission_status'] = 'Full Codebase Inventory (Rule 70(5) Voluminous Software)'

# Generate Excel Workbook
wb = openpyxl.Workbook()

# Sheet 1: Source_Code_Inventory
ws1 = wb.active
ws1.title = "Source_Code_Inventory"

header_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
border_thin = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)

headers1 = [
    "Sl No", "Relative Path", "File Name", "Subsystem / Module", 
    "Language / Ext", "Line Count", "Size (Bytes)", "Size (KB)", 
    "SHA-256 Checksum", "Authorship Category", "Statutory Submission Status", "Functional Description"
]

ws1.append(headers1)
for col_num, h in enumerate(headers1, 1):
    cell = ws1.cell(row=1, column=col_num)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

row_fill_alt = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
for idx, f in enumerate(all_files, 1):
    row_data = [
        idx,
        f['rel_path'],
        f['filename'],
        f['module'],
        f['ext'].upper().replace('.', ''),
        f['lines'],
        f['size'],
        round(f['size'] / 1024, 2),
        f['sha256'],
        f['authorship'],
        f['submission_status'],
        f['description']
    ]
    ws1.append(row_data)
    curr_row = idx + 1
    for c_idx in range(1, len(row_data) + 1):
        cell = ws1.cell(row=curr_row, column=c_idx)
        cell.border = border_thin
        cell.font = Font(name="Calibri", size=10)
        if idx % 2 == 0:
            cell.fill = row_fill_alt
        if c_idx in [1, 5, 6, 7, 8]:
            cell.alignment = Alignment(horizontal="center" if c_idx in [1, 5] else "right", vertical="center")
        elif c_idx in [9]:
            cell.font = Font(name="Consolas", size=8)
            cell.alignment = Alignment(horizontal="center", vertical="center")

# Sheet 2: Subsystem_Summary
ws2 = wb.create_sheet(title="Subsystem_Summary")
headers2 = ["Sl No", "Subsystem / Module", "Total Files", "Total Lines", "Total Size (KB)", "% of Total Lines", "Architectural Role & Description"]
ws2.append(headers2)
for col_num, h in enumerate(headers2, 1):
    cell = ws2.cell(row=1, column=col_num)
    cell.fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

modules_dict = {}
for f in all_files:
    m = f['module']
    if m not in modules_dict:
        modules_dict[m] = {'files': 0, 'lines': 0, 'size': 0}
    modules_dict[m]['files'] += 1
    modules_dict[m]['lines'] += f['lines']
    modules_dict[m]['size'] += f['size']

total_lines_all = sum(x['lines'] for x in all_files)
sorted_mods = sorted(modules_dict.items(), key=lambda x: x[0])

module_roles = {
    'app/App.tsx': 'Root component tree and context provider cascade',
    'app/providers': 'Global state providers (Auth, Business, Theme, Query, Toast)',
    'app/router.tsx': 'Central routing engine supporting classic vs modern dual-look navigation',
    'components/effects': 'Glassmorphic ambient background and particle animations',
    'components/layout': 'Master application shells, responsive sidebar, headers, and quick-dial modal',
    'components/ui': 'Standardized reusable UI component library (21 modular components)',
    'config': 'Vite, TypeScript, Tailwind, Docker, and Nginx deployment configurations',
    'features/agents': 'AI Voice Agent workspace, prompt builder, and PDF dossier exporter',
    'features/businesses': 'Multi-tenant organization management and business detail views',
    'features/calls': 'Live call telemetry, historical CDR table, and call detail transcript drawer',
    'features/campaigns': 'Outbound telephony campaign wizard and status tracking',
    'features/contacts': 'Contact directory, DNC list flag management, and CSV uploader',
    'features/dashboard': 'Real-time telemetry dashboard with KPI cards and Recharts analytics',
    'features/followups': 'Scheduled callback calendar and task tracking interface',
    'features/health': 'System telemetry monitoring DB, Redis, MinIO, and GPU servers',
    'features/invoices': 'Telephony billing records, minute consumption, and invoice generation',
    'features/leads': 'Gemini AI lead qualification pipeline with extracted customer fields & reasoning',
    'features/model_lab': 'Voice latency testing workbench, STT/TTS benchmarks, and diagnostics',
    'features/models': 'AI model provider credentials configuration and schema validation',
    'features/modern': 'Modern futuristic UI layout system (17 dedicated modern views)',
    'features/questionnaires': 'Interactive branching question flow editor with Excel/Word import',
    'features/reports': 'Business intelligence reports and call duration analytics',
    'features/settings': 'Carrier credentials setup (Sarvam AI, VoBiz, Twilio, Gemini API)',
    'hooks': 'Custom React hooks for active call polling and telemetry stats',
    'root': 'Frontend entry scripts and ambient environment definitions',
    'services/api': 'Axios REST and WebSocket API client communication layer (17 services)',
    'styles': 'Global CSS, themes design tokens, and modern style declarations',
    'types': 'TypeScript enterprise data models and schema definitions (api.ts)',
    'utils': 'Client-side PDF and Excel generation utilities and quick-dial helpers'
}

for idx, (m_name, m_data) in enumerate(sorted_mods, 1):
    pct = round((m_data['lines'] / total_lines_all) * 100, 2)
    role_desc = module_roles.get(m_name, "Frontend application sub-system module.")
    row_data = [idx, m_name, m_data['files'], m_data['lines'], round(m_data['size'] / 1024, 2), f"{pct}%", role_desc]
    ws2.append(row_data)
    curr_row = idx + 1
    for c_idx in range(1, len(row_data) + 1):
        cell = ws2.cell(row=curr_row, column=c_idx)
        cell.border = border_thin
        cell.font = Font(name="Calibri", size=10)
        if idx % 2 == 0:
            cell.fill = row_fill_alt
        if c_idx in [1, 3, 4, 5, 6]:
            cell.alignment = Alignment(horizontal="center" if c_idx in [1, 6] else "right", vertical="center")

# Sheet 3: Excluded_Artifacts
ws3 = wb.create_sheet(title="Excluded_Artifacts")
headers3 = ["Sl No", "Directory / Pattern", "Category", "Reason for Exclusion", "Statutory Rule / Authority"]
ws3.append(headers3)
for col_num, h in enumerate(headers3, 1):
    cell = ws3.cell(row=1, column=col_num)
    cell.fill = PatternFill(start_color="334155", end_color="334155", fill_type="solid")
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

excluded_list = [
    ("node_modules/", "Third-Party Runtime Dependencies", "Contains external open-source packages managed by npm. Expressly excluded from proprietary copyright claim.", "Section 52, Indian Copyright Act, 1957"),
    ("dist/ (Full Bundle)", "Production Distribution Build", "Contains 2.05 MB minified production bundle. Representative First 10 and Last 10 Pages deposited in Document 03; balance omitted.", "Rule 70(5), Copyright Rules, 2013"),
    (".env & .env.local", "Environment & Secrets", "Contains sensitive API keys, telephony carrier tokens, and credentials. Redacted for security.", "Standard Security Best Practice"),
    (".git/ & .gitignore", "Version Control Metadata", "Internal Git versioning tracking data. Non-expressive repository administrative files.", "Administrative Exclusion"),
    ("tsconfig.tsbuildinfo", "Compiler Cache", "Transient build cache generated during TypeScript compilation.", "Administrative Exclusion"),
    ("dist/assets/*.map", "Source Map Files (if generated)", "Internal debugging source map lookup files.", "Administrative Exclusion")
]

for idx, item in enumerate(excluded_list, 1):
    row_data = [idx, item[0], item[1], item[2], item[3]]
    ws3.append(row_data)
    curr_row = idx + 1
    for c_idx in range(1, len(row_data) + 1):
        cell = ws3.cell(row=curr_row, column=c_idx)
        cell.border = border_thin
        cell.font = Font(name="Calibri", size=10)
        if idx % 2 == 0:
            cell.fill = row_fill_alt
        if c_idx == 1:
            cell.alignment = Alignment(horizontal="center", vertical="center")

# Adjust column widths
for ws in [ws1, ws2, ws3]:
    ws.freeze_panes = "A2"
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(min(max_len + 3, 60), 10)

# Save verification text files
with open(os.path.join(VERIF_DIR, "project_analysis.txt"), "w", encoding="utf-8") as f:
    f.write(f"""================================================================================
GOVERNMENT OF INDIA • COPYRIGHT REGISTRATION DOCUMENTATION PACKAGE
COMPREHENSIVE FRONTEND PROJECT TECHNICAL ANALYSIS & AUDIT REPORT
STATUTORY BASIS: INDIAN COPYRIGHT ACT, 1957 & COPYRIGHT RULES, 2013 (AS AMENDED)
================================================================================

1. EXECUTIVE SUMMARY & SOFTWARE IDENTIFICATION
--------------------------------------------------------------------------------
Software Title                 : ARB SoftTech AI Enterprise Voice Calling Agent Platform — Frontend Software
Application Package Name       : voxora-enterprise-ai-voice
Platform Version               : 2.0.0 Production
Statutory Classification       : Computer Software / Literary Work (Section 2(o), Indian Copyright Act, 1957)
Statutory Definition           : Set of instructions expressed in words, codes, schemes (Section 2(ffc))
Target Registration Authority  : Copyright Office, DPIIT, Ministry of Commerce and Industry, New Delhi
Registration Form              : Form XIV (Application for Registration of Copyright)
Deposit Mandate                : Rule 70(5), Copyright Rules, 2013 (Source Code & Object Code Deposit)
Primary Application Language   : TypeScript (v5.6.3), JavaScript (ES2022 / ECMAScript Modules), HTML5, CSS3
Runtime Framework              : React 18.3.1 / Vite 6.0.5 Single Page Application (SPA)
Hosting & Delivery             : Nginx Reverse Proxy / Docker Container / Static Web Distribution

2. CODEBASE SIZE & STRUCTURAL METRICS
--------------------------------------------------------------------------------
Total Source Files (src/)      : {len([x for x in all_files if x['rel_path'].startswith('src/')])} files
Total Source Code Lines (src/) : {sum(x['lines'] for x in all_files if x['rel_path'].startswith('src/')):,} lines
Total Source Code Size (src/)  : {sum(x['size'] for x in all_files if x['rel_path'].startswith('src/')):,} bytes ({sum(x['size'] for x in all_files if x['rel_path'].startswith('src/'))/1024:.2f} KB)
Root Configuration Files       : {len([x for x in all_files if not x['rel_path'].startswith('src/')])} files ({sum(x['lines'] for x in all_files if not x['rel_path'].startswith('src/')):,} lines, {sum(x['size'] for x in all_files if not x['rel_path'].startswith('src/')):,} bytes)
Total Frontend Codebase        : {len(all_files)} files ({sum(x['lines'] for x in all_files):,} lines, {sum(x['size'] for x in all_files)/1024:.2f} KB)

File Breakdown by Extension:
  - TypeScript React (.tsx)    : {len([x for x in all_files if x['ext'] == '.tsx'])} files ({sum(x['lines'] for x in all_files if x['ext'] == '.tsx'):,} lines, {sum(x['size'] for x in all_files if x['ext'] == '.tsx')/1024:.2f} KB)
  - TypeScript (.ts)           : {len([x for x in all_files if x['ext'] == '.ts'])} files ({sum(x['lines'] for x in all_files if x['ext'] == '.ts'):,} lines, {sum(x['size'] for x in all_files if x['ext'] == '.ts')/1024:.2f} KB)
  - Cascading Style (.css)     : {len([x for x in all_files if x['ext'] == '.css'])} files ({sum(x['lines'] for x in all_files if x['ext'] == '.css'):,} lines, {sum(x['size'] for x in all_files if x['ext'] == '.css')/1024:.2f} KB)
  - Project Configs & HTML     : {len([x for x in all_files if x['ext'] in ['.html', '.json', '.cjs', '.conf', '']])} files

3. OBJECT CODE & PRODUCTION COMPILED ASSET AUDIT (dist/)
--------------------------------------------------------------------------------
Production Build Tool          : Vite 6.0.5 + TypeScript Compiler (tsc -b && vite build)
Target JavaScript Standard     : ECMAScript 2020 / Modern Web Standard
Minification / Tree-Shaking   : Rollup / Terser Minification Enabled

Production Assets:
  - dist/assets/index-CF2ycynq.js        : 2,047,019 bytes (1,999.04 KB) [Main Production Application Bundle]
  - dist/assets/index-Cly00IWU.css        :   114,670 bytes (  111.98 KB) [Production Compiled Design System]
  - dist/assets/html2canvas.esm-QH1iLAAe.js : 202,379 bytes (  197.64 KB) [PDF Rasterizer Distribution Chunk]
  - dist/assets/index.es-D388Y0sF.js      :   159,715 bytes (  155.97 KB) [Recharts/Vector Charting Chunk]
  - dist/assets/purify.es-DBIK8olT.js     :    29,400 bytes (   28.71 KB) [DOMPurify Security Sanitizer Chunk]
  - dist/index.html                       :     1,987 bytes (    1.94 KB) [Production Single Page Entry Point]
  - dist/favicon.svg                      :       674 bytes (    0.66 KB) [Vector Icon Asset]

4. ARCHITECTURAL & FUNCTIONAL CAPABILITIES AUDIT
--------------------------------------------------------------------------------
1. Dual-Layout & Modern Theme Engine:
   - Classic Enterprise layout vs Modern futuristic UI toggle (LookToggle, LookPage, ModernShell).
   - Dynamic ambient lighting, particle star simulation, and glassmorphic telemetry cards.
2. Real-Time Telephony Dashboard:
   - Live KPI metric cards (Total Calls, Active Calls, Minutes Consumed, Conversion Rate).
   - Active Call Monitor displaying live channel states, agent-to-caller stream, audio waveforms.
   - Interactive Audio Player supporting authentic 8kHz PCM WAV telephony stream playback.
3. AI Voice Agent Studio & Prompt Engineering:
   - Visual agent configuration drawer with multilingual TTS voice selection (Sarvam AI: Shubh, Ritu, etc.).
   - Temperature, interruptibility delay, max conversation turns, and barge-in slider controls.
   - Direct export of comprehensive Agent Dossiers to PDF (jsPDF + autotable).
4. Lead Intelligence & Qualification Pipeline:
   - Leads dashboard reflecting turn-by-turn post-call transcript analysis powered by Google Gemini.
   - Extracted customer intelligence display: Caller Name, Phone, City, Budget, Preferred Callback Time.
   - Hoverable reasoning chips displaying exact conversational evidence and intent score.
   - Dual export capability: Client-side dynamic Excel (.xlsx) and server-side generated Excel export.
5. Conversational Questionnaire Engine:
   - Step-by-step interactive questionnaire branching editor with dynamic node routing.
   - Bulk import interfaces supporting Microsoft Excel (.xlsx) and Word (.docx) schemas.
6. Multi-Tenant Business Administration:
   - Switchable workspace context via BusinessSelector and BusinessProvider.
   - Telephony trunk bindings, business profile editing, and business dossier PDF generation.
7. Outbound PSTN Quick-Dial Dispatcher:
   - Global QuickDialModal allowing instantaneous dialing to regular mobile/PSTN numbers.
8. Telephony Carrier & AI Credentials Configuration:
   - Real-time settings console for Sarvam AI, VoBiz Carrier Trunks, Twilio Trunks, and Gemini APIs.

5. AUTHORSHIP, AI-ASSISTANCE & COPYRIGHT ELIGIBILITY ANALYSIS
--------------------------------------------------------------------------------
A. Statutory Basis under Indian Copyright Act, 1957:
   - Section 2(d)(i) requires an 'author' of a literary work to be a natural human person.
   - Section 17 governs the first owner of copyright (Work Made for Hire in employment or contract).
   - The Indian Copyright Office does not grant authorship to autonomous artificial intelligence systems.

B. Identifiable Human Contributions:
   - High-level architectural specification, domain data schemas, and state management hierarchy.
   - Custom telephony integration logic (PSTN call flows, barge-in audio playback, dual-theme engine).
   - Selection, curation, sequence, and structural arrangement of UI components and user workflows.
   - Prompt engineering designs, validation rules, business logic, and lead qualification thresholds.
   - Verification, code auditing, debugging, integration testing, and production build engineering.

C. AI-Assisted Development Disclosure (Google Antigravity):
   - The software was authored with the computational assistance of Google Antigravity, an advanced
     agentic AI coding assistant.
   - Google Antigravity was directed by human engineers via natural language instructions, architecture
     blueprints, and iterative prompts to generate code scaffolding, boilerplate components, and
     syntax adaptations.
   - The AI tool operated strictly as a sophisticated development instrument under human supervision.
   - Copyright protection is claimed exclusively over the resulting original human expression,
     creative selection, coordination, arrangement, and custom programming logic.

D. Third-Party Open Source Carve-Outs:
   - Contains 18 production dependencies and 9 development dependencies licensed under permissive
     open-source licenses (MIT, Apache 2.0, BSD-3-Clause).
   - Third-party packages (React, Vite, Recharts, Lucide, Tailwind, GSAP, jsPDF, SheetJS, PapaParse, etc.)
     are expressly disclaimed from the proprietary copyright claim, in strict compliance with
     Section 52 of the Indian Copyright Act, 1957.
================================================================================
END OF TECHNICAL ANALYSIS REPORT
================================================================================
""")

with open(os.path.join(VERIF_DIR, "missing_information.txt"), "w", encoding="utf-8") as f:
    f.write("""================================================================================
GOVERNMENT OF INDIA • COPYRIGHT REGISTRATION (FORM XIV)
MISSING APPLICANT & AUTHOR INFORMATION REQUIRING HUMAN INPUT
STATUTORY REFERENCE: COPYRIGHT RULES, 2013 • STATEMENT OF PARTICULARS (SoP)
================================================================================

The following itemized details cannot be determined from the repository files alone
and MUST be completed by the human applicant/counsel prior to final submission of
Form XIV at the Indian Copyright Office (https://copyright.gov.in).

--------------------------------------------------------------------------------
1. HUMAN AUTHOR DETAILS (MANDATORY UNDER SECTION 2(d) & 17)
--------------------------------------------------------------------------------
Under Indian Copyright Law, an Artificial Intelligence tool (such as Google Antigravity)
CANNOT be recognized or registered as an author. The author must be a natural human being.

[ ] Author 1 - Full Legal Name   : _________________________________________________
[ ] Author 1 - Residential Address: _________________________________________________
[ ] Author 1 - Nationality        : _________________________________________________
[ ] Author 1 - Country of Residence: ________________________________________________
[ ] Author 1 - PAN / Aadhaar (ID): _________________________________________________
[ ] Author 1 - Role in Creation   : [e.g. Lead Frontend Architect / Software Engineer]
[ ] If Multiple Authors, Repeat for Authors 2, 3, etc.

--------------------------------------------------------------------------------
2. APPLICANT / PROPOSED COPYRIGHT OWNER DETAILS (STATEMENT OF PARTICULARS COL 2)
--------------------------------------------------------------------------------
[ ] Name of Applicant Entity     : _________________________________________________
    (e.g., ARB SoftTech Pvt. Ltd. / Proprietorship Name / Individual Applicant)
[ ] Legal Status of Applicant    : [Individual / Private Limited / LLP / Partnership]
[ ] Registered Office Address    : _________________________________________________
[ ] State & PIN Code             : _________________________________________________
[ ] Corporate Identity No. (CIN) : _________________________________________________
[ ] GSTIN / Business PAN         : _________________________________________________
[ ] Authorized Signatory Name    : _________________________________________________
[ ] Designation of Signatory     : [Director / Managing Partner / Proprietor]
[ ] Official Contact Email       : _________________________________________________
[ ] Official Contact Mobile Phone: _________________________________________________

--------------------------------------------------------------------------------
3. NATURE OF APPLICANT'S INTEREST (STATEMENT OF PARTICULARS COL 3)
--------------------------------------------------------------------------------
Select one of the statutory ownership options:
[ ] OPTION A: Author is the Applicant (Individual Ownership).
[ ] OPTION B: Work Made for Hire under Section 17(c) of Copyright Act, 1957.
    (Author created the software in the course of employment under a contract of service).
[ ] OPTION C: Ownership acquired through Assignment Deed under Section 19.
    (Formal Copyright Assignment Deed executed between Author and Applicant Company).

Mandatory Attachments for Option B/C:
[ ] Executed No Objection Certificate (NOC) from Author to Applicant Entity.
[ ] Certified true copy of Employment Agreement OR Assignment Deed.

--------------------------------------------------------------------------------
4. CHRONOLOGICAL DEVELOPMENT DATES (STATEMENT OF PARTICULARS COL 8 & 9)
--------------------------------------------------------------------------------
[ ] Date of Commencement of Code : DD / MM / YYYY  [e.g. 01/08/2026]
[ ] Date of Completion of Code   : DD / MM / YYYY  [e.g. 30/10/2026]
[ ] Publication Status           : [ ] Published   [ ] Unpublished
    - If Published:
      * Date of First Publication: DD / MM / YYYY
      * Country of First Pub.    : India
      * Name & Address of Pub.   : _________________________________________________
    - If Unpublished:
      * State year of creation   : 2026
      * Location of creation     : _________________________________________________

--------------------------------------------------------------------------------
5. POWER OF ATTORNEY / LEGAL REPRESENTATION (IF APPLICABLE)
--------------------------------------------------------------------------------
[ ] Will the application be filed directly by the applicant or via an IP Advocate/Agent?
    - If Advocate/Agent:
      * Advocate / Agent Name    : _________________________________________________
      * Bar Council Enrolment No.: _________________________________________________
      * Form XIV Vakalatnama/POA : Executed and stamped on requisite Non-Judicial Stamp Paper.

--------------------------------------------------------------------------------
6. GOVERNMENT STATUTORY FEE PAYMENT (SCHEDULE II, COPYRIGHT RULES, 2013)
--------------------------------------------------------------------------------
[ ] Statutory Fee for Literary / Software Work:
    - ₹500 for Individual / Non-commercial applicant
    - ₹2,000 for Corporate / Company / Commercial applicant
[ ] Payment mode: Online Bharatkosh gateway via copyright.gov.in.

================================================================================
END OF MISSING INFORMATION CHECKLIST
================================================================================
""")

xlsx_path = os.path.join(DOCS_DIR, "SOURCE_CODE_INVENTORY.xlsx")
wb.save(xlsx_path)
print(f"Generated SOURCE_CODE_INVENTORY.xlsx successfully at {xlsx_path}")
print("Generated verification/project_analysis.txt and verification/missing_information.txt")
