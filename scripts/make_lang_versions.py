"""사이트의 두 언어 겸용 index.html 에서 ko/ · en/ 단일 언어 버전을 만든다.

사용(저장소 루트):
    python scripts/make_lang_versions.py <원본 index.html>
    예) python scripts/make_lang_versions.py ../../WebSite/Website_Codingnow/public/pdf-compressor/index.html

원본은 coding-now.com 의 public/pdf-compressor/index.html (KR/EN 전환 단추가 있는 한 파일).
여기서 바꾸는 것:
  - <html lang>, 기본 언어 고정(?lang·localStorage 무시), 제목·설명·canonical
  - 라이브러리 경로 vendor/ → ../vendor/ (두 버전이 루트의 vendor/ 를 같이 쓴다)
  - KR/EN 단추 → 다른 언어 폴더로 가는 링크
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "index.src.html"
src = SRC.read_text(encoding="utf-8")

META = {
    "ko": {
        "title": "PDF 용량 줄이기 — 업로드 없이 브라우저에서 압축 | CODINGNOW",
        "desc": "PDF 용량을 브라우저 안에서 줄입니다. 파일은 서버나 다른 곳으로 보내지 않습니다. 용량 제한에 맞게 줄이고, 그래도 크면 쪽 단위로 나눕니다.",
        "canonical": "https://www.coding-now.com/pdf-compressor",
    },
    "en": {
        "title": "Compress PDF — reduce PDF file size in your browser, no upload | CODINGNOW",
        "desc": "Reduce PDF file size inside your browser. The file is never sent to a server or anywhere else. Fit an upload size limit, or split by pages when it is still too big.",
        "canonical": "https://www.coding-now.com/en/pdf-compressor",
    },
}


def must_replace(s: str, old: str, new: str) -> str:
    if s.count(old) != 1:
        raise SystemExit(f"원본 구조가 바뀌었습니다 — 찾는 문구가 {s.count(old)}번 나옵니다: {old[:60]!r}")
    return s.replace(old, new)


for lang, m in META.items():
    s = src
    s = must_replace(s, '<html lang="ko">', f'<html lang="{lang}">')
    s = must_replace(
        s,
        "<script>try{var _l=new URLSearchParams(location.search).get('lang');if(_l==='ko'||_l==='en')localStorage.setItem('pdfc_lang',_l);}catch(e){}</script>\n",
        "",
    )
    s = must_replace(s, "<title>PDF 용량 줄이기 — 업로드 없이 브라우저에서 압축 | CODINGNOW</title>", f"<title>{m['title']}</title>")
    start = s.index('<meta name="description" content="')
    end = s.index('" />', start)
    s = s[:start] + f'<meta name="description" content="{m["desc"]}' + s[end:]
    s = must_replace(s, '<link rel="canonical" href="https://www.coding-now.com/pdf-compressor" />',
                     f'<link rel="canonical" href="{m["canonical"]}" />')
    s = must_replace(s, '<script src="vendor/pdf-lib.min.js"></script>', '<script src="../vendor/pdf-lib.min.js"></script>')
    s = must_replace(s, 'import * as pdfjsLib from "./vendor/pdf.min.mjs";', 'import * as pdfjsLib from "../vendor/pdf.min.mjs";')
    s = must_replace(s, 'new URL("./vendor/pdf.worker.min.mjs", import.meta.url)', 'new URL("../vendor/pdf.worker.min.mjs", import.meta.url)')
    s = must_replace(
        s,
        'let lang = "ko";\ntry { const s = localStorage.getItem("pdfc_lang"); if (s === "en" || s === "ko") lang = s; } catch (e) {}',
        f'let lang = "{lang}"; // 단일 언어 버전({lang}/) — 다른 언어는 ../{"en" if lang == "ko" else "ko"}/',
    )
    # 전환 단추 → 다른 폴더로 가는 링크
    s = must_replace(
        s,
        '''      <button type="button" data-lang="ko" class="active">KR</button>
      <button type="button" data-lang="en">EN</button>''',
        f'''      <a href="../ko/"{' class="active"' if lang == "ko" else ""}>KR</a>
      <a href="../en/"{' class="active"' if lang == "en" else ""}>EN</a>''',
    )
    s = must_replace(
        s,
        "  .langtoggle button.active{ background:var(--amber); color:#1a1304; font-weight:700; }\n",
        "  .langtoggle button.active{ background:var(--amber); color:#1a1304; font-weight:700; }\n"
        "  .langtoggle a{ padding:6px 14px; font-size:12px; color:var(--muted); background:var(--panel-2); text-decoration:none; }\n"
        "  .langtoggle a + a{ border-left:1px solid var(--line); }\n"
        "  .langtoggle a.active{ background:var(--amber); color:#1a1304; font-weight:700; }\n",
    )
    out = ROOT / lang / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(s, encoding="utf-8")
    print(f"{out.relative_to(ROOT)}  {len(s):,} bytes")
