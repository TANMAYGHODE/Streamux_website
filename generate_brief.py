import base64
import os
import subprocess

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return ""
    ext = os.path.splitext(image_path)[1].lower()
    mime = "image/png"
    if ext == ".svg":
        mime = "image/svg+xml"
    elif ext in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{data}"

streamux_logo = get_base64_image("assets/logo/Streamux_The_New_Era_Of_Empowerment.png")

nvidia_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 20" height="19">
  <rect width="120" height="20" rx="3" fill="#000000"/>
  <path d="M12 4.5C8.4 4.5 5.5 7.4 5.5 11C5.5 14.6 8.4 17.5 12 17.5C14.8 17.5 17.2 15.7 18.1 13.2H15.8C15.1 14.5 13.6 15.5 12 15.5C9.5 15.5 7.5 13.5 7.5 11C7.5 8.5 9.5 6.5 12 6.5C13.6 6.5 15.1 7.5 15.8 8.8H18.1C17.2 6.3 14.8 4.5 12 4.5Z" fill="#76B900"/>
  <circle cx="12" cy="11" r="2.2" fill="#76B900"/>
  <text x="23" y="13.5" fill="#ffffff" font-family="'Helvetica Neue', Arial, sans-serif" font-size="8" font-weight="bold" letter-spacing="0.5">INCEPTION</text>
  <text x="75" y="13.5" fill="#76B900" font-family="'Helvetica Neue', Arial, sans-serif" font-size="8" font-weight="bold">MEMBER</text>
