import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# StabilityLog - 화장품 안정성 시험 트래커
# 기존 index.html(순수 HTML/CSS/JS, localStorage 기반)의 내용을 그대로
# 문자열로 포함해 별도 파일 의존성 없이 단일 app.py로 배포합니다.
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="StabilityLog - 화장품 안정성 시험 트래커",
    page_icon="🧪",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { height: 0; visibility: hidden; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StabilityLog - 화장품 안정성 시험 트래커</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css" />
<style>
  :root {
    --blue-900: #1f4e79;
    --blue-700: #2e6da4;
    --blue-500: #6fa8d8;
    --blue-100: #dcebf7;
    --blue-50: #fbf7f1;
    --gray-900: #3a3630;
    --gray-600: #8a8378;
    --gray-200: #ede7dc;
    --white: #ffffff;
    --warn: #e8593b;
    --warn-bg: #fdeae3;
    --ok: var(--blue-700);
    --ok-bg: var(--blue-100);
    --radius: 20px;
    --shadow: 0 6px 18px rgba(31, 78, 121, 0.14);
  }

  * { box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  /* splash screen */
  .splash {
    position: fixed;
    inset: 0;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 18px;
    background: linear-gradient(135deg, var(--blue-900), var(--blue-700));
    transition: opacity 0.45s ease;
  }
  .splash.hide {
    opacity: 0;
    pointer-events: none;
  }
  .splash-logo {
    width: 60px;
    height: 60px;
    animation: splash-pulse 1.1s ease-in-out infinite;
  }
  .splash-title {
    font-family: 'Space Grotesk', 'Pretendard', 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: 20px;
    color: #fff;
    letter-spacing: 0.02em;
  }
  .splash-spinner {
    width: 26px;
    height: 26px;
    border: 3px solid rgba(255, 255, 255, 0.25);
    border-top-color: #fff;
    border-radius: 50%;
    animation: splash-spin 0.8s linear infinite;
  }
  @keyframes splash-pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.08); opacity: 0.85; }
  }
  @keyframes splash-spin {
    to { transform: rotate(360deg); }
  }

  body {
    margin: 0;
    font-family: 'Pretendard', 'Noto Sans KR', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: linear-gradient(180deg, var(--blue-100) 0%, var(--blue-50) 220px);
    color: var(--gray-900);
  }

  /* utility bar */
  .utility-bar {
    display: flex;
    justify-content: flex-end;
    gap: 16px;
    background: var(--gray-200);
    padding: 6px 20px;
    font-size: 11px;
  }
  .utility-bar a {
    color: var(--gray-600);
    text-decoration: none;
    padding-left: 16px;
    border-left: 1px solid rgba(138, 131, 120, 0.4);
  }
  .utility-bar a:first-child { border-left: none; padding-left: 0; }
  .utility-bar a:hover { color: var(--blue-900); }

  /* main nav */
  header {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(6px);
    border-bottom: 1px solid var(--gray-200);
    position: sticky;
    top: 0;
    z-index: 10;
  }

  .nav-inner {
    max-width: 1100px;
    margin: 0 auto;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    gap: 24px;
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: 'Space Grotesk', 'Pretendard', 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: 18px;
    color: var(--blue-900);
    flex-shrink: 0;
  }

  .logo-mark {
    width: 34px;
    height: 34px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .logo-mark svg {
    width: 28px;
    height: 28px;
    filter: drop-shadow(0 3px 6px rgba(31, 78, 121, 0.25));
  }

  .nav-links {
    display: flex;
    align-items: center;
    gap: 28px;
    flex: 1;
    justify-content: center;
  }
  .nav-links a {
    font-size: 14px;
    font-weight: 600;
    color: var(--gray-900);
    text-decoration: none;
    padding: 4px 2px;
    border-bottom: 2px solid transparent;
    transition: color 0.15s ease, border-color 0.15s ease;
  }
  .nav-links a:hover { color: var(--blue-900); border-color: var(--blue-500); }

  .nav-icons {
    display: flex;
    align-items: center;
    gap: 4px;
    flex-shrink: 0;
  }
  .icon-btn {
    width: 36px;
    height: 36px;
    border: none;
    border-radius: 50%;
    background: transparent;
    color: var(--gray-900);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background 0.15s ease, color 0.15s ease;
  }
  .icon-btn svg { width: 19px; height: 19px; }
  .icon-btn:hover { background: var(--blue-100); color: var(--blue-900); }
  .icon-btn.active { background: var(--blue-900); color: #fff; }

  .nav-search {
    max-height: 0;
    overflow: hidden;
    border-top: 1px solid transparent;
    transition: max-height 0.2s ease, border-color 0.2s ease;
  }
  .nav-search.open {
    max-height: 60px;
    border-top: 1px solid var(--gray-200);
  }
  .nav-search input {
    display: block;
    width: 100%;
    max-width: 1100px;
    margin: 0 auto;
    padding: 14px 20px;
    border: none;
    background: transparent;
    font-family: inherit;
    font-size: 14px;
    color: var(--gray-900);
  }
  .nav-search input:focus { outline: none; }

  /* promo bar */
  .promo-bar {
    background: var(--blue-50);
    text-align: center;
    padding: 10px 20px;
    font-size: 13px;
    color: var(--gray-900);
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }
  .promo-link {
    color: var(--blue-900);
    font-weight: 700;
    text-decoration: underline;
  }

  /* hero */
  .hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, var(--blue-900), var(--blue-700));
    display: flex;
    align-items: flex-end;
  }
  .hero-mark {
    position: absolute;
    right: -60px;
    top: 50%;
    transform: translateY(-50%);
    width: 380px;
    height: 380px;
    opacity: 0.12;
    pointer-events: none;
  }
  .hero-mark svg { width: 100%; height: 100%; }
  .hero-inner {
    position: relative;
    z-index: 1;
    max-width: 1100px;
    margin: 0 auto;
    width: 100%;
    padding: 56px 20px 44px;
  }
  .hero-eyebrow {
    font-size: 12px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--blue-100);
    font-weight: 700;
    margin-bottom: 12px;
  }
  .hero h1 {
    font-family: 'Space Grotesk', 'Pretendard', 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: clamp(26px, 4.5vw, 44px);
    line-height: 1.3;
    color: #fff;
    margin: 0 0 24px;
  }
  .hero-cta {
    background: #fff;
    color: var(--blue-900);
    border: none;
    padding: 14px 26px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  .hero-cta:hover { transform: translateY(-2px); }

  main {
    max-width: 960px;
    margin: 0 auto;
    padding: 20px;
    padding-bottom: 100px;
  }

  section {
    margin-bottom: 28px;
    scroll-margin-top: 84px;
  }

  h2 {
    font-family: 'Space Grotesk', 'Pretendard', 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: 16px;
    color: var(--blue-900);
    margin: 0 0 12px 2px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  /* summary cards */
  .summary-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
  }

  .summary-card {
    background: var(--white);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 16px;
    text-align: left;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  .summary-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 22px rgba(31, 78, 121, 0.2);
  }

  .summary-card .value {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 28px;
    color: var(--blue-900);
    line-height: 1.2;
  }

  .summary-card.warn .value { color: var(--warn); }
  .summary-card.ok .value { color: var(--ok); }

  .summary-card .label {
    font-size: 12px;
    color: var(--gray-600);
    margin-top: 4px;
  }

  /* schedule list */
  .card-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .item-card {
    background: var(--white);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 14px 16px;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 12px;
    cursor: pointer;
    border: 2px solid transparent;
    transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
  }
  .item-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(31, 78, 121, 0.2);
    border-color: var(--blue-100);
  }

  .item-main {
    display: flex;
    flex-direction: column;
    gap: 4px;
    min-width: 0;
    flex: 1;
  }

  .item-name {
    font-weight: 600;
    font-size: 14px;
    color: var(--gray-900);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .item-meta {
    font-size: 12px;
    color: var(--gray-600);
  }

  .item-reason {
    font-size: 12px;
    color: var(--warn);
    margin-top: 4px;
    line-height: 1.4;
  }

  .item-side {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 8px;
  }

  .badge {
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 999px;
    white-space: nowrap;
  }

  .badge.due-today { background: var(--blue-900); color: var(--white); }
  .badge.due-soon { background: var(--blue-100); color: var(--blue-700); }
  .badge.status-ok { background: var(--ok-bg); color: var(--ok); }
  .badge.status-warn { background: var(--warn-bg); color: var(--warn); }

  .btn-observe {
    border: 1.5px solid var(--blue-500);
    background: var(--white);
    color: var(--blue-700);
    font-size: 12px;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 999px;
    cursor: pointer;
    white-space: nowrap;
    transition: transform 0.1s ease, background 0.15s ease;
  }
  .btn-observe:hover { background: var(--blue-100); transform: scale(1.04); }

  .empty-state {
    background: var(--white);
    border-radius: var(--radius);
    padding: 24px;
    text-align: center;
    color: var(--gray-600);
    font-size: 13px;
    box-shadow: var(--shadow);
  }

  /* floating action button */
  .fab {
    position: fixed;
    right: 20px;
    bottom: 24px;
    background: linear-gradient(135deg, var(--blue-700), var(--blue-900));
    color: white;
    border: none;
    border-radius: 999px;
    padding: 14px 22px;
    font-family: 'Space Grotesk', 'Pretendard', 'Noto Sans KR', sans-serif;
    font-size: 15px;
    font-weight: 700;
    box-shadow: 0 8px 20px rgba(31, 78, 121, 0.35);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  .fab:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 10px 24px rgba(31, 78, 121, 0.45);
  }

  /* modal */
  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(31, 78, 121, 0.35);
    display: none;
    align-items: flex-end;
    justify-content: center;
    z-index: 100;
  }
  .modal-overlay.open { display: flex; }

  .modal {
    background: var(--white);
    width: 100%;
    max-width: 520px;
    border-radius: 24px 24px 0 0;
    padding: 22px 20px calc(22px + env(safe-area-inset-bottom));
    max-height: 90vh;
    overflow-y: auto;
  }

  @media (min-width: 640px) {
    .modal-overlay { align-items: center; }
    .modal { border-radius: 24px; }
  }

  .modal h3 {
    font-family: 'Space Grotesk', 'Pretendard', 'Noto Sans KR', sans-serif;
    font-weight: 700;
    margin: 0 0 4px;
    color: var(--blue-900);
    font-size: 19px;
  }

  .modal .modal-sub {
    font-size: 12px;
    color: var(--gray-600);
    margin-bottom: 16px;
  }

  .field {
    margin-bottom: 14px;
  }

  .field-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .field label {
    display: block;
    font-size: 12px;
    font-weight: 600;
    color: var(--gray-600);
    margin-bottom: 6px;
  }

  .field input, .field select {
    width: 100%;
    padding: 10px 12px;
    border: 1.5px solid var(--gray-200);
    border-radius: 12px;
    font-size: 14px;
    font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
    background: var(--blue-50);
    transition: border-color 0.15s ease;
  }
  .field input:focus, .field select:focus {
    outline: none;
    border-color: var(--blue-500);
  }

  .modal-actions {
    display: flex;
    gap: 10px;
    margin-top: 18px;
  }

  .btn-primary, .btn-secondary {
    flex: 1;
    padding: 12px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    transition: transform 0.1s ease, opacity 0.15s ease;
  }
  .btn-primary:active, .btn-secondary:active { transform: scale(0.97); }

  .btn-primary { background: linear-gradient(135deg, var(--blue-700), var(--blue-900)); color: white; }
  .btn-primary:hover { opacity: 0.9; }
  .btn-secondary { background: var(--gray-200); color: var(--gray-900); }
  .btn-secondary:hover { background: var(--blue-100); }

  /* detail modal */
  .ai-summary-box {
    background: var(--warn-bg);
    border: 1.5px solid #f4b8a2;
    border-radius: 16px;
    padding: 12px 14px;
    margin-bottom: 16px;
  }
  .ai-summary-box.ok {
    background: var(--ok-bg);
    border-color: var(--blue-500);
  }
  .ai-summary-box .ai-title {
    font-size: 11px;
    font-weight: 700;
    color: var(--warn);
    margin-bottom: 6px;
  }
  .ai-summary-box.ok .ai-title { color: var(--ok); }
  .ai-summary-box ul {
    margin: 0;
    padding-left: 18px;
    font-size: 13px;
    color: var(--gray-900);
  }
  .ai-summary-box p {
    margin: 0;
    font-size: 13px;
    color: var(--gray-900);
  }

  .chart-block {
    background: var(--blue-100);
    border-radius: 16px;
    padding: 12px;
    margin-bottom: 14px;
  }
  .chart-block .chart-label {
    font-size: 12px;
    font-weight: 600;
    color: var(--gray-600);
    margin-bottom: 6px;
  }
  .chart-svg {
    width: 100%;
    height: 80px;
    display: block;
  }
  .chart-empty {
    font-size: 12px;
    color: var(--gray-600);
    padding: 20px 0;
    text-align: center;
  }

  .obs-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    margin-top: 4px;
  }
  .obs-table th, .obs-table td {
    text-align: left;
    padding: 8px 6px;
    border-bottom: 1px solid var(--gray-200);
    white-space: nowrap;
  }
  .obs-table th {
    color: var(--gray-600);
    font-weight: 600;
  }
  .obs-table tr.flagged td {
    color: var(--warn);
    font-weight: 600;
  }
  .table-scroll {
    overflow-x: auto;
  }

  .photo-thumb {
    width: 28px;
    height: 28px;
    border-radius: 6px;
    object-fit: cover;
    vertical-align: middle;
  }

  @media (max-width: 700px) {
    .nav-links { display: none; }
    .hero-mark { display: none; }
    .utility-bar { font-size: 10px; gap: 10px; }
    .utility-bar a { padding-left: 10px; }
  }

  @media (max-width: 600px) {
    .summary-grid { grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .summary-card { padding: 12px 10px; }
    .summary-card .value { font-size: 20px; }
    .item-card { flex-wrap: wrap; }
    .field-row { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>

<div class="splash" id="splash">
  <svg class="splash-logo" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="StabilityLog 로고">
    <path d="M18 3 L30 8 V17 C30 25.5 24.5 31 18 33 C11.5 31 6 25.5 6 17 V8 Z" fill="#ffffff" />
    <circle cx="18" cy="17" r="6" fill="#1f4e79" />
    <g stroke="#ffffff" stroke-width="2" stroke-linecap="round">
      <line x1="18" y1="6" x2="18" y2="8.5" />
      <line x1="18" y1="25.5" x2="18" y2="28" />
      <line x1="9" y1="17" x2="11.5" y2="17" />
      <line x1="24.5" y1="17" x2="27" y2="17" />
      <line x1="12" y1="11" x2="13.7" y2="12.7" />
      <line x1="22.3" y1="21.3" x2="24" y2="23" />
      <line x1="24" y1="11" x2="22.3" y2="12.7" />
      <line x1="13.7" y1="21.3" x2="12" y2="23" />
    </g>
    <circle cx="18" cy="17" r="4" fill="#ffffff" />
  </svg>
  <div class="splash-title">StabilityLog</div>
  <div class="splash-spinner"></div>
</div>

<div class="utility-bar">
  <a href="#" id="link-guide">사용 가이드</a>
  <a href="#" id="link-export">데이터 내보내기</a>
  <a href="#" id="link-contact">문의하기</a>
</div>

<header>
  <div class="nav-inner">
    <div class="logo">
      <span class="logo-mark">
        <svg viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="StabilityLog 로고">
          <path d="M18 3 L30 8 V17 C30 25.5 24.5 31 18 33 C11.5 31 6 25.5 6 17 V8 Z" fill="#1f4e79" />
          <circle cx="18" cy="17" r="6" fill="#fbf7f1" />
          <g stroke="#f2994a" stroke-width="2" stroke-linecap="round">
            <line x1="18" y1="6" x2="18" y2="8.5" />
            <line x1="18" y1="25.5" x2="18" y2="28" />
            <line x1="9" y1="17" x2="11.5" y2="17" />
            <line x1="24.5" y1="17" x2="27" y2="17" />
            <line x1="12" y1="11" x2="13.7" y2="12.7" />
            <line x1="22.3" y1="21.3" x2="24" y2="23" />
            <line x1="24" y1="11" x2="22.3" y2="12.7" />
            <line x1="13.7" y1="21.3" x2="12" y2="23" />
          </g>
          <circle cx="18" cy="17" r="4" fill="#f2994a" />
        </svg>
      </span>
      StabilityLog
    </div>
    <nav class="nav-links">
      <a href="#section-dashboard">대시보드</a>
      <a href="#section-attention">확인 필요</a>
      <a href="#section-all">전체 시험</a>
    </nav>
    <div class="nav-icons">
      <button class="icon-btn" id="btn-search-toggle" aria-label="검색" title="검색">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7" /><line x1="21" y1="21" x2="16.65" y2="16.65" /></svg>
      </button>
      <button class="icon-btn" id="btn-today-toggle" aria-label="오늘 확인만 보기" title="오늘 확인만 보기">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2" /><line x1="16" y1="3" x2="16" y2="7" /><line x1="8" y1="3" x2="8" y2="7" /><line x1="3" y1="10" x2="21" y2="10" /><path d="M8 15l2.5 2.5L16 12" /></svg>
      </button>
      <button class="icon-btn" id="btn-flag-toggle" aria-label="이상 징후만 보기" title="이상 징후만 보기">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 3v18" /><path d="M4 4h13l-3 4 3 4H4" /></svg>
      </button>
      <button class="icon-btn" id="btn-nav-add" aria-label="새 시험 등록" title="새 시험 등록">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19" /><line x1="5" y1="12" x2="19" y2="12" /></svg>
      </button>
    </div>
  </div>
  <div class="nav-search" id="nav-search">
    <input type="text" id="search-input" placeholder="샘플명으로 검색..." />
  </div>
</header>

<div class="promo-bar">
  <span id="promo-text">이번 주 확인이 필요한 시험이 없습니다.</span>
  <a href="#section-attention" class="promo-link">바로 확인</a>
</div>

<section class="hero">
  <div class="hero-mark">
    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <ellipse cx="76" cy="16" rx="8" ry="10" fill="none" stroke="#ffffff" stroke-width="2.5" />
      <line x1="76" y1="26" x2="60" y2="50" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
      <circle cx="54" cy="60" r="2.6" fill="#ffffff" />
      <path d="M32 38 L27 82 Q27 88 33 88 L67 88 Q73 88 73 82 L68 38 Z" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" />
      <line x1="27" y1="38" x2="73" y2="38" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
      <path d="M30 62 L27.6 82 Q27.6 86 33 86 L67 86 Q72.4 86 72.4 82 L70 62 Z" fill="#ffffff" opacity="0.22" />
      <line x1="31" y1="50" x2="35" y2="50" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round" />
      <line x1="30" y1="60" x2="35" y2="60" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round" />
      <line x1="29" y1="70" x2="35" y2="70" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round" />
    </svg>
  </div>
  <div class="hero-inner">
    <div class="hero-eyebrow">화장품 안정성 시험 트래커</div>
    <h1>StabilityLog</h1>
    <button class="hero-cta" id="hero-cta-add">＋ 새 시험 등록</button>
  </div>
</section>

<main>
  <section id="section-dashboard">
    <h2>📊 진행 중인 시험 현황</h2>
    <div class="summary-grid">
      <div class="summary-card">
        <div class="value" id="stat-total">0</div>
        <div class="label">전체 진행 시험</div>
      </div>
      <div class="summary-card ok">
        <div class="value" id="stat-ok">0</div>
        <div class="label">정상</div>
      </div>
      <div class="summary-card warn">
        <div class="value" id="stat-warn">0</div>
        <div class="label">이상 징후</div>
      </div>
    </div>
  </section>

  <section id="section-attention">
    <h2>🔎 이번 주 확인 필요</h2>
    <div class="card-list" id="attention-list"></div>
  </section>

  <section id="section-all">
    <h2>🧪 전체 시험 목록</h2>
    <div class="card-list" id="all-list"></div>
  </section>
</main>

<button class="fab" id="fab-add">＋ 새 시험 등록</button>

<!-- 새 시험 등록 모달 -->
<div class="modal-overlay" id="modal-add">
  <div class="modal">
    <h3>새 안정성 시험 등록</h3>
    <div class="field">
      <label for="f-name">샘플명</label>
      <input type="text" id="f-name" placeholder="예: 크림 A 시제품 #12" />
    </div>
    <div class="field">
      <label for="f-condition">시험 조건</label>
      <select id="f-condition">
        <option>40℃ 가혹조건</option>
        <option>상온(25℃)</option>
        <option>저온(4℃)</option>
        <option>광안정성</option>
        <option>냉동-해동 반복</option>
      </select>
    </div>
    <div class="field">
      <label for="f-cycle">관찰 주기(일)</label>
      <input type="number" id="f-cycle" value="7" min="1" />
    </div>
    <div class="modal-actions">
      <button class="btn-secondary" id="btn-add-cancel">취소</button>
      <button class="btn-primary" id="btn-add-save">등록</button>
    </div>
  </div>
</div>

<!-- 관찰 결과 입력 모달 -->
<div class="modal-overlay" id="modal-observe">
  <div class="modal">
    <h3 id="observe-title">관찰 결과 입력</h3>
    <div class="modal-sub" id="observe-sub"></div>
    <div class="field-row">
      <div class="field">
        <label for="o-color">색상</label>
        <input type="text" id="o-color" placeholder="예: 아이보리색" />
      </div>
      <div class="field">
        <label for="o-smell">냄새</label>
        <input type="text" id="o-smell" placeholder="예: 이상 없음" />
      </div>
    </div>
    <div class="field-row">
      <div class="field">
        <label for="o-viscosity">점도 (cP)</label>
        <input type="number" id="o-viscosity" placeholder="예: 12000" />
      </div>
      <div class="field">
        <label for="o-ph">pH</label>
        <input type="number" step="0.1" id="o-ph" placeholder="예: 5.5" />
      </div>
    </div>
    <div class="field">
      <label for="o-separation">상 분리 여부</label>
      <select id="o-separation">
        <option value="no">없음</option>
        <option value="yes">있음</option>
      </select>
    </div>
    <div class="field">
      <label for="o-photo">사진 첨부 (선택)</label>
      <input type="file" id="o-photo" accept="image/*" />
    </div>
    <div class="modal-actions">
      <button class="btn-secondary" id="btn-observe-cancel">취소</button>
      <button class="btn-primary" id="btn-observe-save">저장</button>
    </div>
  </div>
</div>

<!-- 상세보기 모달 -->
<div class="modal-overlay" id="modal-detail">
  <div class="modal">
    <h3 id="detail-title">시험 상세</h3>
    <div class="modal-sub" id="detail-sub"></div>

    <div id="detail-ai-summary"></div>

    <div class="chart-block">
      <div class="chart-label">점도 추이 (cP)</div>
      <div id="chart-viscosity"></div>
    </div>
    <div class="chart-block">
      <div class="chart-label">pH 추이</div>
      <div id="chart-ph"></div>
    </div>

    <div class="chart-label">관찰 이력</div>
    <div class="table-scroll">
      <table class="obs-table" id="obs-table">
        <thead>
          <tr><th>일자</th><th>색상</th><th>냄새</th><th>점도</th><th>pH</th><th>분리</th><th>사진</th></tr>
        </thead>
        <tbody id="obs-tbody"></tbody>
      </table>
    </div>

    <div class="modal-actions">
      <button class="btn-secondary" id="btn-detail-close">닫기</button>
    </div>
  </div>
</div>

<!-- 사용 가이드 모달 -->
<div class="modal-overlay" id="modal-guide">
  <div class="modal">
    <h3>StabilityLog 사용 가이드</h3>
    <div class="modal-sub">화장품 안정성 시험, 이렇게 관리하세요</div>
    <ol style="padding-left: 18px; margin: 0 0 4px; font-size: 13px; line-height: 1.8; color: var(--gray-900);">
      <li><strong>새 시험 등록</strong> — 우측 상단 ➕ 또는 히어로의 "새 시험 등록" 버튼으로 샘플명·시험조건·관찰주기를 입력하세요.</li>
      <li><strong>관찰 결과 입력</strong> — "확인 필요" 목록에서 색상·냄새·점도·pH·상분리 여부를 주기적으로 기록하세요.</li>
      <li><strong>이상 징후 자동 감지</strong> — 색상 변화, 점도 20% 이상 변화, pH 0.5 이상 변화, 상분리가 감지되면 자동으로 "이상 징후"로 표시됩니다.</li>
      <li><strong>검색 · 필터</strong> — 🔍로 샘플명을 검색하고, 📅/🚩 아이콘으로 오늘 확인할 항목 또는 이상 징후만 모아볼 수 있습니다.</li>
    </ol>
    <div class="modal-actions">
      <button class="btn-primary" id="btn-guide-close">확인했어요</button>
    </div>
  </div>
</div>

<!-- 문의하기 모달 -->
<div class="modal-overlay" id="modal-contact">
  <div class="modal">
    <h3>문의하기</h3>
    <div class="modal-sub">서비스 이용 중 궁금한 점이 있으면 연락주세요</div>
    <div style="font-size: 13px; line-height: 2; color: var(--gray-900); margin-bottom: 4px;">
      <div><strong>담당자</strong> · 김민서 (StabilityLog 고객지원팀)</div>
      <div><strong>이메일</strong> · support@stabilitylog-demo.com</div>
      <div><strong>전화</strong> · 02-1234-5678 (평일 09:00–18:00)</div>
    </div>
    <div class="modal-actions">
      <button class="btn-secondary" id="btn-contact-close">닫기</button>
    </div>
  </div>
</div>

<script>
  const STORAGE_KEY = 'stabilitylog_tests_v4';
  const DAY = 24 * 60 * 60 * 1000;

  function loadTests() {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw);
    const now = Date.now();
    const seed = [
      {
        id: 1,
        name: '선크림 SPF50+ 무기자차 리뉴얼',
        condition: '광안정성',
        cycleDays: 3,
        nextDue: now - 1 * DAY,
        observations: [
          { date: now - 10 * DAY, color: '화이트', smell: '이상 없음', viscosity: 21000, pH: 7.2, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 7 * DAY, color: '화이트', smell: '이상 없음', viscosity: 21300, pH: 7.1, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 4 * DAY, color: '연한 아이보리색', smell: '약간의 유분 산패취', viscosity: 20800, pH: 6.9, separation: 'no', photo: null, flagged: true, reasons: ['색상이 "화이트"에서 "연한 아이보리색"(으)로 변했습니다.'] },
        ],
      },
      {
        id: 2,
        name: '수분크림 세라마이드 강화 시제품 #7',
        condition: '40℃ 가혹조건',
        cycleDays: 7,
        nextDue: now + 5 * DAY,
        observations: [
          { date: now - 16 * DAY, color: '아이보리색', smell: '이상 없음', viscosity: 16000, pH: 5.8, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 9 * DAY, color: '아이보리색', smell: '이상 없음', viscosity: 16250, pH: 5.7, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 2 * DAY, color: '아이보리색', smell: '이상 없음', viscosity: 16100, pH: 5.6, separation: 'no', photo: null, flagged: false, reasons: [] },
        ],
      },
      {
        id: 3,
        name: '비타민C 앰플 저자극 개선판',
        condition: '저온(4℃)',
        cycleDays: 3,
        nextDue: now,
        observations: [
          { date: now - 9 * DAY, color: '투명', smell: '이상 없음', viscosity: 320, pH: 3.6, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 6 * DAY, color: '투명', smell: '이상 없음', viscosity: 310, pH: 3.5, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 3 * DAY, color: '연한 황색', smell: '약한 산화취', viscosity: 300, pH: 3.3, separation: 'no', photo: null, flagged: true, reasons: ['색상이 "투명"에서 "연한 황색"(으)로 변했습니다.'] },
        ],
      },
      {
        id: 4,
        name: '클렌징오일 순한버전 v2',
        condition: '상온(25℃)',
        cycleDays: 14,
        nextDue: now + 9 * DAY,
        observations: [
          { date: now - 19 * DAY, color: '연한 노란색', smell: '이상 없음', viscosity: 380, pH: 6.0, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 5 * DAY, color: '연한 노란색', smell: '이상 없음', viscosity: 390, pH: 6.0, separation: 'no', photo: null, flagged: false, reasons: [] },
        ],
      },
      {
        id: 5,
        name: '톤업선크림 핑크베이스 시제품 #3',
        condition: '광안정성',
        cycleDays: 3,
        nextDue: now - 2 * DAY,
        observations: [
          { date: now - 11 * DAY, color: '연핑크색', smell: '이상 없음', viscosity: 18500, pH: 7.0, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 8 * DAY, color: '연핑크색', smell: '이상 없음', viscosity: 18700, pH: 6.9, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 5 * DAY, color: '연핑크색', smell: '이상 없음', viscosity: 14500, pH: 6.8, separation: 'yes', photo: null, flagged: true, reasons: ['점도가 18700 → 14500cP로 22% 감소했습니다.', '상 분리가 관찰되었습니다.'] },
        ],
      },
      {
        id: 6,
        name: '나이트리페어 세럼 레티놀 0.3%',
        condition: '저온(4℃)',
        cycleDays: 7,
        nextDue: now + 6 * DAY,
        observations: [
          { date: now - 15 * DAY, color: '연한 노란색', smell: '이상 없음', viscosity: 850, pH: 5.5, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 8 * DAY, color: '연한 노란색', smell: '이상 없음', viscosity: 860, pH: 5.5, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 1 * DAY, color: '연한 노란색', smell: '이상 없음', viscosity: 855, pH: 5.4, separation: 'no', photo: null, flagged: false, reasons: [] },
        ],
      },
      {
        id: 7,
        name: '진정토너 병풀추출물 고함량',
        condition: '상온(25℃)',
        cycleDays: 7,
        nextDue: now + 2 * DAY,
        observations: [
          { date: now - 12 * DAY, color: '투명한 연녹색', smell: '이상 없음', viscosity: 280, pH: 5.8, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 5 * DAY, color: '투명한 연녹색', smell: '이상 없음', viscosity: 290, pH: 5.7, separation: 'no', photo: null, flagged: false, reasons: [] },
        ],
      },
      {
        id: 8,
        name: '립밤 SPF15 UV차단 신규처방',
        condition: '냉동-해동 반복',
        cycleDays: 5,
        nextDue: now + 1 * DAY,
        observations: [
          { date: now - 14 * DAY, color: '아이보리색', smell: '이상 없음', viscosity: 85000, pH: 7.5, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 9 * DAY, color: '아이보리색', smell: '이상 없음', viscosity: 84500, pH: 7.5, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 4 * DAY, color: '아이보리색', smell: '표면 미세 기포 및 얼룩', viscosity: 66000, pH: 7.4, separation: 'yes', photo: null, flagged: true, reasons: ['점도가 84500 → 66000cP로 22% 감소했습니다.', '상 분리가 관찰되었습니다.'] },
        ],
      },
      {
        id: 9,
        name: '미스트 선쿠션 리필용 유화 테스트',
        condition: '40℃ 가혹조건',
        cycleDays: 5,
        nextDue: now - 3 * DAY,
        observations: [
          { date: now - 18 * DAY, color: '화이트', smell: '이상 없음', viscosity: 12000, pH: 6.8, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 13 * DAY, color: '화이트', smell: '이상 없음', viscosity: 12200, pH: 6.7, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 8 * DAY, color: '화이트', smell: '고소한 유분 분리취', viscosity: 9000, pH: 6.2, separation: 'yes', photo: null, flagged: true, reasons: ['점도가 12200 → 9000cP로 26% 감소했습니다.', 'pH가 6.7 → 6.2로 0.5 변화했습니다.', '상 분리가 관찰되었습니다.'] },
        ],
      },
      {
        id: 10,
        name: '저자극 파운데이션 쿠션 유화제 교체판',
        condition: '냉동-해동 반복',
        cycleDays: 7,
        nextDue: now + 6 * DAY,
        observations: [
          { date: now - 8 * DAY, color: '베이지색', smell: '이상 없음', viscosity: 22000, pH: 6.5, separation: 'no', photo: null, flagged: false, reasons: [] },
          { date: now - 1 * DAY, color: '베이지색', smell: '이상 없음', viscosity: 22300, pH: 6.4, separation: 'no', photo: null, flagged: false, reasons: [] },
        ],
      },
    ];
    saveTests(seed);
    return seed;
  }

  function saveTests(tests) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tests));
  }

  let tests = loadTests();
  let activeObserveTestId = null;
  let activeDetailTestId = null;
  let searchTerm = '';
  let flagOnly = false;
  let todayOnly = false;

  function daysBetween(a, b) {
    return Math.round((a - b) / DAY);
  }

  function formatDate(ts) {
    const d = new Date(ts);
    return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, '0')}.${String(d.getDate()).padStart(2, '0')}`;
  }

  function lastObservation(test) {
    return test.observations.length ? test.observations[test.observations.length - 1] : null;
  }

  function testStatus(test) {
    const last = lastObservation(test);
    return last && last.flagged ? 'warn' : 'ok';
  }

  // 이전 관찰값 대비 색상/점도/pH/분리 여부를 비교해 이상 징후를 사람이 읽을 수 있는 문장으로 만든다.
  function analyzeObservation(curr, prev) {
    const reasons = [];
    if (prev) {
      if (prev.viscosity != null && curr.viscosity != null && prev.viscosity !== 0) {
        const changePct = Math.abs(curr.viscosity - prev.viscosity) / prev.viscosity * 100;
        if (changePct >= 20) {
          reasons.push(`점도가 ${prev.viscosity} → ${curr.viscosity}cP로 ${changePct.toFixed(0)}% ${curr.viscosity > prev.viscosity ? '증가' : '감소'}했습니다.`);
        }
      }
      if (prev.pH != null && curr.pH != null) {
        const diff = Math.abs(curr.pH - prev.pH);
        if (diff >= 0.5) {
          reasons.push(`pH가 ${prev.pH} → ${curr.pH}로 ${diff.toFixed(1)} 변화했습니다.`);
        }
      }
      if (prev.color && curr.color && prev.color.trim() !== curr.color.trim()) {
        reasons.push(`색상이 "${prev.color}"에서 "${curr.color}"(으)로 변했습니다.`);
      }
    }
    if (curr.separation === 'yes') {
      reasons.push('상 분리가 관찰되었습니다.');
    }
    return { flagged: reasons.length > 0, reasons };
  }

  function render() {
    const total = tests.length;
    const warnCount = tests.filter(t => testStatus(t) === 'warn').length;
    document.getElementById('stat-total').textContent = total;
    document.getElementById('stat-ok').textContent = total - warnCount;
    document.getElementById('stat-warn').textContent = warnCount;

    const term = searchTerm.trim().toLowerCase();
    const matchesFilters = (t) =>
      (!term || t.name.toLowerCase().includes(term)) &&
      (!flagOnly || testStatus(t) === 'warn') &&
      (!todayOnly || daysBetween(t.nextDue, Date.now()) <= 0);

    // 이번 주 확인 필요 = 관찰 예정일이 7일 이내이거나 최근 관찰에서 이상 징후가 발견된 시험
    const attentionList = document.getElementById('attention-list');
    const attentionAll = tests.filter(t => daysBetween(t.nextDue, Date.now()) <= 7 || testStatus(t) === 'warn');
    const attention = attentionAll.filter(matchesFilters).sort((a, b) => a.nextDue - b.nextDue);

    const promoText = document.getElementById('promo-text');
    promoText.textContent = attentionAll.length > 0
      ? `이번 주 확인이 필요한 시험이 ${attentionAll.length}건 있습니다.`
      : '이번 주 확인이 필요한 시험이 없습니다.';

    attentionList.innerHTML = '';
    if (attention.length === 0) {
      attentionList.innerHTML = attentionAll.length === 0
        ? '<div class="empty-state">이번 주 확인이 필요한 시험이 없습니다.</div>'
        : '<div class="empty-state">조건에 맞는 시험이 없습니다.</div>';
    } else {
      attention.forEach(t => {
        const diff = daysBetween(t.nextDue, Date.now());
        const dueBadge = diff <= 0
          ? { text: '오늘 관찰', cls: 'due-today' }
          : { text: `${diff}일 후`, cls: 'due-soon' };
        const last = lastObservation(t);
        const el = document.createElement('div');
        el.className = 'item-card';
        el.innerHTML = `
          <div class="item-main">
            <div class="item-name">${t.name}</div>
            <div class="item-meta">${t.condition} · ${t.cycleDays}일 주기</div>
            ${last && last.flagged ? `<div class="item-reason">⚠ ${last.reasons[0]}${last.reasons.length > 1 ? ` 외 ${last.reasons.length - 1}건` : ''}</div>` : ''}
          </div>
          <div class="item-side">
            <span class="badge ${last && last.flagged ? 'status-warn' : dueBadge.cls}">${last && last.flagged ? '이상 징후' : dueBadge.text}</span>
            <button class="btn-observe" data-id="${t.id}">관찰 결과 입력</button>
          </div>
        `;
        el.querySelector('.btn-observe').addEventListener('click', (e) => {
          e.stopPropagation();
          openObserveModal(t.id);
        });
        el.addEventListener('click', () => openDetailModal(t.id));
        attentionList.appendChild(el);
      });
    }

    const allList = document.getElementById('all-list');
    allList.innerHTML = '';
    const filteredAll = tests.filter(matchesFilters);
    if (filteredAll.length === 0) {
      allList.innerHTML = '<div class="empty-state">조건에 맞는 시험이 없습니다.</div>';
    } else {
      filteredAll.forEach(t => {
        const status = testStatus(t);
        const el = document.createElement('div');
        el.className = 'item-card';
        el.innerHTML = `
          <div class="item-main">
            <div class="item-name">${t.name}</div>
            <div class="item-meta">${t.condition} · ${t.cycleDays}일 주기 · 관찰 ${t.observations.length}회</div>
          </div>
          <span class="badge ${status === 'warn' ? 'status-warn' : 'status-ok'}">${status === 'warn' ? '이상 징후' : '정상'}</span>
        `;
        el.addEventListener('click', () => openDetailModal(t.id));
        allList.appendChild(el);
      });
    }
  }

  // ---------- 새 시험 등록 ----------
  const modalAdd = document.getElementById('modal-add');
  const openAddModal = () => modalAdd.classList.add('open');
  document.getElementById('fab-add').addEventListener('click', openAddModal);
  document.getElementById('btn-nav-add').addEventListener('click', openAddModal);
  document.getElementById('hero-cta-add').addEventListener('click', openAddModal);
  document.getElementById('btn-add-cancel').addEventListener('click', () => modalAdd.classList.remove('open'));

  document.getElementById('btn-add-save').addEventListener('click', () => {
    const name = document.getElementById('f-name').value.trim();
    const condition = document.getElementById('f-condition').value;
    const cycleDays = Number(document.getElementById('f-cycle').value) || 7;
    if (!name) {
      alert('샘플명을 입력해주세요.');
      return;
    }
    tests.push({
      id: Date.now(),
      name,
      condition,
      cycleDays,
      nextDue: Date.now(),
      observations: [],
    });
    saveTests(tests);
    render();
    modalAdd.classList.remove('open');
    document.getElementById('f-name').value = '';
  });

  // ---------- 관찰 결과 입력 ----------
  const modalObserve = document.getElementById('modal-observe');

  function openObserveModal(testId) {
    activeObserveTestId = testId;
    const t = tests.find(x => x.id === testId);
    document.getElementById('observe-title').textContent = '관찰 결과 입력';
    document.getElementById('observe-sub').textContent = `${t.name} · ${t.condition}`;
    document.getElementById('o-color').value = '';
    document.getElementById('o-smell').value = '';
    document.getElementById('o-viscosity').value = '';
    document.getElementById('o-ph').value = '';
    document.getElementById('o-separation').value = 'no';
    document.getElementById('o-photo').value = '';
    modalObserve.classList.add('open');
  }

  document.getElementById('btn-observe-cancel').addEventListener('click', () => modalObserve.classList.remove('open'));

  document.getElementById('btn-observe-save').addEventListener('click', () => {
    const t = tests.find(x => x.id === activeObserveTestId);
    if (!t) return;

    const color = document.getElementById('o-color').value.trim();
    const smell = document.getElementById('o-smell').value.trim();
    const viscosity = Number(document.getElementById('o-viscosity').value);
    const pH = Number(document.getElementById('o-ph').value);
    const separation = document.getElementById('o-separation').value;
    const photoFile = document.getElementById('o-photo').files[0];

    if (!color || !viscosity || !pH) {
      alert('색상, 점도, pH는 필수 입력 항목입니다.');
      return;
    }

    const prev = lastObservation(t);
    const finalize = (photoDataUrl) => {
      const curr = { date: Date.now(), color, smell, viscosity, pH, separation, photo: photoDataUrl || null };
      const analysis = analyzeObservation(curr, prev);
      curr.flagged = analysis.flagged;
      curr.reasons = analysis.reasons;
      t.observations.push(curr);
      t.nextDue = Date.now() + t.cycleDays * DAY;
      saveTests(tests);
      render();
      modalObserve.classList.remove('open');
    };

    if (photoFile) {
      const reader = new FileReader();
      reader.onload = () => finalize(reader.result);
      reader.readAsDataURL(photoFile);
    } else {
      finalize(null);
    }
  });

  // ---------- 상세보기 ----------
  const modalDetail = document.getElementById('modal-detail');
  document.getElementById('btn-detail-close').addEventListener('click', () => modalDetail.classList.remove('open'));

  function buildLineChart(observations, key, colorHex) {
    const points = observations.filter(o => o[key] != null && !isNaN(o[key]));
    if (points.length === 0) {
      return '<div class="chart-empty">데이터가 없습니다.</div>';
    }
    const width = 300, height = 80, pad = 16;
    const values = points.map(p => Number(p[key]));
    const min = Math.min(...values);
    const max = Math.max(...values);
    // 값이 하나뿐이거나 모두 같으면 기준선 가운데에 점을 찍어 보여준다.
    const effMin = max === min ? min - Math.max(Math.abs(min) * 0.1, 1) : min;
    const effMax = max === min ? max + Math.max(Math.abs(max) * 0.1, 1) : max;
    const effRange = effMax - effMin;
    const stepX = points.length > 1 ? (width - pad * 2) / (points.length - 1) : 0;
    const coords = points.map((p, i) => {
      const x = points.length > 1 ? pad + i * stepX : width / 2;
      const y = height - pad - ((Number(p[key]) - effMin) / effRange) * (height - pad * 2);
      return [x, y];
    });
    const line = coords.length > 1
      ? `<polyline points="${coords.map(c => c.join(',')).join(' ')}" fill="none" stroke="${colorHex}" stroke-width="2" />`
      : '';
    const circles = coords.map(([x, y], i) => {
      const isFlagged = points[i].flagged;
      return `<circle cx="${x}" cy="${y}" r="4" fill="${isFlagged ? '#e8593b' : colorHex}" />`;
    }).join('');
    const soloLabel = coords.length === 1
      ? `<text x="${coords[0][0]}" y="${coords[0][1] - 10}" font-size="11" fill="${colorHex}" text-anchor="middle">${values[0]}</text>`
      : '';
    return `<svg viewBox="0 0 ${width} ${height}" class="chart-svg" preserveAspectRatio="none">
      <line x1="${pad}" y1="${height - pad}" x2="${width - pad}" y2="${height - pad}" stroke="#e5e7eb" stroke-width="1" />
      ${line}
      ${circles}
      ${soloLabel}
    </svg>`;
  }

  function openDetailModal(testId) {
    activeDetailTestId = testId;
    const t = tests.find(x => x.id === testId);
    document.getElementById('detail-title').textContent = t.name;
    document.getElementById('detail-sub').textContent = `${t.condition} · ${t.cycleDays}일 주기 · 다음 관찰: ${formatDate(t.nextDue)}`;

    const last = lastObservation(t);
    const summaryBox = document.getElementById('detail-ai-summary');
    if (last && last.flagged) {
      summaryBox.innerHTML = `
        <div class="ai-summary-box">
          <div class="ai-title">⚠ 이상 징후 요약 (최근 관찰: ${formatDate(last.date)})</div>
          <ul>${last.reasons.map(r => `<li>${r}</li>`).join('')}</ul>
        </div>`;
    } else if (last) {
      summaryBox.innerHTML = `
        <div class="ai-summary-box ok">
          <div class="ai-title">✔ 정상</div>
          <p>이전 관찰 대비 특이 변화가 감지되지 않았습니다. (최근 관찰: ${formatDate(last.date)})</p>
        </div>`;
    } else {
      summaryBox.innerHTML = `
        <div class="ai-summary-box ok">
          <div class="ai-title">관찰 대기</div>
          <p>아직 등록된 관찰 결과가 없습니다.</p>
        </div>`;
    }

    document.getElementById('chart-viscosity').innerHTML = buildLineChart(t.observations, 'viscosity', '#2e6da4');
    document.getElementById('chart-ph').innerHTML = buildLineChart(t.observations, 'pH', '#1f4e79');

    const tbody = document.getElementById('obs-tbody');
    tbody.innerHTML = '';
    if (t.observations.length === 0) {
      tbody.innerHTML = '<tr><td colspan="7" style="color:var(--gray-600);">관찰 이력이 없습니다.</td></tr>';
    } else {
      [...t.observations].reverse().forEach(o => {
        const tr = document.createElement('tr');
        if (o.flagged) tr.className = 'flagged';
        tr.innerHTML = `
          <td>${formatDate(o.date)}</td>
          <td>${o.color}</td>
          <td>${o.smell || '-'}</td>
          <td>${o.viscosity}</td>
          <td>${o.pH}</td>
          <td>${o.separation === 'yes' ? '있음' : '없음'}</td>
          <td>${o.photo ? `<img class="photo-thumb" src="${o.photo}" />` : '-'}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    modalDetail.classList.add('open');
  }

  // ---------- 사용 가이드 / 문의하기 / 데이터 내보내기 ----------
  const modalGuide = document.getElementById('modal-guide');
  document.getElementById('link-guide').addEventListener('click', (e) => {
    e.preventDefault();
    modalGuide.classList.add('open');
  });
  document.getElementById('btn-guide-close').addEventListener('click', () => modalGuide.classList.remove('open'));

  const modalContact = document.getElementById('modal-contact');
  document.getElementById('link-contact').addEventListener('click', (e) => {
    e.preventDefault();
    modalContact.classList.add('open');
  });
  document.getElementById('btn-contact-close').addEventListener('click', () => modalContact.classList.remove('open'));

  function csvEscape(value) {
    const str = String(value ?? '');
    return /[",\r\n]/.test(str) ? '"' + str.replace(/"/g, '""') + '"' : str;
  }

  function exportTestsToCsv() {
    const header = ['샘플명', '시험조건', '관찰주기(일)', '관찰일자', '색상', '냄새', '점도(cP)', 'pH', '상분리', '이상징후'];
    const rows = [header];
    tests.forEach(t => {
      if (t.observations.length === 0) {
        rows.push([t.name, t.condition, t.cycleDays, '', '', '', '', '', '', '관찰 대기']);
      } else {
        t.observations.forEach(o => {
          rows.push([
            t.name, t.condition, t.cycleDays, formatDate(o.date), o.color, o.smell || '',
            o.viscosity, o.pH, o.separation === 'yes' ? '있음' : '없음', o.flagged ? '이상 징후' : '정상',
          ]);
        });
      }
    });
    const csvContent = rows.map(r => r.map(csvEscape).join(',')).join('\r\n');
    const blob = new Blob(['﻿' + csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `stabilitylog_export_${formatDate(Date.now())}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  document.getElementById('link-export').addEventListener('click', (e) => {
    e.preventDefault();
    exportTestsToCsv();
  });

  // ---------- 검색 / 이상 징후 필터 ----------
  const navSearch = document.getElementById('nav-search');
  const searchInput = document.getElementById('search-input');
  document.getElementById('btn-search-toggle').addEventListener('click', () => {
    navSearch.classList.toggle('open');
    if (navSearch.classList.contains('open')) searchInput.focus();
  });
  searchInput.addEventListener('input', (e) => {
    searchTerm = e.target.value;
    render();
  });

  const flagToggleBtn = document.getElementById('btn-flag-toggle');
  flagToggleBtn.addEventListener('click', () => {
    flagOnly = !flagOnly;
    flagToggleBtn.classList.toggle('active', flagOnly);
    render();
  });

  const todayToggleBtn = document.getElementById('btn-today-toggle');
  todayToggleBtn.addEventListener('click', () => {
    todayOnly = !todayOnly;
    todayToggleBtn.classList.toggle('active', todayOnly);
    render();
  });

  render();

  const splash = document.getElementById('splash');
  setTimeout(() => {
    splash.classList.add('hide');
    splash.addEventListener('transitionend', () => splash.remove(), { once: true });
  }, 550);
</script>

</body>
</html>

"""

components.html(HTML_CONTENT, height=1400, scrolling=True)