import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="AI Learning Impact Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CUSTOM CSS (LIGHTWEIGHT ENTERPRISE)
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* === DESIGN TOKENS === */
:root {
    --bg-primary: #0F172A;
    --bg-surface: #1E293B;
    --border-subtle: #334155;
    --border-medium: #475569;
    --text-primary: #F8FAFC;
    --text-secondary: #CBD5E1;
    --text-muted: #94A3B8;
    --accent-primary: #3B82F6;
    --accent-secondary: #06B6D4;
    --accent-success: #22C55E;
    --accent-warning: #F59E0B;
    --accent-danger: #EF4444;
    --accent-purple: #8B5CF6;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, sans-serif;
    color: var(--text-primary);
}

/* === BACKGROUND === */
[data-testid="stAppViewContainer"] {
    background: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(59, 130, 246, 0.12), transparent),
        radial-gradient(ellipse 60% 50% at 80% 100%, rgba(139, 92, 246, 0.08), transparent),
        linear-gradient(180deg, #0F172A 0%, #0B1120 100%);
    background-attachment: fixed;
}

[data-testid="stHeader"] { background-color: transparent; }

/* === SIDEBAR === */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1120 0%, #131B2E 100%) !important;
    border-right: 1px solid var(--border-subtle);
}

/* === TABS === */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: rgba(30, 41, 59, 0.5);
    border-radius: 14px;
    padding: 6px;
    border: 1px solid var(--border-subtle);
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}
.stTabs [data-baseweb="tab"] p {
    color: var(--text-muted);
    font-size: 14px;
    font-weight: 500;
    margin: 0;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(6, 182, 212, 0.15));
    border: 1px solid rgba(59, 130, 246, 0.3);
}
.stTabs [aria-selected="true"] p {
    color: var(--text-primary);
    font-weight: 600;
}

/* === BUTTON === */
.stButton > button {
    background: linear-gradient(135deg, var(--accent-primary) 0%, #2563EB 100%);
    color: #FFFFFF;
    border-radius: 12px;
    font-weight: 600;
    padding: 10px 24px;
    border: none;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
    color: #FFFFFF;
}

/* === MULTISELECT === */
.stMultiSelect [data-baseweb="tag"] {
    background: rgba(59, 130, 246, 0.2);
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-radius: 8px;
}
.stMultiSelect [data-baseweb="tag"] span { color: var(--text-primary); }

/* === EXPANDER === */
[data-testid="stExpander"] {
    background: rgba(30, 41, 59, 0.4);
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    margin-bottom: 12px;
}
[data-testid="stExpander"] summary span {
    font-weight: 600;
    color: var(--text-primary);
}

/* === METRIC CARDS === */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.4));
    border: 1px solid var(--border-subtle);
    border-radius: 18px;
    padding: 22px 24px;
    position: relative;
    overflow: hidden;
}
div[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent-primary), transparent);
}
div[data-testid="stMetricValue"] {
    color: var(--text-primary);
    font-weight: 700;
    font-size: 34px;
    background: linear-gradient(135deg, #F8FAFC 0%, #CBD5E1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
div[data-testid="stMetricLabel"] {
    color: var(--text-muted);
    font-size: 12px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* === CONTAINER CARDS === */
[data-testid="stVerticalBlockBorderWrapper"] > div,
section[data-testid="stVerticalBlock"] > div {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(15, 23, 42, 0.3));
    border: 1px solid var(--border-subtle);
    border-radius: 20px;
    padding: 24px;
}

/* === HERO === */
.hero-box {
    background:
        radial-gradient(ellipse 100% 100% at 0% 0%, rgba(59, 130, 246, 0.15), transparent 50%),
        radial-gradient(ellipse 80% 100% at 100% 100%, rgba(139, 92, 246, 0.12), transparent 50%),
        linear-gradient(135deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.8));
    padding: 40px;
    border-radius: 24px;
    border: 1px solid rgba(59, 130, 246, 0.2);
    margin-bottom: 24px;
}
.hero-title {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -0.03em;
    margin-bottom: 12px;
    background: linear-gradient(135deg, #F8FAFC 0%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 16px;
    color: var(--text-secondary);
    margin-bottom: 24px;
    line-height: 1.6;
    max-width: 720px;
}
.meta-chip {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid var(--border-subtle);
    border-radius: 10px;
    padding: 8px 14px;
    font-size: 13px;
    color: var(--text-secondary);
    margin-right: 8px;
    margin-bottom: 8px;
}

/* === SECTION DIVIDER === */
.section-divider {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 32px 0 20px 0;
}
.section-divider-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-medium), transparent);
}
.section-divider-title {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--text-muted);
    padding: 6px 14px;
    background: rgba(30, 41, 59, 0.4);
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    gap: 10px;
}
.section-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    color: white;
    font-size: 12px;
    font-weight: 700;
    border-radius: 6px;
}

