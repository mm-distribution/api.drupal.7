# Sanitization functions

- **Topic id:** `sanitization`
- **Defined in:** [`includes/common.inc`](../includes/common.inc/_file.md), line 1418 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1418)

## Documentation

```text
@defgroup sanitization Sanitization functions
@{
Functions to sanitize values.

See http://drupal.org/writing-secure-code for information
on writing secure code.
```

## Members (derived, 14)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_filter_xss_attributes()](../includes/common.inc/_filter_xss_attributes.md) (function) — Processes a string of HTML attributes.
- [_filter_xss_split()](../includes/common.inc/_filter_xss_split.md) (function) — Processes an HTML tag.
- [check_markup()](../modules/filter/filter.module/check_markup.md) (function) — Runs all the enabled filters on a piece of text.
- [check_plain()](../includes/bootstrap.inc/check_plain.md) (function) — Encodes special characters in a plain-text string for display as HTML.
- [check_url()](../includes/common.inc/check_url.md) (function) — Strips dangerous protocols from a URI and encodes it for output to HTML.
- [drupal_attributes()](../includes/common.inc/drupal_attributes.md) (function) — Converts an associative array to an XML/HTML tag attribute string.
- [drupal_strip_dangerous_protocols()](../includes/common.inc/drupal_strip_dangerous_protocols.md) (function) — Strips dangerous protocols (e.g. 'javascript:') from a URI.
- [filter_xss()](../includes/common.inc/filter_xss.md) (function) — Filters HTML to prevent cross-site-scripting (XSS) vulnerabilities.
- [filter_xss_admin()](../includes/common.inc/filter_xss_admin.md) (function) — Applies a very permissive XSS/HTML filter for admin-only use.
- [filter_xss_bad_protocol()](../includes/common.inc/filter_xss_bad_protocol.md) (function) — Processes an HTML attribute value and strips dangerous protocols from URLs.
- [format_string()](../includes/bootstrap.inc/format_string.md) (function) — Formats a string for HTML display by replacing variable placeholders.
- [get_t()](../includes/bootstrap.inc/get_t.md) (function) — Returns the name of the proper localization function.
- [st()](../includes/install.inc/st.md) (function) — Translates a string when some systems are not available.
- [t()](../includes/bootstrap.inc/t.md) (function) — Translates a string to the current language or to a given language.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
