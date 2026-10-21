# format_string()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1871–1891 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1871-L1891)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function format_string($string, array $args = array())
```

## Documentation

```text
Formats a string for HTML display by replacing variable placeholders.

This function replaces variable placeholders in a string with the requested
values and escapes the values so they can be safely displayed as HTML. It
should be used on any unknown text that is intended to be printed to an HTML
page (especially text that may have come from untrusted users, since in that
case it prevents cross-site scripting and other security problems).

In most cases, you should use t() rather than calling this function
directly, since it will translate the text (on non-English-only sites) in
addition to formatting it.

@param $string
  A string containing placeholders.
@param $args
  An associative array of replacements to make. Occurrences in $string of
  any key in $args are replaced with the corresponding value, after optional
  sanitization and formatting. The type of sanitization and formatting
  depends on the first character of the key:
  - @variable: Escaped to HTML using check_plain(). Use this as the default
    choice for anything displayed on a page on the site.
  - %variable: Escaped to HTML and formatted using drupal_placeholder(),
    which makes it display as <em>emphasized</em> text.
  - !variable: Inserted as is, with no sanitization or formatting. Only use
    this for text that has already been prepared for HTML display (for
    example, user-supplied text that has already been run through
    check_plain() previously, or is expected to contain some limited HTML
    tags and has already been run through filter_xss() previously).

@see t()
@ingroup sanitization
```

## Code

```php
function format_string($string, array $args = array()) {
  // Transform arguments before inserting them.
  foreach ($args as $key => $value) {
    switch ($key[0]) {
      case '@':
        // Escaped only.
        $args[$key] = check_plain($value);
        break;

      case '%':
      default:
        // Escaped and placeholder.
        $args[$key] = drupal_placeholder($value);
        break;

      case '!':
        // Pass-through.
    }
  }
  return strtr($string, $args);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
