# Compress a PDF under an 8 MB upload limit — free, without uploading it

The insurance app wants your medical receipts as a PDF **under 8 MB**. A government portal rejects files over 10 MB. An HR system caps attachments.
This free tool shrinks the PDF to fit — without sending it anywhere.

- Tool: https://www.coding-now.com/en/pdf-compressor
- The PDF is processed **only in your browser**. It is never sent to a server or anywhere else.

## Steps

1. Drop the PDF in, or click to choose it.
2. Keep the method on **Keep text · recompress images** for most files.
3. Choose the **Size limit** the upload form asks for (for example 8 MB).
4. Click **Compress PDF** and download when the check finishes.

If it is still over the limit, it compresses once more at a stronger level, and if that is not enough it **splits the PDF by pages** so each file is under the limit.
Most claim and application forms accept several attachments, so the split files usually go through where one big file would not.

## How much smaller (measured)

| PDF | Before | After |
|---|---|---|
| Four phone photos | 2.18 MB | 0.18 MB (−92%) |
| 4-page scan | 5.12 MB | 0.93 MB (−82%) |
| 16-page paper with figures | 7.70 MB | 4.58 MB (−40%) |
| 68-page text document | 0.51 MB | 0.51 MB (−0.3%) |

Most of a PDF's size is its images, so photo PDFs and scans shrink the most and text-only PDFs barely change.

## Your file stays on your computer

While a PDF was loaded, compressed and checked, the browser made **zero network requests** (Chrome DevTools, 2026-10-06).
To check it yourself, press F12, open the Network tab, and compress a file — no new request appears.

## It checks that nothing broke

The result is reopened, its page count compared with the original, and every page rendered small and compared with the original page.
If any page looks very different, the result is discarded and the original kept. Split files get the same check.

## Two methods

| Method | Text selectable | Best for |
|---|---|---|
| Keep text · recompress images | Yes | Documents with photos, photo receipts |
| Strong · turn pages into images | No | Scans, or PDFs that will not fit any other way |

## Good to know

- Password-protected PDFs cannot be compressed. Remove the password first.
- The limit counts 1 MB = 1,000,000 bytes, so it also passes sites that use 1,048,576.
- Keep the tab open while it works.

Why PDFs get large, and other ways to shrink them in Word, on a Mac or with Ghostscript:
https://www.coding-now.com/en/guides/reduce-pdf-file-size