/* === EXECUTIVE SUMMARY === */
.executive-summary {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(6, 182, 212, 0.05));
    border: 1px solid rgba(59, 130, 246, 0.25);
    border-left: 3px solid var(--accent-primary);
    border-radius: 16px;
    padding: 20px 24px;
    margin: 16px 0;
    color: var(--text-secondary);
    font-size: 14px;
    line-height: 1.7;
}
.executive-summary strong { color: var(--text-primary); }

/* === INSIGHT BOX === */
.insight-box {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.06), rgba(6, 182, 212, 0.04));
    border: 1px solid rgba(34, 197, 94, 0.2);
    border-left: 3px solid var(--accent-success);
    border-radius: 12px;
    padding: 12px 16px;
    margin-top: 16px;
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.6;
}
.insight-box strong { color: var(--accent-success); margin-right: 6px; }

/* === CHART HEADER === */
.chart-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}
.chart-description {
    font-size: 13px;
    color: var(--text-muted);
    margin-bottom: 16px;
}

/* === DATA QUALITY === */
.data-quality-panel {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(15, 23, 42, 0.3));
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 20px 24px;
    margin: 16px 0;
}
.dq-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
    gap: 12px;
    margin-top: 12px;
}
.dq-item {
    background: rgba(15, 23, 42, 0.5);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 12px 14px;
}
.dq-label {
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 4px;
}
.dq-value {
    color: var(--text-primary);
    font-size: 17px;
    font-weight: 600;
}
.semester-badge {
    display: inline-block;
    margin-top: 6px;
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.semester-badge.included {
    background: rgba(59, 130, 246, 0.15);
    color: #3B82F6;
}
.semester-badge.missing {
    background: rgba(245, 158, 11, 0.15);
    color: #F59E0B;
}

/* === MC STATUS === */
.mc-status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(34, 197, 94, 0.1);
    border: 1px solid rgba(34, 197, 94, 0.3);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    color: var(--accent-success);
    font-weight: 600;
    margin-bottom: 12px;
}
.mc-status-dot {
    width: 8px;
    height: 8px;
    background: var(--accent-success);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--accent-success);
}

/* === HEATMAP INTERP === */
.heatmap-interp {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    margin-top: 10px;
}
.heatmap-interp.strong-pos { background: rgba(34, 197, 94, 0.15); color: var(--accent-success); }
.heatmap-interp.weak-neg { background: rgba(239, 68, 68, 0.15); color: var(--accent-danger); }
.heatmap-interp.neutral { background: rgba(148, 163, 184, 0.15); color: var(--text-muted); }

/* === AI INSIGHT === */
.ai-insight-panel {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.08), rgba(59, 130, 246, 0.06));
    border: 1px solid rgba(139, 92, 246, 0.25);
    border-left: 3px solid var(--accent-purple);
    border-radius: 16px;
    padding: 20px 24px;
    margin: 20px 0;
    color: var(--text-secondary);
    font-size: 14px;
    line-height: 1.7;
}
.ai-insight-panel strong { color: var(--accent-purple); }

/* === FOOTER === */
.dashboard-footer {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.4), rgba(15, 23, 42, 0.6));
    border: 1px solid var(--border-subtle);
    border-radius: 18px;
    padding: 24px 28px;
    margin-top: 48px;
    color: var(--text-muted);
    font-size: 13px;
    line-height: 1.7;
}
.dashboard-footer strong { color: var(--text-primary); }
.footer-meta {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 14px;
    padding-top: 14px;
    border-top: 1px solid var(--border-subtle);
    font-size: 12px;
}

/* === GLOBAL TEXT === */
p, h1, h2, h3, h4, h5, h6, label { color: var(--text-primary) !important; }
.stMarkdown { color: var(--text-primary); }

/* === SCROLLBAR === */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb { background: var(--border-medium); border-radius: 5px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-primary); }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DESIGN TOKENS
# ==========================================
SOFT_COLORS = {
    'primary': '#3B82F6', 'secondary': '#06B6D4', 'success': '#22C55E',
    'danger': '#EF4444', 'warning': '#F59E0B', 'purple': '#8B5CF6', 'muted': '#94A3B8'
}
PLOTLY_TEMPLATE = 'plotly_dark'

# ==========================================
# 4. HELPER FUNCTIONS (SIMPLIFIED)
# ==========================================
def section_divider(title, number=None):
    num_html = f'<span class="section-number">{number}</span>' if number else ''
    st.markdown(f"""
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-title">{num_html}{title}</div>
        <div class="section-divider-line"></div>
    </div>
    """, unsafe_allow_html=True)

