# PDF 용량 줄이기 · PDF Compressor

브라우저 안에서 PDF 용량을 줄이는 단일 HTML 도구입니다. PDF 는 서버나 다른 곳으로 보내지 않습니다.
A single-HTML tool that reduces PDF file size inside your browser. The PDF is never sent anywhere.

| | 한국어 | English |
|---|---|---|
| 도구 · Tool | [`ko/index.html`](ko/index.html) | [`en/index.html`](en/index.html) |
| 설명 · README | [`ko/README.md`](ko/README.md) | [`en/README.md`](en/README.md) |
| 사용법 · How-to | [`ko/usage-guide.md`](ko/usage-guide.md) | [`en/usage-guide.md`](en/usage-guide.md) |
| 라이브 · Live | [coding-now.com/pdf-compressor](https://www.coding-now.com/pdf-compressor) | [coding-now.com/en/pdf-compressor](https://www.coding-now.com/en/pdf-compressor) |

![PDF 용량 줄이기 실행 화면](docs/images/screenshot-kr.png)

- 용량 제한(예: 8MB)에 맞게 줄이고, 그래도 크면 쪽 단위로 나눕니다 · Fits an upload size limit (e.g. 8 MB) and splits by pages if needed
- 결과를 원본과 쪽마다 비교해 깨지지 않았는지 확인합니다 · Every result is checked page by page against the original
- 처리 중 네트워크 요청 0건(실측) · Zero network requests while processing (measured)

## 구성 · Layout

```
ko/            한국어판 (index.html · README.md · usage-guide.md)
en/            English version
vendor/        pdf-lib 1.17.1 (MIT) · pdf.js 4.10.38 (Apache-2.0) — 두 판이 같이 씀 · shared
docs/images/   스크린샷 · screenshots
scripts/make_lang_versions.py   사이트의 두 언어 겸용 원본에서 ko/ · en/ 를 다시 만든다 · regenerates ko/ and en/
```

## 실행 · Run

`file://` 로는 열리지 않습니다(pdf.js 모듈·worker). 로컬 서버로 여세요 · Serve the folder (pdf.js needs http):

```
python -m http.server 8000
```

→ http://localhost:8000/ko/ · http://localhost:8000/en/
