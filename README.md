# zenrows-vs-scraperapi-brightdata-benchmark

This repository contains the scripts from an original benchmark comparing ZenRows and ScraperAPI across 8 target URLs at two concurrency levels, conducted in May 2026.

---

## Test Targets

| Target | Type |
|--------|------|
| Amazon product page | Protected |
| Glassdoor company page | Protected |
| LinkedIn company profile | Protected |
| Google SERP results page | Protected |
| Mid-sized e-commerce site behind Cloudflare, like Ikea.com| Protected |
| Zillow real estate listing | Unprotected |
| BBC news article | Unprotected |

---

## Methodology

- **10 requests** per target per platform
- ZenRows configured with `mode=auto` on all requests
- Firecrawl's /scrape endpoint
- Bright Data's Web Unlocker
- Recorded per request: HTTP status code, response time (ms), and page title detection

### What this test does not cover

- Bulk asynchronous job workflows
- No-code scheduling via ScraperAPI DataPipeline
- Session persistence across multi-step logged-in workflows

---

## Setup

### Prerequisites

- Python 3.10+
- API keys for [ZenRows](https://app.zenrows.com/register)
- API keys for [Bright Data](https://brightdata.com/cp/billing/settings?get_started=1)
- API keys for [Firecrawl](https://www.firecrawl.dev/)