def chart_header(title, description):
    st.markdown(f'<div class="chart-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chart-description">{description}</div>', unsafe_allow_html=True)

def insight_box(text):
    st.markdown(f'<div class="insight-box"><strong>💡 Insight</strong>{text}</div>', unsafe_allow_html=True)

def dark_layout(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E2E8F0', family='Inter', size=12),
        margin=dict(t=20, b=20, l=0, r=0)
    )
    return fig

def data_quality_panel(df):
    if len(df) == 0: return
    
    missing = df.isnull().sum().sum()
    total_cells = df.shape[0] * df.shape[1]
    missing_pct = (missing / total_cells * 100) if total_cells > 0 else 0
    
    date_min = str(df['Date_Parsed'].min())[:10] if 'Date_Parsed' in df.columns else 'N/A'
    date_max = str(df['Date_Parsed'].max())[:10] if 'Date_Parsed' in df.columns else 'N/A'
    
    # Semester detail dengan badge SMT 4
    if 'Semester' in df.columns and len(df) > 0:
        try:
            sem_list = sorted([int(s) for s in df['Semester'].dropna().unique().tolist()])
            sem_display = ', '.join([str(s) for s in sem_list])
            sem_count = len(sem_list)
            has_4 = 4 in sem_list
            badge = '<span class="semester-badge included">✓ SMT 4 Included</span>' if has_4 else '<span class="semester-badge missing">⚠ SMT 4 Missing</span>'
            sem_value = f"{sem_count} ({sem_display})"
        except:
            sem_count = df['Semester'].nunique()
            sem_value = str(sem_count)
            badge = ''
    else:
        sem_value = '0'
        badge = ''
    
    prodi_count = df['Prodi'].nunique() if 'Prodi' in df.columns else 0
    
    st.markdown(f"""
    <div class="data-quality-panel">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <div style="font-size: 22px;">📊</div>
            <div>
                <div style="font-size: 16px; font-weight: 600; color: #F8FAFC;">Data Quality Overview</div>
                <div style="font-size: 12px; color: #94A3B8;">Ringkasan kualitas dataset</div>
            </div>
        </div>
        <div class="dq-grid">
            <div class="dq-item">
                <div class="dq-label">Total Records</div>
                <div class="dq-value">{len(df):,}</div>
            </div>
            <div class="dq-item">
                <div class="dq-label">Missing Values</div>
                <div class="dq-value">{missing} ({missing_pct:.2f}%)</div>
            </div>
            <div class="dq-item">
                <div class="dq-label">Program Studi</div>
                <div class="dq-value">{prodi_count}</div>
            </div>
            <div class="dq-item">
                <div class="dq-label">Semester</div>
                <div class="dq-value" style="font-size: 14px;">{sem_value}</div>
                {badge}
            </div>
            <div class="dq-item">
                <div class="dq-label">Variables</div>
                <div class="dq-value">{len(df.columns)}</div>
            </div>
            <div class="dq-item">
                <div class="dq-label">Date Range</div>
                <div class="dq-value" style="font-size: 13px;">{date_min} → {date_max}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 5. LOAD DATA (LOGIKA TIDAK BERUBAH)
# ==========================================
@st.cache_data
def load_data():
    df = pd.read_csv('Data Mentah.csv', sep=';')
    df.columns = [
        'Timestamp', 'Prodi', 'Semester', 'Jenis_AI', 'Frekuensi_Penggunaan',
        'Tujuan_Penggunaan', 'Kesulitan_Tanpa_AI', 'Jam_per_Hari',
        'Porsi_Tugas_AI', 'Frekuensi_Info_Salah', 'Peningkatan_Nilai',
        'Tingkat_Copy_Paste', 'Skor_Efektivitas'
    ]
    df['Is_Ketergantungan_Tinggi'] = np.where(df['Porsi_Tugas_AI'] > 5, 'Tinggi (>5 Tugas)', 'Rendah (<=5 Tugas)')
    try:
        df['Date_Parsed'] = pd.to_datetime(df['Timestamp'], errors='coerce').dt.date
    except:
        df['Date_Parsed'] = df['Timestamp']
    return df

df_raw = load_data()

# ==========================================
# 6. SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 20px 0;">
        <div style="font-size: 20px; font-weight: 700; background: linear-gradient(135deg, #3B82F6, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            🎓 AI Learning Impact
        </div>
        <div style="font-size: 12px; color: #94A3B8; margin-top: 4px;">Enterprise Analytics Dashboard</div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📁 Filter Dataset", expanded=True):
        prodi_list = df_raw['Prodi'].unique().tolist()
        filter_prodi = st.multiselect("Program Studi", options=prodi_list, default=prodi_list)
        semester_list = sorted(df_raw['Semester'].unique().tolist())
        filter_semester = st.multiselect("Semester", options=semester_list, default=semester_list)
    
    with st.expander("🔮 Profil Simulator"):
        sim_tugas = st.slider("Porsi Bantuan AI Anda:", 0, 10, 6)
        if sim_tugas > 5:
            st.error("⚠️ Risiko Ketergantungan Tinggi")
        else:
            st.success("✅ Ketergantungan Aman")
    
    with st.expander("ℹ️ Tentang Dashboard"):
        st.markdown("""
        <div style="font-size: 13px; color: #CBD5E1; line-height: 1.6;">
            Dashboard ini menganalisis dampak <strong>Artificial Intelligence</strong> 
            terhadap efektivitas belajar mahasiswa dengan pendekatan <em>data-driven analytics</em>.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 40px; padding-top: 20px; border-top: 1px solid #334155;'>", unsafe_allow_html=True)
    st.caption("👨‍💻 **Developer:** Ahmad Rizza Pahlevi")
    st.caption("🏢 UIN K.H. Abdurrahman Wahid")
    st.caption("📅 Juni 2026")

# Apply filter
if filter_prodi and filter_semester:
    df = df_raw[(df_raw['Prodi'].isin(filter_prodi)) & (df_raw['Semester'].isin(filter_semester))]
else:
    df = df_raw

# ==========================================
# 7. HERO SECTION
# ==========================================
st.markdown(f"""
<div class="hero-box">
    <div class="hero-title">AI Learning Impact Analytics</div>
    <div class="hero-subtitle">
        Memahami pola, dampak, dan probabilitas penggunaan <strong>Artificial Intelligence</strong> 
        dalam ekosistem akademik melalui pendekatan analitik berbasis data dan simulasi Monte Carlo.
    </div>
    <div>
        <span class="meta-chip">📅 Update: Juni 2026</span>
        <span class="meta-chip">👨‍💻 Ahmad Rizza Pahlevi</span>
        <span class="meta-chip">🏢 UIN K.H. Abdurrahman Wahid</span>
        <span class="meta-chip">📊 {len(df)} Responden Aktif</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 8. KPI CARDS
# ==========================================
k1, k2, k3, k4 = st.columns(4)
avg_jam = df['Jam_per_Hari'].mean() if len(df) > 0 else 0
avg_tugas = df['Porsi_Tugas_AI'].mean() if len(df) > 0 else 0
avg_skor = df['Skor_Efektivitas'].mean() if len(df) > 0 else 0

with k1: st.metric("Total Sampel", f"{len(df)}", "Data Terfilter")
with k2: st.metric("Durasi Rata-rata", f"{avg_jam:.1f} Jam", "-0.2 vs Nasional", delta_color="inverse")
with k3: st.metric("Bantuan Tugas", f"{avg_tugas:.1f}/10", "Ketergantungan", delta_color="off")
with k4: st.metric("Skor Efektivitas", f"{avg_skor:.2f}/5", "Excellent" if avg_skor > 3.5 else "Moderate")

# ==========================================
# 9. DATA QUALITY PANEL
# ==========================================
data_quality_panel(df)

# ==========================================
# 10. EXECUTIVE SUMMARY
# ==========================================
section_divider("Executive Summary", "01")

if len(df) > 0:
    setiap_hari_pct = len(df[df['Frekuensi_Penggunaan']=='Setiap hari'])/len(df)*100
    mean_jam = df['Jam_per_Hari'].mean()
    max_jam = df['Jam_per_Hari'].max()
    high_dep_pct = len(df[df['Is_Ketergantungan_Tinggi']=='Tinggi (>5 Tugas)'])/len(df)*100
    
    st.markdown(f"""
    <div class="executive-summary">
        Dataset merepresentasikan <strong>{len(df)} mahasiswa</strong> yang aktif menggunakan AI. 
        <strong>{setiap_hari_pct:.0f}%</strong> menggunakan AI setiap hari dengan durasi rata-rata 
        <strong>{mean_jam:.1f} jam/hari</strong> (max {max_jam} jam). 
        Ketergantungan tinggi mencapai <strong>{high_dep_pct:.0f}%</strong>, mengindikasikan perlunya intervensi edukatif.
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("Tidak ada data yang sesuai dengan filter.")

# ==========================================
# 11. TAB NAVIGATION
# ==========================================
section_divider("Modul Analitik", "02")
tab1, tab2, tab3 = st.tabs([
    "📊 02 • Descriptive Analytics", 
    "🔗 03 • Correlation Analysis", 
    "🎲 04 • Monte Carlo"
])

# ==========================================
# TAB 1: DESCRIPTIVE
# ==========================================
with tab1:
    with st.container(border=True):
        chart_header("📈 Tren Frekuensi Penggunaan AI", "Distribusi frekuensi penggunaan AI.")
        trend_data = df['Frekuensi_Penggunaan'].value_counts().reset_index()
        trend_data.columns = ['Frekuensi', 'Jumlah']
        fig = px.bar(trend_data, x='Frekuensi', y='Jumlah', text='Jumlah', color='Frekuensi',
            color_discrete_sequence=[SOFT_COLORS['primary'], SOFT_COLORS['secondary'], SOFT_COLORS['purple'], SOFT_COLORS['muted']],
            template=PLOTLY_TEMPLATE)
        fig.update_traces(textposition='outside', hovertemplate='<b>%{x}</b><br>Jumlah: %{y}<extra></extra>')
        fig.update_layout(height=380, showlegend=False)
        st.plotly_chart(dark_layout(fig), use_container_width=True)
        if len(trend_data) > 0:
            top = trend_data.iloc[0]
            insight_box(f"Mayoritas ({top['Jumlah']} orang) menggunakan AI <strong>{top['Frekuensi']}</strong>.")

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            chart_header("🍩 Distribusi Ketergantungan", "Proporsi ketergantungan tinggi vs rendah.")
            fig = px.pie(df, names='Is_Ketergantungan_Tinggi', hole=0.55,
                color='Is_Ketergantungan_Tinggi',
                color_discrete_map={'Tinggi (>5 Tugas)': SOFT_COLORS['danger'], 'Rendah (<=5 Tugas)': SOFT_COLORS['secondary']},
                template=PLOTLY_TEMPLATE)
            fig.update_traces(textinfo='percent+label', hoverinfo='label+percent+value')
            fig.update_layout(height=380, showlegend=False)
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            high_pct = len(df[df['Is_Ketergantungan_Tinggi']=='Tinggi (>5 Tugas)'])/len(df)*100 if len(df) > 0 else 0
            insight_box(f"<strong>{high_pct:.1f}%</strong> responden memiliki ketergantungan tinggi (>5 tugas).")

    with col2:
        with st.container(border=True):
            chart_header("📊 Distribusi Porsi Tugas AI", "Histogram jumlah tugas yang dibantu AI.")
            fig = px.histogram(df, x='Porsi_Tugas_AI', text_auto=True,
                color_discrete_sequence=[SOFT_COLORS['primary']], template=PLOTLY_TEMPLATE)
            fig.update_traces(hovertemplate='<b>Porsi:</b> %{x}<br><b>Jumlah:</b> %{y}<extra></extra>')
            fig.update_layout(height=380, xaxis_title="Jumlah Tugas (0-10)", yaxis_title="Jumlah Mahasiswa")
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            insight_box(f"Rata-rata mahasiswa menggunakan AI untuk <strong>{avg_tugas:.1f} tugas</strong>.")

    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            chart_header("⏳ Histogram Durasi Harian", "Distribusi durasi penggunaan AI per hari.")
            fig = px.histogram(df, x='Jam_per_Hari', nbins=8, marginal="box",
                color_discrete_sequence=[SOFT_COLORS['secondary']], template=PLOTLY_TEMPLATE)
            fig.update_traces(hovertemplate='<b>Durasi:</b> %{x} jam<br><b>Frekuensi:</b> %{y}<extra></extra>')
            fig.update_layout(height=380)
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            insight_box(f"Durasi rata-rata <strong>{mean_jam:.1f} jam/hari</strong>.")

    with col4:
        with st.container(border=True):
            chart_header("⭐ Distribusi Skor Efektivitas", "Persepsi efektivitas AI dalam belajar.")
            fig = px.histogram(df, x='Skor_Efektivitas', text_auto=True,
                color_discrete_sequence=[SOFT_COLORS['success']], template=PLOTLY_TEMPLATE)
            fig.update_traces(hovertemplate='<b>Skor:</b> %{x}/5<br><b>Jumlah:</b> %{y}<extra></extra>')
            fig.update_layout(height=380, xaxis_title="Skor Efektivitas (1-5)")
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            insight_box(f"Skor efektivitas rata-rata <strong>{avg_skor:.2f}/5</strong>.")

    with st.container(border=True):
        chart_header("📈 Persepsi Peningkatan Nilai", "Distribusi persepsi peningkatan nilai akademik.")
        fig = px.histogram(df, x='Peningkatan_Nilai', text_auto=True, color='Peningkatan_Nilai',
            color_discrete_sequence=[SOFT_COLORS['success'], SOFT_COLORS['warning'], SOFT_COLORS['muted']],
            template=PLOTLY_TEMPLATE)
        fig.update_traces(hovertemplate='<b>Persepsi:</b> %{x}<br><b>Jumlah:</b> %{y}<extra></extra>')
        fig.update_layout(height=380, xaxis_title="Persepsi Nilai", showlegend=False)
        st.plotly_chart(dark_layout(fig), use_container_width=True)
        insight_box("Sebagian besar mahasiswa merasa AI berkontribusi pada peningkatan nilai.")

# ==========================================
# TAB 2: CORRELATION
# ==========================================
with tab2:
    col5, col6 = st.columns(2)
    with col5:
        with st.container(border=True):
            chart_header("⚠️ Probabilitas Kesulitan Tanpa AI", "Analisis kondisional kesulitan belajar tanpa AI.")
            prob_df = pd.crosstab(df['Is_Ketergantungan_Tinggi'], df['Kesulitan_Tanpa_AI'], normalize='index') * 100
            prob_df = prob_df.reset_index().melt(id_vars='Is_Ketergantungan_Tinggi', var_name='Kesulitan', value_name='Persentase')
            fig = px.bar(prob_df, x='Is_Ketergantungan_Tinggi', y='Persentase', color='Kesulitan',
                barmode='stack', text_auto='.1f',
                color_discrete_map={'Ya': SOFT_COLORS['danger'], 'Tidak': SOFT_COLORS['secondary']},
                template=PLOTLY_TEMPLATE)
            fig.update_layout(height=400)
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            insight_box("Ketergantungan tinggi meningkatkan risiko kesulitan belajar mandiri.")

    with col6:
        with st.container(border=True):
            chart_header("🔗 Heatmap Korelasi (RdBu)", "Matriks korelasi dengan skema diverging.")
            corr_matrix = df[['Jam_per_Hari', 'Porsi_Tugas_AI', 'Tingkat_Copy_Paste', 'Skor_Efektivitas']].corr()
            fig = px.imshow(corr_matrix, text_auto=".3f", aspect="auto",
                color_continuous_scale="RdBu", origin="lower", zmin=-1, zmax=1, template=PLOTLY_TEMPLATE)
            fig.update_traces(hovertemplate='<b>%{x}</b> vs <b>%{y}</b><br>r = %{z:.3f}<extra></extra>')
            fig.update_layout(height=400)
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            
            try:
                corr_val = corr_matrix.loc['Porsi_Tugas_AI', 'Skor_Efektivitas']
            except:
                corr_val = 0.0
            
            if corr_val > 0.5: interp_class, interp_text = "strong-pos", "Kuat Positif"
            elif corr_val < -0.5: interp_class, interp_text = "weak-neg", "Kuat Negatif"
            else: interp_class, interp_text = "neutral", "Lemah"
            
            st.markdown(f'<div class="heatmap-interp {interp_class}"><span>Korelasi: {corr_val:.2f}</span><span>•</span><span>{interp_text}</span></div>', unsafe_allow_html=True)
            insight_box(f"Korelasi Porsi AI & Efektivitas <strong>r = {corr_val:.2f}</strong> (lemah).")

    col7, col8 = st.columns(2)
    with col7:
        with st.container(border=True):
            chart_header("📉 Efektivitas vs Porsi AI", "Scatter plot dengan trendline linear.")
            z = np.polyfit(df['Porsi_Tugas_AI'], df['Skor_Efektivitas'], 1)
            p = np.poly1d(z)
            df_sorted = df.sort_values('Porsi_Tugas_AI')
            fig = px.scatter(df, x='Porsi_Tugas_AI', y='Skor_Efektivitas', opacity=0.8, template=PLOTLY_TEMPLATE)
            fig.update_traces(marker=dict(size=12, color=SOFT_COLORS['secondary']),
                hovertemplate='<b>Porsi:</b> %{x}<br><b>Skor:</b> %{y:.2f}<extra></extra>')
            fig.add_trace(go.Scatter(x=df_sorted['Porsi_Tugas_AI'], y=p(df_sorted['Porsi_Tugas_AI']),
                mode='lines', name='Trendline', line=dict(color=SOFT_COLORS['danger'], width=3)))
            r_squared = np.corrcoef(df['Porsi_Tugas_AI'], df['Skor_Efektivitas'])[0, 1] ** 2
            fig.update_layout(height=380, showlegend=False,
                annotations=[dict(x=0.02, y=0.98, xref='paper', yref='paper',
                    text=f"y = {z[0]:.3f}x + {z[1]:.3f}<br>R² = {r_squared:.3f}",
                    showarrow=False, font=dict(size=11, color='#E2E8F0'),
                    bgcolor='rgba(30, 41, 59, 0.8)', bordercolor='rgba(59, 130, 246, 0.3)',
                    borderwidth=1, borderpad=8)])
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            insight_box("Trendline lemah - efektivitas bergantung pada cara penggunaan, bukan frekuensi.")

    with col8:
        with st.container(border=True):
            chart_header("📦 Boxplot Efektivitas per Porsi", "Distribusi skor per tingkat porsi AI.")
            fig = px.box(df, x='Porsi_Tugas_AI', y='Skor_Efektivitas', color='Porsi_Tugas_AI',
                color_discrete_sequence=[SOFT_COLORS['primary'], SOFT_COLORS['secondary'], SOFT_COLORS['purple']],
                template=PLOTLY_TEMPLATE)
            fig.update_traces(hovertemplate='<b>Porsi:</b> %{x}<br><b>Skor:</b> %{y:.2f}<extra></extra>')
            fig.update_layout(height=380, xaxis_title="Porsi Tugas (0-10)", showlegend=False)
            st.plotly_chart(dark_layout(fig), use_container_width=True)
            insight_box("Variasi besar antar kategori - faktor individu berpengaruh kuat.")

    with st.container(border=True):
        chart_header("📑 Rata-rata Copy-Paste per Porsi", "Tingkat ketergantungan pasif terhadap output AI.")
        cp = df.groupby('Porsi_Tugas_AI')['Tingkat_Copy_Paste'].mean().reset_index()
        fig = px.bar(cp, x='Porsi_Tugas_AI', y='Tingkat_Copy_Paste', text_auto='.2f',
            color='Tingkat_Copy_Paste', color_continuous_scale="Purples", template=PLOTLY_TEMPLATE)
        fig.update_traces(textposition='outside', hovertemplate='<b>Porsi:</b> %{x}<br><b>Copy-Paste:</b> %{y:.2f}<extra></extra>')
        fig.update_layout(height=380, xaxis_title="Porsi AI (0-10)", yaxis_title="Skor Copy-Paste (1-5)")
        st.plotly_chart(dark_layout(fig), use_container_width=True)
        insight_box("Korelasi positif - risiko plagiarisme pada pengguna berat AI.")

# ==========================================
# TAB 3: MONTE CARLO
# ==========================================
with tab3:
    with st.container(border=True):
        chart_header("🎲 Monte Carlo Simulation",
            "Proyeksi stokastik untuk prediksi stabilitas skor efektivitas melalui ribuan iterasi acak.")
        
        st.markdown('<div class="mc-status"><span class="mc-status-dot"></span> Stochastic Engine Ready</div>', unsafe_allow_html=True)
        
        mc_c1, mc_c2 = st.columns([1, 3])
        with mc_c1:
            iterations = st.number_input("Jumlah Iterasi", min_value=1000, max_value=50000, value=10000, step=1000)
            run_mc = st.button("🚀 Jalankan Simulasi", use_container_width=True)
        
        with mc_c2:
            if run_mc and len(df) > 0:
                with st.spinner(f"Memproses {iterations} iterasi..."):
                    p_dist = df['Porsi_Tugas_AI'].value_counts(normalize=True).sort_index()
                    cats, weights = p_dist.index.values, p_dist.values
                    stats = df.groupby('Porsi_Tugas_AI')['Skor_Efektivitas'].agg(['mean', 'std']).fillna(df['Skor_Efektivitas'].std())
                    hasil = []
                    for _ in range(iterations):
                        sim_tugas = np.random.choice(cats, size=100, p=weights)
                        skor = [np.clip(np.random.normal(loc=stats.loc[p, 'mean'], scale=stats.loc[p, 'std']), 1, 5) for p in sim_tugas]
                        hasil.append(np.mean(skor))
                    mean_mc = np.mean(hasil)
                    ci_low, ci_high = np.percentile(hasil, 2.5), np.percentile(hasil, 97.5)
                    running_mean = np.cumsum(hasil) / np.arange(1, iterations+1)
                
                col_m1, col_m2, col_m3 = st.columns(3)
                with col_m1: st.metric("Target Iterasi", f"{iterations:,}")
                with col_m2: st.metric("Mean Ekspektasi", f"{mean_mc:.3f}")
                with col_m3: st.metric("95% Confidence Interval", f"{ci_low:.2f} - {ci_high:.2f}")
                
                fig = px.line(x=np.arange(1, iterations+1), y=running_mean, template=PLOTLY_TEMPLATE)
                fig.update_traces(line=dict(color=SOFT_COLORS['primary'], width=2.5),
                    hovertemplate='<b>Iterasi:</b> %{x}<br><b>Mean:</b> %{y:.3f}<extra></extra>')
                fig.add_hline(y=mean_mc, line_dash="dash", line_color=SOFT_COLORS['danger'],
                    annotation_text="Titik Konvergen", annotation_font_color=SOFT_COLORS['danger'])
                fig.update_layout(title="Kurva Konvergensi", xaxis_title="Iterasi", yaxis_title="Running Mean", height=380)
                st.plotly_chart(dark_layout(fig), use_container_width=True)
                
                fig = px.histogram(x=hasil, nbins=50, color_discrete_sequence=[SOFT_COLORS['purple']], template=PLOTLY_TEMPLATE)
                fig.update_traces(hovertemplate='<b>Skor:</b> %{x:.3f}<br><b>Frekuensi:</b> %{y}<extra></extra>')
                fig.update_layout(title="Distribusi Hasil Simulasi", xaxis_title="Skor Efektivitas", yaxis_title="Frekuensi", height=380)
                st.plotly_chart(dark_layout(fig), use_container_width=True)
                
                insight_box(f"Setelah {iterations:,} iterasi, konvergensi stabil di {mean_mc:.3f} dengan 95% CI [{ci_low:.2f}, {ci_high:.2f}].")
            elif run_mc and len(df) == 0:
                st.warning("Tidak ada data untuk disimulasikan.")

# ==========================================
# 12. AI INSIGHT PANEL
# ==========================================
section_divider("AI Insights & Recommendations", "05")

with st.container(border=True):
    chart_header("🤖 AI-Generated Insights", "Analisis otomatis berdasarkan pola data terkini")
    
    if len(df) > 0:
        setiap_hari_pct = len(df[df['Frekuensi_Penggunaan']=='Setiap hari'])/len(df)*100
        mean_jam = df['Jam_per_Hari'].mean()
        try:
            corr_val = df[['Porsi_Tugas_AI', 'Skor_Efektivitas']].corr().loc['Porsi_Tugas_AI', 'Skor_Efektivitas']
        except:
            corr_val = 0.0
        
        st.markdown(f"""
        <div class="ai-insight-panel">
            <strong>Analisis Pola Penggunaan AI:</strong><br>
            Mahasiswa dengan penggunaan AI tinggi cenderung mengalami ketergantungan lebih besar, 
            namun peningkatan efektivitas belajar hanya menunjukkan korelasi lemah (r = {corr_val:.2f}). 
            {setiap_hari_pct:.0f}% mahasiswa menggunakan AI setiap hari ({mean_jam:.1f} jam/hari). 
            <strong>Kualitas penggunaan AI lebih penting daripada kuantitas.</strong>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 13. STRATEGIC INSIGHTS
# ==========================================
section_divider("Strategic Insights", "06")

with st.container(border=True):
    chart_header("💡 Strategic Insights", "Temuan kunci untuk kebijakan akademik.")
    
    if len(df) > 0:
        setiap_hari_pct = len(df[df['Frekuensi_Penggunaan']=='Setiap hari'])/len(df)*100
        mean_jam = df['Jam_per_Hari'].mean()
        max_jam = df['Jam_per_Hari'].max()
        try:
            corr_val = df[['Porsi_Tugas_AI', 'Skor_Efektivitas']].corr().loc['Porsi_Tugas_AI', 'Skor_Efektivitas']
        except:
            corr_val = 0.0
        
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 14px;">
            <div class="insight-box" style="margin-top: 0;"><strong>🎯 Adopsi Tinggi:</strong> {setiap_hari_pct:.0f}% menggunakan AI setiap hari.</div>
            <div class="insight-box" style="margin-top: 0;"><strong>⏱️ Intensitas:</strong> Rata-rata {mean_jam:.1f} jam, max {max_jam} jam/hari.</div>
            <div class="insight-box" style="margin-top: 0;"><strong>⚠️ Risiko Kognitif:</strong> Ketergantungan tinggi meningkatkan kesulitan belajar mandiri.</div>
            <div class="insight-box" style="margin-top: 0;"><strong>📊 Korelasi Lemah:</strong> r = {corr_val:.2f}, bergantung pada AI tidak menjamin pemahaman.</div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 14. FOOTER
# ==========================================
st.markdown("""
<div class="dashboard-footer">
    <div style="font-size: 16px; font-weight: 600; color: #F8FAFC; margin-bottom: 8px;">🎓 AI Learning Impact Analytics</div>
    <div>Dashboard analitik untuk memahami dampak <strong>Artificial Intelligence</strong> dalam ekosistem akademik melalui pendekatan <em>data-driven analytics</em> dan simulasi Monte Carlo.</div>
    <div class="footer-meta">
        <div>
            <strong>Developer:</strong> Ahmad Rizza Pahlevi<br>
            <strong>Institusi:</strong> UIN K.H. Abdurrahman Wahid
        </div>
        <div>
            <strong>Tech Stack:</strong> Python • Streamlit • Plotly • Pandas<br>
            <strong>Version:</strong> 2.1 Lightweight • Juni 2026
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
