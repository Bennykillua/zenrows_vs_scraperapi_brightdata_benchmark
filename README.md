# zenrows-vs-scraperapi-brightdata-benchmark

This repository contains the scripts from an original benchmark comparing ZenRows and ScraperAPI across 8 target URLs at two concurrency levels, conducted in May 2026.

---

## Test Targets

| Target | Type | URL |
|--------|------|------|
| Amazon product page | Protected | https://www.amazon.com/ref=nav_logo |
| Glassdoor company page | Protected | https://www.glassdoor.com/Overview/Working-at-Google-EI_IE9079.11,17.htm |
| LinkedIn company profile | Protected | https://www.linkedin.com/in/satyanadella/ |
| Google SERP results page | Protected | https://www.google.com/search?q=web+scraping+api |
| Mid-sized e-commerce site behind Cloudflare, like Ikea.com| Protected | https://www.ikea.com/ |
| Zillow real estate listing | Unprotected | https://www.zillow.com/homes/for_sale/ |
| BBC news article | Unprotected | https://www.bbc.com/news/technology |

---

## Methodology

- **100 requests** per target per platform
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

