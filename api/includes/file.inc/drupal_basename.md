# drupal_basename()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2478–2494 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2478-L2494)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_basename($uri, $suffix = NULL)
```

## Documentation

```text
Gets the filename from a given path.

PHP's basename() does not properly support streams or filenames beginning
with a non-US-ASCII character.

@see http://bugs.php.net/bug.php?id=37738
@see basename()

@ingroup php_wrappers
```

## Code

```php
function drupal_basename($uri, $suffix = NULL) {
  $separators = '/';
  if (DIRECTORY_SEPARATOR != '/') {
    // For Windows OS add special separator.
    $separators .= DIRECTORY_SEPARATOR;
  }
  // Remove right-most slashes when $uri points to directory.
  $uri = rtrim($uri, $separators);
  // Returns the trailing part of the $uri starting after one of the directory
  // separators.
  $filename = preg_match('@[^' . preg_quote($separators, '@') . ']+$@', $uri, $matches) ? $matches[0] : '';
  // Cuts off a suffix from the filename.
  if ($suffix) {
    $filename = preg_replace('@' . preg_quote($suffix, '@') . '$@', '', $filename);
  }
  return $filename;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
