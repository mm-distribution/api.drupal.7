# Translation import/export API.

- **Topic id:** `locale-api-import-export`
- **Defined in:** [`includes/locale.inc`](../includes/locale.inc/_file.md), line 646 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L646)

## Documentation

```text
@defgroup locale-api-import-export Translation import/export API.
@{
Functions to import and export translations.

These functions provide the ability to import translations from
external files and to export translations and translation templates.
```

## Members (derived, 18)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_locale_export_get_strings()](../includes/locale.inc/_locale_export_get_strings.md) (function) — Generates a structured array of all strings with translations in $language, if given. This array can be used to generate an export of the string in the database.
- [_locale_export_po()](../includes/locale.inc/_locale_export_po.md) (function) — Write a generated PO or POT file to the output.
- [_locale_export_po_generate()](../includes/locale.inc/_locale_export_po_generate.md) (function) — Generates the PO(T) file contents for given strings.
- [_locale_export_remove_plural()](../includes/locale.inc/_locale_export_remove_plural.md) (function) — Removes plural index information from a string
- [_locale_export_string()](../includes/locale.inc/_locale_export_string.md) (function) — Print out a string on multiple lines
- [_locale_export_wrap()](../includes/locale.inc/_locale_export_wrap.md) (function) — Custom word wrapping for Portable Object (Template) files.
- [_locale_import_append_plural()](../includes/locale.inc/_locale_import_append_plural.md) (function) — Modify a string to contain proper count indices
- [_locale_import_message()](../includes/locale.inc/_locale_import_message.md) (function) — Sets an error message occurred during locale file parsing.
- [_locale_import_one_string()](../includes/locale.inc/_locale_import_one_string.md) (function) — Imports a string into the database
- [_locale_import_one_string_db()](../includes/locale.inc/_locale_import_one_string_db.md) (function) — Import one string into the database.
- [_locale_import_parse_arithmetic()](../includes/locale.inc/_locale_import_parse_arithmetic.md) (function) — Parses and sanitizes an arithmetic formula into a PHP expression
- [_locale_import_parse_header()](../includes/locale.inc/_locale_import_parse_header.md) (function) — Parses a Gettext Portable Object file header
- [_locale_import_parse_plural_forms()](../includes/locale.inc/_locale_import_parse_plural_forms.md) (function) — Parses a Plural-Forms entry from a Gettext Portable Object file header
- [_locale_import_parse_quoted()](../includes/locale.inc/_locale_import_parse_quoted.md) (function) — Parses a string in quotes
- [_locale_import_po()](../includes/locale.inc/_locale_import_po.md) (function) — Parses Gettext Portable Object file information and inserts into database
- [_locale_import_read_po()](../includes/locale.inc/_locale_import_read_po.md) (function) — Parses Gettext Portable Object file into an array
- [_locale_import_shorten_comments()](../includes/locale.inc/_locale_import_shorten_comments.md) (function) — Generate a short, one string version of the passed comment array
- [_locale_import_tokenize_formula()](../includes/locale.inc/_locale_import_tokenize_formula.md) (function) — Backward compatible implementation of token_get_all() for formula parsing

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
