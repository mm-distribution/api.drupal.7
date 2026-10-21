# Language negotiation options

- **Topic id:** `locale-languages-negotiation`
- **Defined in:** [`includes/locale.inc`](../includes/locale.inc/_file.md), line 99 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L99)

## Documentation

```text
@defgroup locale-languages-negotiation Language negotiation options
@{
Functions for language negotiation.

There are functions that provide the ability to identify the
language. This behavior can be controlled by various options.
```

## Members (derived, 10)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [locale_language_from_browser()](../includes/locale.inc/locale_language_from_browser.md) (function) — Identify language from the Accept-language HTTP header we got.
- [locale_language_from_interface()](../includes/locale.inc/locale_language_from_interface.md) (function) — Identifies the language from the current interface language.
- [locale_language_from_session()](../includes/locale.inc/locale_language_from_session.md) (function) — Identify language from a request/session parameter.
- [locale_language_from_url()](../includes/locale.inc/locale_language_from_url.md) (function) — Identify language via URL prefix or domain.
- [locale_language_from_user()](../includes/locale.inc/locale_language_from_user.md) (function) — Identify language from the user preferences.
- [locale_language_switcher_session()](../includes/locale.inc/locale_language_switcher_session.md) (function) — Return the session language switcher block.
- [locale_language_switcher_url()](../includes/locale.inc/locale_language_switcher_url.md) (function) — Return the URL language switcher block. Translation links may be provided by other modules.
- [locale_language_url_fallback()](../includes/locale.inc/locale_language_url_fallback.md) (function) — Determines the language to be assigned to URLs when none is detected.
- [locale_language_url_rewrite_session()](../includes/locale.inc/locale_language_url_rewrite_session.md) (function) — Rewrite URLs for the Session language provider.
- [locale_language_url_rewrite_url()](../includes/locale.inc/locale_language_url_rewrite_url.md) (function) — Rewrite URLs for the URL language provider.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
