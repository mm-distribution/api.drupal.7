# PHP wrapper functions

- **Topic id:** `php_wrappers`
- **Defined in:** [`includes/common.inc`](../includes/common.inc/_file.md), line 11 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L11)

## Documentation

```text
@defgroup php_wrappers PHP wrapper functions
@{
Functions that are wrappers or custom implementations of PHP functions.

Certain PHP functions should not be used in Drupal. Instead, Drupal's
replacement functions should be used.

For example, for improved or more secure UTF8-handling, or RFC-compliant
handling of URLs in Drupal.

For ease of use and memorizing, all these wrapper functions use the same name
as the original PHP function, but prefixed with "drupal_". Beware, however,
that not all wrapper functions support the same arguments as the original
functions.

You should always use these wrapper functions in your code.

Wrong:
@code
  $my_substring = substr($original_string, 0, 5);
@endcode

Correct:
@code
  $my_substring = drupal_substr($original_string, 0, 5);
@endcode

@}
```

## Members (derived, 25)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [drupal_basename()](../includes/file.inc/drupal_basename.md) (function) — Gets the filename from a given path.
- [drupal_chmod()](../includes/file.inc/drupal_chmod.md) (function) — Sets the permissions on a file or directory.
- [drupal_dirname()](../includes/file.inc/drupal_dirname.md) (function) — Gets the name of the directory from a given path.
- [drupal_http_build_query()](../includes/common.inc/drupal_http_build_query.md) (function) — Parses an array into a valid, rawurlencoded query string.
- [drupal_json_decode()](../includes/common.inc/drupal_json_decode.md) (function) — Converts an HTML-safe JSON string into its PHP equivalent.
- [drupal_json_encode()](../includes/common.inc/drupal_json_encode.md) (function) — Converts a PHP variable into its JavaScript equivalent.
- [drupal_mkdir()](../includes/file.inc/drupal_mkdir.md) (function) — Creates a directory, optionally creating missing components in the path to the directory.
- [drupal_move_uploaded_file()](../includes/file.inc/drupal_move_uploaded_file.md) (function) — Moves an uploaded file to a new location.
- [drupal_parse_url()](../includes/common.inc/drupal_parse_url.md) (function) — Parses a URL string into its path, query, and fragment components.
- [drupal_realpath()](../includes/file.inc/drupal_realpath.md) (function) — Resolves the absolute filepath of a local URI or filepath.
- [drupal_register_shutdown_function()](../includes/bootstrap.inc/drupal_register_shutdown_function.md) (function) — Registers a function for execution on shutdown.
- [drupal_rmdir()](../includes/file.inc/drupal_rmdir.md) (function) — Removes a directory.
- [drupal_session_regenerate()](../includes/session.inc/drupal_session_regenerate.md) (function) — Called when an anonymous user becomes authenticated or vice-versa.
- [drupal_session_start()](../includes/session.inc/drupal_session_start.md) (function) — Starts a session forcefully, preserving already set session data.
- [drupal_set_time_limit()](../includes/common.inc/drupal_set_time_limit.md) (function) — Attempts to set the PHP maximum execution time.
- [drupal_setcookie()](../includes/bootstrap.inc/drupal_setcookie.md) (function) — Drupal's wrapper around PHP's setcookie() function.
- [drupal_strlen()](../includes/unicode.inc/drupal_strlen.md) (function) — Counts the number of characters in a UTF-8 string.
- [drupal_strtolower()](../includes/unicode.inc/drupal_strtolower.md) (function) — Lowercase a UTF-8 string.
- [drupal_strtoupper()](../includes/unicode.inc/drupal_strtoupper.md) (function) — Uppercase a UTF-8 string.
- [drupal_substr()](../includes/unicode.inc/drupal_substr.md) (function) — Cuts off a piece of a string based on character indices and counts.
- [drupal_tempnam()](../includes/file.inc/drupal_tempnam.md) (function) — Creates a file with a unique filename in the specified directory.
- [drupal_ucfirst()](../includes/unicode.inc/drupal_ucfirst.md) (function) — Capitalizes the first letter of a UTF-8 string.
- [drupal_unlink()](../includes/file.inc/drupal_unlink.md) (function) — Deletes a file.
- [drupal_xml_parser_create()](../includes/unicode.inc/drupal_xml_parser_create.md) (function) — Prepares a new XML parser.
- [php_eval()](../modules/php/php.module/php_eval.md) (function) — Evaluates a string of PHP code.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
