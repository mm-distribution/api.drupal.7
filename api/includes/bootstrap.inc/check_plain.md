# check_plain()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1910–1912 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1910-L1912)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function check_plain($text)
```

## Documentation

```text
Encodes special characters in a plain-text string for display as HTML.

Also validates strings as UTF-8 to prevent cross site scripting attacks on
Internet Explorer 6.

@param string $text
  The text to be checked or processed.

@return string
  An HTML safe version of $text. If $text is not valid UTF-8, an empty string
  is returned and, on PHP < 5.4, a warning may be issued depending on server
  configuration (see @link https://bugs.php.net/bug.php?id=47494 @endlink).

@see drupal_validate_utf8()
@ingroup sanitization
```

## Code

```php
function check_plain($text) {
  return htmlspecialchars((string) $text, ENT_QUOTES, 'UTF-8');
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
