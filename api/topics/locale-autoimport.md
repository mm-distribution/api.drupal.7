# Automatic interface translation import

- **Topic id:** `locale-autoimport`
- **Defined in:** [`includes/locale.inc`](../includes/locale.inc/_file.md), line 2235 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2235)

## Documentation

```text
@defgroup locale-autoimport Automatic interface translation import
@{
Functions to create batches for importing translations.

These functions can be used to import translations for installed
modules.
```

## Members (derived, 6)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_locale_batch_build()](../includes/locale.inc/_locale_batch_build.md) (function) — Build a locale batch from an array of files.
- [_locale_batch_import()](../includes/locale.inc/_locale_batch_import.md) (function) — Implements callback_batch_operation().
- [_locale_batch_language_finished()](../includes/locale.inc/_locale_batch_language_finished.md) (function) — Implements callback_batch_finished().
- [_locale_batch_system_finished()](../includes/locale.inc/_locale_batch_system_finished.md) (function) — Implements callback_batch_finished().
- [locale_batch_by_component()](../includes/locale.inc/locale_batch_by_component.md) (function) — Prepare a batch to run when installing modules or enabling themes.
- [locale_batch_by_language()](../includes/locale.inc/locale_batch_by_language.md) (function) — Prepare a batch to import translations for all enabled modules in a given language.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
