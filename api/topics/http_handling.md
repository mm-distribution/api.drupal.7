# HTTP handling

- **Topic id:** `http_handling`
- **Defined in:** [`includes/common.inc`](../includes/common.inc/_file.md), line 397 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L397)

## Documentation

```text
@defgroup http_handling HTTP handling
@{
Functions to properly handle HTTP responses.
```

## Members (derived, 14)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_drupal_http_use_proxy()](../includes/common.inc/_drupal_http_use_proxy.md) (function) — Helper function for determining hosts excluded from needing a proxy.
- [_drupal_parse_response_status()](../includes/common.inc/_drupal_parse_response_status.md) (function) — Splits an HTTP response status line into components.
- [_drupal_should_strip_sensitive_headers_on_http_redirect()](../includes/common.inc/_drupal_should_strip_sensitive_headers_on_http_redirect.md) (function) — Determine whether to strip sensitive headers from a request when redirected.
- [drupal_access_denied()](../includes/common.inc/drupal_access_denied.md) (function) — Delivers an "access denied" error to the browser.
- [drupal_encode_path()](../includes/common.inc/drupal_encode_path.md) (function) — Encodes a Drupal path for use in a URL.
- [drupal_get_destination()](../includes/common.inc/drupal_get_destination.md) (function) — Prepares a 'destination' URL query parameter for use with drupal_goto().
- [drupal_get_query_array()](../includes/common.inc/drupal_get_query_array.md) (function) — Splits a URL-encoded query string into an array.
- [drupal_get_query_parameters()](../includes/common.inc/drupal_get_query_parameters.md) (function) — Processes a URL query parameter array to remove unwanted elements.
- [drupal_goto()](../includes/common.inc/drupal_goto.md) (function) — Sends the user to a different page.
- [drupal_http_build_query()](../includes/common.inc/drupal_http_build_query.md) (function) — Parses an array into a valid, rawurlencoded query string.
- [drupal_http_request()](../includes/common.inc/drupal_http_request.md) (function) — Performs an HTTP request.
- [drupal_not_found()](../includes/common.inc/drupal_not_found.md) (function) — Delivers a "page not found" error to the browser.
- [drupal_parse_url()](../includes/common.inc/drupal_parse_url.md) (function) — Parses a URL string into its path, query, and fragment components.
- [drupal_site_offline()](../includes/common.inc/drupal_site_offline.md) (function) — Delivers a "site is under maintenance" message to the browser.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