</svg>"""
nvidia_base64 = f"data:image/svg+xml;base64,{base64.b64encode(nvidia_svg.encode('utf-8')).decode('utf-8')}"

img_fight = get_base64_image("assets/images/thumbnails/thumb_fight.jpg")
img_gate = get_base64_image("assets/images/thumbnails/thumb_gate.jpg")
img_ppe = get_base64_image("assets/images/thumbnails/thumb_ppe.jpg")
img_temple = get_base64_image("assets/images/thumbnails/thumb_temple.jpg")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Streamux AI - Visual Executive Brief for Government & Public Sector</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 5mm 8mm 5mm 8mm;
  }}
  
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    color: #0f172a;
    background: #ffffff;
    font-size: 8.3pt;
    line-height: 1.35;
    height: 100%;
  }}

  a {{
    color: #1d4ed8;
    text-decoration: none;
    font-weight: 600;
  }}

  /* Top Header */
  .header-table {{
    width: 100%;
    border-collapse: collapse;
    padding-bottom: 5px;
    border-bottom: 2px solid #0f172a;
    margin-bottom: 5px;
  }}

  .logo-img {{
    height: 38px;
    display: block;
  }}

  .header-right {{
    text-align: right;
    vertical-align: middle;
  }}

  .nvidia-pill {{
    display: inline-block;
    vertical-align: middle;
    margin-bottom: 3px;
  }}

  .gov-subtag {{
    font-size: 7.2pt;
    font-weight: 700;
    color: #334155;
    letter-spacing: 0.4px;
    text-transform: uppercase;
  }}

  /* Title Banner */
  .title-banner {{
    background: linear-gradient(90deg, #0b1120 0%, #1e293b 100%);
    color: #ffffff;
    padding: 7px 10px;
    border-radius: 4px;
    margin-bottom: 7px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .title-main {{
    font-size: 11pt;
    font-weight: 800;
    letter-spacing: 0.3px;
    text-transform: uppercase;
    color: #ffffff;
  }}

  .title-sub {{
    font-size: 7.5pt;
    color: #94a3b8;
    margin-top: 1.5px;
    font-weight: 500;
  }}

  .badge-tag {{
    background: linear-gradient(135deg, #ea580c, #c2410c);
    color: #ffffff;
    font-size: 7pt;
    font-weight: 700;
    padding: 4px 9px;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    white-space: nowrap;
  }}

  /* Section Headings */
  .section-heading {{
    font-size: 8.4pt;
    font-weight: 800;
    text-transform: uppercase;
    color: #0f172a;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 2.5px;
    margin: 6px 0 5px 0;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}

  .section-heading-tag {{
    font-size: 6.8pt;
    color: #64748b;
    font-weight: 600;
    text-transform: none;
  }}

  /* Visual Architecture Pipeline Infographic */
  .arch-container {{
    border: 1.5px solid #cbd5e1;
    border-radius: 5px;
    background: #f8fafc;
    padding: 7px 9px;
    margin-bottom: 7px;
  }}

  .arch-title-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
  }}

  .arch-heading {{
    font-size: 7.9pt;
    font-weight: 800;
    text-transform: uppercase;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 5px;
  }}

  .arch-pill {{
    font-size: 6.6pt;
    font-weight: 700;
    background: #ecfdf5;
    color: #047857;
    border: 1px solid #a7f3d0;
    padding: 2px 8px;
    border-radius: 3px;
  }}

  .arch-steps {{
    display: grid;
    grid-template-columns: 1fr auto 1.15fr auto 1fr auto 1.15fr;
    gap: 6px;
    align-items: center;
  }}

  .arch-box {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 6px;
    text-align: center;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
  }}

  .arch-box-icon {{
    font-size: 13pt;
    line-height: 1;
    margin-bottom: 3px;
  }}

  .arch-box-title {{
    font-size: 7.3pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
  }}

  .arch-box-desc {{
    font-size: 6.3pt;
    color: #64748b;
    margin-top: 2px;
    line-height: 1.2;
  }}

  .arch-arrow {{
    color: #0284c7;
    font-size: 12pt;
    font-weight: 900;
    text-align: center;
  }}

  /* Visual Comparison Chart / Graphs */
  .comparison-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6px;
    margin-bottom: 7px;
  }}

  .chart-card {{
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    background: #ffffff;
    padding: 6px 8px;
  }}

  .chart-card-title {{
    font-size: 7.2pt;
    font-weight: 800;
    color: #1e293b;
    text-transform: uppercase;
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .bar-group {{
    margin-bottom: 3px;
  }}

  .bar-label-row {{
    display: flex;
    justify-content: space-between;
    font-size: 6.2pt;
    font-weight: 600;
    color: #475569;
    margin-bottom: 1.5px;
  }}

  .bar-bg {{
    height: 9px;
    background: #f1f5f9;
    border-radius: 4.5px;
    overflow: hidden;
    position: relative;
    border: 1px solid #e2e8f0;
  }}

  .bar-fill-red {{
    height: 100%;
    width: 90%;
    background: linear-gradient(90deg, #ef4444, #dc2626);
    border-radius: 3px;
  }}

  .bar-fill-green {{
    height: 100%;
    width: 8%;
    background: linear-gradient(90deg, #22c55e, #16a34a);
    border-radius: 3px;
  }}

  .bar-fill-green-wide {{
    height: 100%;
    width: 99%;
    background: linear-gradient(90deg, #22c55e, #16a34a);
    border-radius: 3px;
  }}

  .bar-fill-red-low {{
    height: 100%;
    width: 10%;
    background: linear-gradient(90deg, #ef4444, #dc2626);
    border-radius: 3px;
  }}

  /* 4 Visual AI Solution Cards with Embedded Demo Images (Larger & Taller) */
  .solutions-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-bottom: 7px;
  }}

  .solution-card {{
    border: 1.5px solid #cbd5e1;
    border-radius: 5px;
    background: #ffffff;
    padding: 6px 8px;
    display: flex;
    gap: 9px;
    align-items: center;
  }}

  .solution-img-box {{
    width: 110px;
    height: 72px;
    border-radius: 4px;
    overflow: hidden;
    flex-shrink: 0;
    border: 1.5px solid #64748b;
    background: #0b1120;
    position: relative;
  }}

  .solution-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}

  .ai-overlay-badge {{
    position: absolute;
    bottom: 2px;
    right: 2px;
    background: rgba(0, 0, 0, 0.82);
    color: #38bdf8;
    font-size: 5.5pt;
    font-weight: 800;
    padding: 1px 4.5px;
    border-radius: 2px;
    border: 0.5px solid #0284c7;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}

  .solution-content {{
    flex: 1;
    min-width: 0;
  }}

  .solution-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3px;
  }}

  .solution-title {{
    font-size: 7.9pt;
    font-weight: 800;
    color: #0f172a;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  .solution-pill {{
    font-size: 6pt;
    font-weight: 700;
    padding: 1.5px 6px;
    border-radius: 2px;
    text-transform: uppercase;
  }}

  .pill-blue {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
  .pill-orange {{ background: #fff7ed; color: #c2410c; border: 1px solid #fed7aa; }}
  .pill-green {{ background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }}
  .pill-purple {{ background: #faf5ff; color: #7e22ce; border: 1px solid #e9d5ff; }}

  .solution-bullets {{
    list-style: none;
    padding: 0;
  }}

  .solution-bullets li {{
    font-size: 6.8pt;
    color: #334155;
    position: relative;
    padding-left: 10px;
    margin-bottom: 2.5px;
    line-height: 1.25;
  }}

  .solution-bullets li:last-child {{
    margin-bottom: 0;
  }}

  .solution-bullets li::before {{
    content: "▸";
    position: absolute;
    left: 0;
    font-size: 6.5pt;
    color: #0284c7;
    top: -0.5px;
  }}

  /* Government Department Matrix Table */
  .matrix-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 7px;
    font-size: 6.9pt;
  }}

  .matrix-table th {{
    background: #1e293b;
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 4px 7px;
    font-size: 6.8pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}

  .matrix-table td {{
    padding: 3.5px 7px;
    border: 1px solid #cbd5e1;
    color: #334155;
    vertical-align: middle;
  }}

  .matrix-table tr:nth-child(even) td {{
    background: #f8fafc;
  }}

  .dept-title {{
    font-weight: 800;
    color: #0f172a;
    display: block;
    font-size: 7.1pt;
  }}

  /* Strategic Advantages Pillars */
  .pillars-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6px;
    margin-bottom: 7px;
  }}

  .pillar-card {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 5px 7px;
  }}

  .pillar-title {{
    font-size: 7.4pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 4px;
  }}

  .pillar-desc {{
    font-size: 6.6pt;
    color: #475569;
    line-height: 1.28;
  }}

  /* KPI Metrics Dark Strip */
  .metrics-row {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px;
    background: #0f172a;
    color: #ffffff;
    border-radius: 5px;
    padding: 6px 8px;
    text-align: center;
    margin-bottom: 7px;
  }}

  .metric-item {{
    border-right: 1px solid #334155;
  }}
  .metric-item:last-child {{
    border-right: none;
  }}

  .metric-val {{
    font-size: 11pt;
    font-weight: 800;
    color: #38bdf8;
    line-height: 1.05;
  }}

  .metric-lbl {{
    font-size: 6.2pt;
    font-weight: 600;
    color: #cbd5e1;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-top: 1px;
  }}

  /* 3-Step Pilot PoC Workflow */
  .poc-container {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 5px;
    padding: 5.5px 8px;
    margin-bottom: 7px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .poc-tag {{
    font-size: 7.4pt;
    font-weight: 800;
    color: #1e3a8a;
    text-transform: uppercase;
  }}

  .poc-step {{
    font-size: 6.8pt;
    color: #1e3a8a;
    display: flex;
    align-items: center;
    gap: 4px;
  }}

  .poc-num {{
    background: #1d4ed8;
    color: #ffffff;
    font-weight: 800;
    border-radius: 50%;
    width: 14.5px;
    height: 14.5px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 6.2pt;
  }}

  /* Footer & Official Links Box */
  .footer-box {{
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 6px 9px;
  }}

  .links-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 4px;
  }}

  .links-table td {{
    font-size: 6.8pt;
    vertical-align: top;
    padding: 1px 3px;
    line-height: 1.3;
  }}

  .link-label {{
    font-weight: 700;
    color: #1e293b;
  }}

  .bottom-bar {{
    border-top: 1px solid #cbd5e1;
    padding-top: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 6.6pt;
    color: #475569;
  }}

  .contact-highlight {{
    font-weight: 700;
    color: #0f172a;
  }}
</style>
</head>
<body>

  <!-- Header -->
  <table class="header-table">
    <tr>
      <td style="vertical-align: middle;">
        <img src="{streamux_logo}" alt="Streamux AI - The New Era of Empowerment" class="logo-img">
      </td>
      <td class="header-right">
        <div class="nvidia-pill">
          <img src="{nvidia_base64}" alt="NVIDIA Inception Member" style="height: 18px; display: inline-block;">
        </div>
        <div class="gov-subtag">
          Make in India Deep-Tech &bull; DPIIT Recognised Startup &bull; HQ: Nagpur, MH
        </div>
      </td>
    </tr>
  </table>

  <!-- Title Banner -->
  <div class="title-banner">
    <div>
      <div class="title-main">Executive Brief: Real-Time AI Video Analytics for Public Infrastructure</div>
      <div class="title-sub">Turnkey Edge Intelligence Transforming Existing CCTV Cameras into Automated Public Safety Sentinels</div>
    </div>
    <div class="badge-tag">Government & PSU Brief</div>
  </div>

  <!-- Infographic 1: Visual Architecture Pipeline -->
  <div class="arch-container">
    <div class="arch-title-row">
      <div class="arch-heading">&#9881; System Architecture: Non-Intrusive Edge AI Pipeline</div>
      <div class="arch-pill">&#10004; 100% On-Premise &bull; Zero Video Cloud Egress &bull; Internet Independent</div>
    </div>
    <div class="arch-steps">
      <div class="arch-box">
        <div class="arch-box-icon">&#128249;</div>
        <div class="arch-box-title">Existing CCTV / RTSP</div>
        <div class="arch-box-desc">Legacy IP, Dome, Bullet & PTZ cameras (0% hardware replacement)</div>
      </div>
      <div class="arch-arrow">&#10140;</div>
      <div class="arch-box">
        <div class="arch-box-icon">&#128187;</div>
        <div class="arch-box-title">NVIDIA Edge AI Node</div>
        <div class="arch-box-desc">On-Premise Jetson Orin or Local GPU Server in your command</div>
      </div>
      <div class="arch-arrow">&#10140;</div>
      <div class="arch-box">
        <div class="arch-box-icon">&#129504;</div>
        <div class="arch-box-title">Sub-50ms Inference</div>
        <div class="arch-box-desc">TensorRT & DeepStream accelerated computer vision models</div>
      </div>
      <div class="arch-arrow">&#10140;</div>
      <div class="arch-box">
        <div class="arch-box-icon">&#128680;</div>
        <div class="arch-box-title">Instant Action Relays</div>
        <div class="arch-box-desc">ICCC screen popups, automated boom barriers, siren & SMS dispatch</div>
      </div>
    </div>
  </div>

  <!-- Infographic 2: Comparative Bar Charts / Graphs (3 Charts) -->
  <div class="comparison-grid">
    <!-- Chart 1: Response Time -->
    <div class="chart-card">
      <div class="chart-card-title">
        <span>&#9201; Incident Response</span>
        <span style="color: #15803d; font-weight: 800;">30x Faster</span>
      </div>
      <div class="bar-group">
        <div class="bar-label-row">
          <span>Manual CCTV</span>
          <span style="color: #b91c1c;">20 - 30 Mins (Delayed)</span>
        </div>
        <div class="bar-bg"><div class="bar-fill-red"></div></div>
      </div>
      <div class="bar-group">
        <div class="bar-label-row">
          <span><strong>Streamux AI</strong></span>
          <span style="color: #15803d;"><strong>&lt; 50 ms (Instant)</strong></span>
        </div>
        <div class="bar-bg"><div class="bar-fill-green"></div></div>
      </div>
    </div>

    <!-- Chart 2: Threat Prevention Effectiveness -->
    <div class="chart-card">
      <div class="chart-card-title">
        <span>&#128737; Threat Detection</span>
        <span style="color: #15803d; font-weight: 800;">99% Accuracy</span>
      </div>
      <div class="bar-group">
        <div class="bar-label-row">
          <span>Passive CCTV</span>
          <span style="color: #b91c1c;">0% (Post-Disaster)</span>
        </div>
        <div class="bar-bg"><div class="bar-fill-red-low"></div></div>
      </div>
      <div class="bar-group">
        <div class="bar-label-row">
          <span><strong>Streamux AI</strong></span>
          <span style="color: #15803d;"><strong>99% Live Alerts</strong></span>
        </div>
        <div class="bar-bg"><div class="bar-fill-green-wide"></div></div>
      </div>
    </div>

    <!-- Chart 3: Infrastructure Protection -->
    <div class="chart-card">
      <div class="chart-card-title">
        <span>&#128274; Data Sovereignty</span>
        <span style="color: #15803d; font-weight: 800;">100% Private</span>
      </div>
      <div class="bar-group">
        <div class="bar-label-row">
          <span>Foreign Cloud</span>
          <span style="color: #b91c1c;">High Egress Risk</span>
        </div>
        <div class="bar-bg"><div class="bar-fill-red"></div></div>
      </div>
      <div class="bar-group">
        <div class="bar-label-row">
          <span><strong>Streamux Edge</strong></span>
          <span style="color: #15803d;"><strong>0% Video Egress</strong></span>
        </div>
        <div class="bar-bg"><div class="bar-fill-green-wide"></div></div>
      </div>
    </div>
  </div>

  <!-- Section: 4 Core AI Solutions with Embedded Real Video Thumbnails (Larger Photos) -->
  <div class="section-heading">
    <span>Turnkey AI Vision Modules & Real-Time Demonstrations</span>
    <span class="section-heading-tag">Real Production Model Overlays</span>
  </div>

  <div class="solutions-grid">
    <!-- 1. Smart City & Law Enforcement -->
    <div class="solution-card">
      <div class="solution-img-box">
        <img src="{img_fight}" alt="Fight Detection AI" class="solution-img">
        <div class="ai-overlay-badge">AI ACTIVE</div>
      </div>
      <div class="solution-content">
        <div class="solution-header">
          <span class="solution-title">1. Law Enforcement & Public Safety</span>
          <span class="solution-pill pill-blue">ICCC Police</span>
        </div>
        <ul class="solution-bullets">
          <li><strong>Fight & Violence Detection:</strong> Pose-temporal neural alerts on brawls.</li>
          <li><strong>Virtual Perimeter Tripwires:</strong> Restricted perimeter breach alarms.</li>
          <li><strong>Watchlist Facial Recognition:</strong> ArcFace 512-D vector verification.</li>
        </ul>
      </div>
    </div>

    <!-- 2. Smart Gate & Urban Mobility -->
    <div class="solution-card">
      <div class="solution-img-box">
        <img src="{img_gate}" alt="Smart Gate ANPR AI" class="solution-img">
        <div class="ai-overlay-badge">ANPR OCR</div>
      </div>
      <div class="solution-content">
        <div class="solution-header">
          <span class="solution-title">2. Smart Gate & Urban Mobility (SGM)</span>
          <span class="solution-pill pill-green">Traffic / NHAI</span>
        </div>
        <ul class="solution-bullets">
          <li><strong>Sub-Second Indian ANPR:</strong> High-precision OCR for all plates.</li>
          <li><strong>Automated Boom Barrier:</strong> Instant contactless gate triggering.</li>
          <li><strong>Live Traffic & Occupancy:</strong> Automated IN/OUT audit CSV logs.</li>
        </ul>
      </div>
    </div>

    <!-- 3. Industrial & Public Works Safety -->
    <div class="solution-card">
      <div class="solution-img-box">
        <img src="{img_ppe}" alt="PPE Detection AI" class="solution-img">
        <div class="ai-overlay-badge">OSHA AUDIT</div>
      </div>
      <div class="solution-content">
        <div class="solution-header">
          <span class="solution-title">3. Critical Infra & Public Works</span>
          <span class="solution-pill pill-purple">PWD / PSUs</span>
        </div>
        <ul class="solution-bullets">
          <li><strong>PPE Compliance Tracking:</strong> Automated helmets & vest audits.</li>
          <li><strong>Flame & Smoke Early Warning:</strong> Seconds before thermal alarms.</li>
          <li><strong>Worker Slips & Falls:</strong> Instant exclusion zone breach alerts.</li>
        </ul>
      </div>
    </div>

    <!-- 4. Devotee & Mass Gathering (AI Netra) -->
    <div class="solution-card">
      <div class="solution-img-box">
        <img src="{img_temple}" alt="Devotee & Stampede AI Netra" class="solution-img">
        <div class="ai-overlay-badge">AI NETRA</div>
      </div>
      <div class="solution-content">
        <div class="solution-header">
          <span class="solution-title">4. Devotee & Crowd Safety (AI Netra)</span>
          <span class="solution-pill pill-orange">Stampede Guard</span>
        </div>
        <ul class="solution-bullets">
          <li><strong>Devotee Headcount Analytics:</strong> Live crowd density heatmaps.</li>
          <li><strong>Stampede Preemption:</strong> Detects panic surges & corridor blockages.</li>
          <li><strong>Queue Wait-Time Telemetry:</strong> Balances pilgrim batches in real time.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Government Department Matrix Table -->
  <div class="section-heading">
    <span>Departmental Alignment & Governance Impact</span>
    <span class="section-heading-tag">Cross-Departmental Utility</span>
  </div>

  <table class="matrix-table">
    <thead>
      <tr>
        <th style="width: 25%;">Target Department / Authority</th>
        <th style="width: 45%;">Deployed AI Vision Capabilities</th>
        <th style="width: 30%;">Operational Governance Impact</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="dept-title">Smart City Missions & Police (ICCC)</span>City Command Centers, Transit Nodes</td>
        <td>Physical conflict/riot alerts, perimeter tripwires, crowd aggression detection, watchlist match.</td>
        <td>Emergency response reduced from 20 mins to under 60 secs; proactive dispatch.</td>
      </tr>
      <tr>
        <td><span class="dept-title">Temple Trusts & Pilgrimage Boards</span>Yatras, Major Shrines, Cultural Festivals</td>
        <td>AI Netra: Headcount tracking, corridor chokepoints, stampede preemption, darshan queue time.</td>
        <td>Zero stampede casualties; auditable devotee footfalls; optimized crowd dispersal.</td>
      </tr>
      <tr>
        <td><span class="dept-title">Transport, NHAI & Municipalities</span>Toll Plazas, Municipal Parking, Depots</td>
        <td>Smart Gate Management, high-speed ANPR, vehicle classification, automated barrier relays.</td>
        <td>Eliminates vehicular bottlenecks; automated audit trail preventing toll leakages.</td>
      </tr>
      <tr>
        <td><span class="dept-title">Public Works, Ports & PSUs</span>PWD, Mines, Power Plants, Warehouses</td>
        <td>OSHA PPE enforcement (helmets, vests), smoke/fire detection, worker slip/fall alerts, dock logs.</td>
        <td>Workplace fatality prevention; 100% compliance with labor safety mandates.</td>
      </tr>
    </tbody>
  </table>

  <!-- Strategic Government Pillars -->
  <div class="pillars-grid">
    <div class="pillar-card">
      <div class="pillar-title">&#128274; 100% Data Sovereignty</div>
      <div class="pillar-desc">
        Edge-first execution on local GPU hardware. Zero video data egress outside government premises; functions uninterrupted through internet outages.
      </div>
    </div>
    <div class="pillar-card">
      <div class="pillar-title">&#9851; Zero Capex / 100% Retrofit</div>
      <div class="pillar-desc">
        Directly overlays onto existing RTSP/ONVIF CCTV cameras without replacing cables, cameras, or NVRs; maximizes existing civic investments.
      </div>
    </div>
    <div class="pillar-card">
      <div class="pillar-title">&#128640; Indigenous & High-Impact ROI</div>
      <div class="pillar-desc">
        Engineered specifically for Indian conditions, vehicles, and crowds. Zero reliance on foreign cloud servers, imported black-box hardware, or licenses.
      </div>
    </div>
  </div>

  <!-- KPI Metrics Banner -->
  <div class="metrics-row">
    <div class="metric-item">
      <div class="metric-val">99%</div>
      <div class="metric-lbl">Model Accuracy</div>
    </div>
    <div class="metric-item">
      <div class="metric-val">&lt; 50ms</div>
      <div class="metric-lbl">Edge Latency</div>
    </div>
    <div class="metric-item">
      <div class="metric-val">100%</div>
      <div class="metric-lbl">RTSP Compatibility</div>
    </div>
    <div class="metric-item">
      <div class="metric-val">48 Hours</div>
      <div class="metric-lbl">Pilot PoC Turnaround</div>
    </div>
  </div>

  <!-- Government Pilot PoC Workflow -->
  <div class="poc-container">
    <div class="poc-tag">&#9733; 48-Hour Zero-Risk Pilot:</div>
    <div class="poc-step"><span class="poc-num">1</span> <strong>Connect:</strong> Non-intrusive feed tap to 5-10 existing RTSP cameras</div>
    <div class="poc-step"><span class="poc-num">2</span> <strong>Calibrate:</strong> Configure custom alert zones, ANPR gates & tripwires</div>
    <div class="poc-step"><span class="poc-num">3</span> <strong>Evaluate:</strong> Live command dashboard demo on site within 48 hours</div>
  </div>

  <!-- Footer & Official Links Box -->
  <div class="footer-box">
    <table class="links-table">
      <tr>
        <td style="width: 50%;">
          <span class="link-label">&#127760; Official Web Portal:</span> <a href="https://streamux.ai" target="_blank">https://streamux.ai</a><br>
          <span class="link-label">&#128196; Technical Brochures:</span> <a href="https://streamux.ai/solutions.html" target="_blank">https://streamux.ai/solutions.html</a><br>
          <span class="link-label">&#127916; Live Video Demonstrations:</span> <a href="https://streamux.ai/demos.html" target="_blank">https://streamux.ai/demos.html</a>
        </td>
        <td style="width: 50%;">
          <span class="link-label">&#9654; PPE & Workplace Safety Demo:</span> <a href="https://streamux.ai/assets/Demo_Videos/PPE_DETECTION_DEMO.mp4" target="_blank">streamux.ai/demo/ppe</a><br>
          <span class="link-label">&#9654; Public Conflict & Violence Demo:</span> <a href="https://streamux.ai/assets/Demo_Videos/Fight_new.mp4" target="_blank">streamux.ai/demo/fight</a><br>
          <span class="link-label">&#9654; Smart Gate & ANPR Demo:</span> <a href="https://streamux.ai/assets/Demo_Videos/Smart_gate_management.mp4" target="_blank">streamux.ai/demo/gate</a>
        </td>
      </tr>
    </table>

    <div class="bottom-bar">
      <div>
        <span class="contact-highlight">Registered Office:</span> 317, NarayanNarayani, Laxmi Nagar, Near Dikshabhoomi, Nagpur 440022, MH
      </div>
      <div>
        <span class="contact-highlight">Direct Contact:</span> <a href="mailto:contact@streamux.ai">contact@streamux.ai</a> &bull; <a href="tel:+919511874029">+91 9511874029</a>
      </div>
      <div>
        <span class="contact-highlight">Leadership:</span> Aryan N. Ole Patil (CEO) &bull; Tanmay Ghode (Co-Founder)
      </div>
    </div>
  </div>

</body>
</html>
"""

output_html = "Streamux_Government_Executive_Brief.html"
with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Wrote full-page {output_html}")
