# 📦 Third-Party Dependencies & Open Source Software Disclosure

**Software Application:** ARB SoftTech AI Enterprise Voice Calling Agent Platform — Frontend Software  
**Package Identifier:** `voxora-enterprise-ai-voice` (v2.0.0 Production)  
**Jurisdiction:** Republic of India  
**Statutory Framework:** Indian Copyright Act, 1957 & Copyright Rules, 2013 (as amended)  
**Filing Reference:** Statement of Further Particulars (SoFP) accompanying Form XIV (Computer Software)

---

## 1. Statutory Statement & Carve-Out Disclaimer

In accordance with the requirements of the Indian Copyright Office and established principles under the **Indian Copyright Act, 1957**, the Applicant hereby expressly discloses and records the third-party software libraries, runtimes, utilities, and development dependencies utilized in the construction, compilation, and execution of the frontend client application.

> **LEGAL NOTICE & CARVE-OUT OF THIRD-PARTY CODE:**  
> The Applicant **does NOT claim** any proprietary copyright, authorship, or exclusive ownership over any third-party open-source libraries, node modules, frameworks, compilers, fonts, or third-party assets identified herein.  
> 
> All third-party software packages remain the exclusive intellectual property of their respective copyright holders and licensors under their designated permissive licenses (including the MIT License, Apache License 2.0, ISC License, and GreenSock Standard License).  
> 
> Copyright protection is claimed **strictly and exclusively** over the original, custom-authored frontend source code, software architecture, user interface component hierarchy, proprietary state logic, telephony integration routines, dynamic branching questionnaire editors, AI voice agent studio interfaces, custom CSS/Tailwind animations, and unique compilation and arrangement of elements created by or on behalf of the Applicant.

---

## 2. Production Runtime Dependencies

The following open-source dependencies are linked and bundled into the production client application executed in the end-user's web browser:

| Sl. No. | Package Name | Declared Version | Primary License | Copyright Holder / Maintainer | Purpose & Functional Role in Frontend |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `react` | `^18.3.1` | MIT License | Meta Platforms, Inc. & React Contributors | Core declarative UI component runtime and virtual DOM engine. |
| 2 | `react-dom` | `^18.3.1` | MIT License | Meta Platforms, Inc. & React Contributors | DOM rendering engine for web browser mounts. |
| 3 | `react-router-dom` | `^6.28.1` | MIT License | Remix Software, Inc. / Shopify | Client-side routing, navigation history, and route state management. |
| 4 | `@tanstack/react-query` | `^5.62.7` | MIT License | Tanner Linsley & TanStack Contributors | Asynchronous server-state management, cache synchronization, and background revalidation. |
| 5 | `axios` | `^1.7.9` | MIT License | Matt Zabriskie & Axios Contributors | Promise-based HTTP client for RESTful backend communication and telephony controls. |
| 6 | `zustand` | `^5.0.2` | MIT License | Paul Henschel & Zustand Contributors | Lightweight, un-opinionated global client state store (modals, active tabs, layout settings). |
| 7 | `recharts` | `^2.15.0` | MIT License | Recharts Group & Open Source Community | SVG-based charting library for telephony telemetry, call duration graphs, and conversion rates. |
| 8 | `lucide-react` | `^0.469.0` | ISC License | Lucide Project Contributors | Standardized SVG vector icon library for dashboard UI elements. |
| 9 | `tailwindcss` / `tailwind-merge` | `^2.6.0` | MIT License | Tailwind Labs, Inc. | Utility-first CSS class deduplication and styling resolution. |
| 10 | `clsx` | `^2.1.1` | MIT License | Luke Edwards | Conditional CSS class constructor utility. |
| 11 | `date-fns` | `^4.1.0` | MIT License | Sasha Koss & Lesha Koss | Modular date manipulation and formatting library for call timestamps and schedules. |
| 12 | `react-hook-form` | `^7.54.2` | MIT License | BeikVer & React Hook Form Contributors | High-performance, declarative form state handling and input validation. |
| 13 | `@hookform/resolvers` | `^3.9.1` | MIT License | React Hook Form Contributors | Form validation resolver bridging React Hook Form with Zod schemas. |
| 14 | `zod` | `^3.24.1` | MIT License | Colin McDonnell | TypeScript-first schema declaration and runtime data validation library. |
| 15 | `gsap` | `^3.15.0` | GreenSock Standard | GreenSock, Inc. | High-performance JavaScript animation engine for ambient background and UI micro-interactions. |
| 16 | `jspdf` | `^4.2.1` | MIT License | James Hall & Parvez | Client-side PDF generation engine for agent and business dossier exports. |
| 17 | `jspdf-autotable` | `^5.0.8` | MIT License | Simon Tenggren | Table generation plugin for jsPDF used in reporting and analytics exports. |
| 18 | `xlsx` | `^0.18.5` | Apache 2.0 | SheetJS LLC | Spreadsheet parser and generator for call records and questionnaire bulk import/export. |
| 19 | `papaparse` | `^5.4.1` | MIT License | Matt Holt & PapaParse Contributors | In-browser CSV parsing engine for contact list bulk uploads. |

