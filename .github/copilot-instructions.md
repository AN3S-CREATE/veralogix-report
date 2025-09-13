# Veralogix Report - Mining Solution Website

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

This is a static HTML single-page application showcasing Veralogix Group SA's Smart Mining Solution. It's a marketing/presentation website with interactive charts and responsive design, deployed via GitHub Pages.

## Working Effectively

### Quick Start (No Build Required)
- This is a **static website** - no build process, compilation, or package management needed
- Simply serve the HTML file directly:
  - `cd /path/to/repository`
  - `python3 -m http.server 8080` -- starts immediately, no timeout needed
  - Navigate to `http://localhost:8080/` to view the site
- **CRITICAL**: External CDNs may be blocked in restricted environments (Tailwind CSS, Chart.js, Google Fonts) but the site structure remains functional

### Repository Structure
```
/
├── README.md           # Company information and licensing
├── index.html          # Complete single-page application (659 lines)
└── .github/
    └── copilot-instructions.md
```

### Dependencies & External Resources
The website uses CDN-hosted resources:
- **Tailwind CSS**: `https://cdn.tailwindcss.com` (styling framework)
- **Chart.js**: `https://cdn.jsdelivr.net/npm/chart.js` (interactive charts)
- **Google Fonts**: Montserrat and Inter fonts
- **External Images**: Various hosted images on iili.io, freeimage.host, imgur

**Important**: In restricted network environments, these external resources may be blocked, causing styling and chart functionality to fail, but the core content remains accessible.

## Validation

### Manual Testing Scenarios
**ALWAYS perform these validation steps after making any changes:**

1. **Basic Serving Test**:
   - `python3 -m http.server 8080`
   - Open `http://localhost:8080/` in browser
   - Verify page loads with title "Veralogix | Let's Mine Smarter, Together"
   - **Expected Time**: Immediate startup, no build time

2. **Content Validation**:
   - Verify navigation menu appears with links: LOADSCAN®, TRIMBLE®, CABIN-EYE™, VTOL DRONES™, SENTRYMINE™
   - Confirm hero section displays "YOUR ROI SUCCESS IS AUTONOMOUS"
   - Check that tabbed interface for solution pillars is present
   - Verify footer shows "© 2025 Veralogix Group. All rights reserved."

3. **Interactive Elements** (may fail in restricted environments):
   - Test search box functionality
   - Verify tab navigation works between solution pillars
   - Check if charts render (Haulage Optimization, Safety Incursions)
   - Validate smooth scrolling navigation links

4. **Screenshot Validation**:
   - Take a full-page screenshot to verify visual layout
   - Ensure responsive design elements are functioning
   - **ALWAYS capture and review screenshots when making visual changes**

### File Integrity Checks
- **HTML Validation**: `file index.html` should report "HTML document, Unicode text, UTF-8 text"
- **Size Check**: `wc -l index.html` should report ~659 lines
- **Content Search**: `grep -i "veralogix\|mining" index.html` should return multiple matches

## Common Tasks

### Making Content Changes
- **Edit the HTML directly**: `index.html` contains all content, styling, and JavaScript
- **Testing**: Immediately refresh browser after saving changes - no build step required
- **Validation**: Always test both with and without external CDN access

### Adding New Sections
- Follow existing HTML structure and CSS classes
- Use Tailwind CSS classes for styling consistency
- Test interactive elements if adding JavaScript functionality
- Ensure responsive design on different screen sizes

### Troubleshooting External Dependencies
If external resources fail to load:
- **Expected behavior**: Site loads but without styling/charts
- **Not a code issue**: This indicates network restrictions, not broken code
- **Workaround**: Download and host resources locally if needed for full functionality

## File Contents Reference

### README.md Summary
```
Company: Veralogix Group (Pty) Ltd
Registration: 2018/407824/07
Purpose: GitHub Pages repository for Smart Mining Solution website
License: All rights reserved - not open source
Contact: info@veralogixgroup.co.za
```

### index.html Key Sections
- **Line 1-50**: Document head with CDN resources and meta tags
- **Line 51-200**: Hero section and navigation
- **Line 201-400**: Problem narrative with "Tshepo's Journey"
- **Line 401-600**: Solution pillars (Loadscan, Trimble, Cabin-Eye, VTOL Drones)
- **Line 601-659**: Smart Hub integration and call-to-action

## Critical Reminders

- **No Build Process**: This is pure HTML/CSS/JavaScript - serve directly
- **No Package Management**: No npm, pip, or other dependency management needed
- **No Compilation**: No TypeScript, Sass, or preprocessing required
- **External Dependencies**: May fail in restricted environments - document this, don't try to "fix" it
- **GitHub Pages Ready**: Repository is configured for direct GitHub Pages deployment
- **Copyright Protected**: All content is proprietary to Veralogix Group SA

## Workflow Validation Commands
Use these exact commands to validate the repository:

```bash
# Navigate to repository
cd /path/to/veralogix-report

# Verify repository structure
ls -la
# Expected: README.md, index.html, .git/, .github/

# Check file integrity
file index.html
# Expected: HTML document, Unicode text, UTF-8 text

# Start local server
python3 -m http.server 8080
# Expected: Immediate startup on port 8080

# Test in another terminal
curl -I http://localhost:8080/
# Expected: HTTP/1.0 200 OK, Content-type: text/html

# Content verification
grep -c "Veralogix" index.html
# Expected: Multiple matches (should be > 10)
```

**Remember**: This is a presentation website, not a development project. Focus on content accuracy and visual presentation rather than complex build processes or testing frameworks.