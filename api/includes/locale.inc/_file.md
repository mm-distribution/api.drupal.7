# includes/locale.inc

- **Source:** [local](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · 2501 lines

## File documentation

```text
@file
Administration functions for locale.module.
```

## Functions (derived index)

- [locale_language_from_interface()](locale_language_from_interface.md) — Identifies the language from the current interface language.
- [locale_language_from_browser()](locale_language_from_browser.md) — Identify language from the Accept-language HTTP header we got.
- [locale_language_from_user()](locale_language_from_user.md) — Identify language from the user preferences.
- [locale_language_from_session()](locale_language_from_session.md) — Identify language from a request/session parameter.
- [locale_language_from_url()](locale_language_from_url.md) — Identify language via URL prefix or domain.
- [locale_language_url_fallback()](locale_language_url_fallback.md) — Determines the language to be assigned to URLs when none is detected.
- [locale_language_switcher_url()](locale_language_switcher_url.md) — Return the URL language switcher block. Translation links may be provided by other modules.
- [locale_language_switcher_session()](locale_language_switcher_session.md) — Return the session language switcher block.
- [locale_language_url_rewrite_url()](locale_language_url_rewrite_url.md) — Rewrite URLs for the URL language provider.
- [locale_language_url_rewrite_session()](locale_language_url_rewrite_session.md) — Rewrite URLs for the Session language provider.
- [locale_string_is_safe()](locale_string_is_safe.md) — Check that a string is safe to be added or imported as a translation.
- [locale_add_language()](locale_add_language.md) — API function to add a language.
- [_locale_import_po()](_locale_import_po.md) — Parses Gettext Portable Object file information and inserts into database
- [_locale_import_read_po()](_locale_import_read_po.md) — Parses Gettext Portable Object file into an array
- [_locale_import_message()](_locale_import_message.md) — Sets an error message occurred during locale file parsing.
- [_locale_import_one_string()](_locale_import_one_string.md) — Imports a string into the database
- [_locale_import_one_string_db()](_locale_import_one_string_db.md) — Import one string into the database.
- [_locale_import_parse_header()](_locale_import_parse_header.md) — Parses a Gettext Portable Object file header
- [_locale_import_parse_plural_forms()](_locale_import_parse_plural_forms.md) — Parses a Plural-Forms entry from a Gettext Portable Object file header
- [_locale_import_parse_arithmetic()](_locale_import_parse_arithmetic.md) — Parses and sanitizes an arithmetic formula into a PHP expression
- [_locale_import_tokenize_formula()](_locale_import_tokenize_formula.md) — Backward compatible implementation of token_get_all() for formula parsing
- [_locale_import_append_plural()](_locale_import_append_plural.md) — Modify a string to contain proper count indices
- [_locale_import_shorten_comments()](_locale_import_shorten_comments.md) — Generate a short, one string version of the passed comment array
- [_locale_import_parse_quoted()](_locale_import_parse_quoted.md) — Parses a string in quotes
- [_locale_parse_js_file()](_locale_parse_js_file.md) — Parses a JavaScript file, extracts strings wrapped in Drupal.t() and Drupal.formatPlural() and inserts them into the database.
- [_locale_export_get_strings()](_locale_export_get_strings.md) — Generates a structured array of all strings with translations in $language, if given. This array can be used to generate an export of the string in the database.
- [_locale_export_po_generate()](_locale_export_po_generate.md) — Generates the PO(T) file contents for given strings.
- [_locale_export_po()](_locale_export_po.md) — Write a generated PO or POT file to the output.
- [_locale_export_string()](_locale_export_string.md) — Print out a string on multiple lines
- [_locale_export_wrap()](_locale_export_wrap.md) — Custom word wrapping for Portable Object (Template) files.
- [_locale_export_remove_plural()](_locale_export_remove_plural.md) — Removes plural index information from a string
- [_locale_translate_seek()](_locale_translate_seek.md) — Perform a string search and display results in a table
- [_locale_translate_seek_query()](_locale_translate_seek_query.md) — Build array out of search criteria specified in request variables
- [_locale_invalidate_js()](_locale_invalidate_js.md) — Force the JavaScript translation file(s) to be refreshed.
- [_locale_rebuild_js()](_locale_rebuild_js.md) — (Re-)Creates the JavaScript translation file for a language.
- [_locale_translate_language_list()](_locale_translate_language_list.md) — List languages in search result table
- [_locale_prepare_predefined_list()](_locale_prepare_predefined_list.md) — Prepares the language code list for a select form item with only the unsupported ones
- [locale_batch_by_language()](locale_batch_by_language.md) — Prepare a batch to import translations for all enabled modules in a given language.
- [locale_batch_by_component()](locale_batch_by_component.md) — Prepare a batch to run when installing modules or enabling themes.
- [_locale_batch_build()](_locale_batch_build.md) — Build a locale batch from an array of files.
- [_locale_batch_import()](_locale_batch_import.md) — Implements callback_batch_operation().
- [_locale_batch_system_finished()](_locale_batch_system_finished.md) — Implements callback_batch_finished().
- [_locale_batch_language_finished()](_locale_batch_language_finished.md) — Implements callback_batch_finished().
- [country_get_list()](country_get_list.md) — Get list of all predefined and custom countries.
- [locale_date_format_save()](locale_date_format_save.md) — Save locale specific date formats to the database.
- [locale_get_localized_date_format()](locale_get_localized_date_format.md) — Select locale date format details from database.

## Constants

### LOCALE_LANGUAGE_NEGOTIATION_URL

- Line 12

```php
define('LOCALE_LANGUAGE_NEGOTIATION_URL', 'locale-url');
```

```text
The language is determined using a URL language indicator:
path prefix or domain according to the configuration.
```

### LOCALE_LANGUAGE_NEGOTIATION_BROWSER

- Line 17

```php
define('LOCALE_LANGUAGE_NEGOTIATION_BROWSER', 'locale-browser');
```

```text
The language is set based on the browser language settings.
```

### LOCALE_LANGUAGE_NEGOTIATION_INTERFACE

- Line 22

```php
define('LOCALE_LANGUAGE_NEGOTIATION_INTERFACE', 'locale-interface');
```

```text
The language is determined using the current interface language.
```

### LOCALE_LANGUAGE_NEGOTIATION_URL_FALLBACK

- Line 28

```php
define('LOCALE_LANGUAGE_NEGOTIATION_URL_FALLBACK', 'locale-url-fallback');
```

```text
If no URL language is available language is determined using an already
detected one.
```

### LOCALE_LANGUAGE_NEGOTIATION_USER

- Line 33

```php
define('LOCALE_LANGUAGE_NEGOTIATION_USER', 'locale-user');
```

```text
The language is set based on the user language settings.
```

### LOCALE_LANGUAGE_NEGOTIATION_SESSION

- Line 38

```php
define('LOCALE_LANGUAGE_NEGOTIATION_SESSION', 'locale-session');
```

```text
The language is set based on the request/session parameters.
```

### LOCALE_JS_STRING

- Line 43

```php
define('LOCALE_JS_STRING', '(?:(?:\'(?:\\\\\'|[^\'])*\'|"(?:\\\\"|[^"])*")(?:\s*\+\s*)?)+');
```

```text
Regular expression pattern used to localize JavaScript strings.
```

### LOCALE_JS_OBJECT

- Line 51

```php
define('LOCALE_JS_OBJECT', '\{.*?\}');
```

```text
Regular expression pattern used to match simple JS object literal.

This pattern matches a basic JS object, but will fail on an object with
nested objects. Used in JS file parsing for string arg processing.
```

### LOCALE_JS_OBJECT_CONTEXT

- Line 59

```php
define('LOCALE_JS_OBJECT_CONTEXT', '
  \{              # match object literal start
  .*?             # match anything, non-greedy
  (?:             # match a form of "context"
    \'context\'
    |
    "context"
    |
    context
  )
  \s*:\s*         # match key-value separator ":"
  (' . LOCALE_JS_STRING . ')  # match context string
  .*?             # match anything, non-greedy
  \}              # match end of object literal
');
```

```text
Regular expression to match an object containing a key 'context'.

Pattern to match a JS object containing a 'context key' with a string value,
which is captured. Will fail if there are nested objects.
```

### LOCALE_IMPORT_OVERWRITE

- Line 79

```php
define('LOCALE_IMPORT_OVERWRITE', 0);
```

```text
Translation import mode overwriting all existing translations
if new translated version available.
```

### LOCALE_IMPORT_KEEP

- Line 85

```php
define('LOCALE_IMPORT_KEEP', 1);
```

```text
Translation import mode keeping existing translations and only
inserting new strings.
```

### LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX

- Line 91

```php
define('LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX', 0);
```

```text
URL language negotiation: use the path prefix as URL language
indicator.
```

### LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN

- Line 97

```php
define('LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN', 1);
```

```text
URL language negotiation: use the domain as URL language
indicator.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