---

## 3. Build & Development Tooling Dependencies

The following software packages are utilized strictly in the local development, compilation, transpilation, and type-checking environments and are **not** distributed as standalone runtime components:

| Sl. No. | Package Name | Version | License | Developer / Maintainer | Role in Development Pipeline |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `typescript` | `~5.6.3` | Apache 2.0 | Microsoft Corporation | Static typing, interface verification, and AST transpilation. |
| 2 | `vite` | `^6.0.5` | MIT License | Evan You & Vite Contributors | Next-generation frontend build tool and Rollup-based production bundler. |
| 3 | `@vitejs/plugin-react` | `^4.3.4` | MIT License | Vite Contributors | Fast Refresh and JSX transformation plugin for Vite. |
| 4 | `tailwindcss` | `^3.4.17` | MIT License | Tailwind Labs, Inc. | Utility-first CSS compiler and JIT engine. |
| 5 | `postcss` | `^8.4.49` | MIT License | Andrey Sitnik & PostCSS Contributors | CSS transformation pipeline and vendor prefixing. |
| 6 | `autoprefixer` | `^10.4.20` | MIT License | Andrey Sitnik & Contributors | Automated CSS vendor prefix injection for cross-browser support. |
| 7 | `@types/react` | `^18.3.18` | MIT License | DefinitelyTyped Community | TypeScript type definitions for React. |
| 8 | `@types/react-dom` | `^18.3.5` | MIT License | DefinitelyTyped Community | TypeScript type definitions for ReactDOM. |
| 9 | `@types/node` | `^22.10.2` | MIT License | DefinitelyTyped Community | TypeScript type definitions for Node.js APIs. |
| 10 | `@types/papaparse` | `^5.3.15` | MIT License | DefinitelyTyped Community | TypeScript type definitions for PapaParse. |

---

## 4. Typography & External Web Resources

The application references external web typography hosted on Google Fonts servers for on-screen display:
- **Inter** (SIL Open Font License 1.1) by Rasmus Andersson
- **Plus Jakarta Sans** (SIL Open Font License 1.1) by Tokotype
- **JetBrains Mono** (SIL Open Font License 1.1) by JetBrains s.r.o.

These fonts are loaded at runtime via `<link>` elements in `index.html` and are not distributed or claimed as proprietary assets.

---

## 5. Compliance with Section 52 of the Indian Copyright Act, 1957

Section 52 of the Indian Copyright Act, 1957 establishes statutory exceptions to copyright infringement ("fair dealing"). Under Sections 52(1)(aa), 52(1)(ab), and 52(1)(ac):
1. The utilization, compilation, linking, and interoperability testing of third-party libraries for the purpose of achieving interoperability of an independently created computer program with other programs does not constitute an infringement of copyright.
2. The Applicant confirms that all open-source libraries have been incorporated in accordance with their respective open-source license agreements, maintaining all copyright notices and disclaimers intact.
3. No proprietary claim is advanced over any open-source dependency.

---

*This document forms an integral part of the Copyright Registration Documentation Package submitted under the Copyright Rules, 2013.*

