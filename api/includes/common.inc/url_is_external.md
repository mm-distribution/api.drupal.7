# url_is_external()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2436–2454 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2436-L2454)

## Signature

```php
function url_is_external($path)
```

## Documentation

```text
Returns TRUE if a path is external to Drupal (e.g. http://example.com).

If a path cannot be assessed by Drupal's menu handler, then we must
treat it as potentially insecure.

@param $path
  The internal path or external URL being linked to, such as "node/34" or
  "http://example.com/foo".

@return
  Boolean TRUE or FALSE, where TRUE indicates an external path.
```

## Code

```php
function url_is_external($path) {
  $path = (string) $path;
  $colonpos = strpos($path, ':');
  // Some browsers treat \ as / so normalize to forward slashes.
  $path = str_replace('\\', '/', $path);
  // If the path starts with 2 slashes then it is always considered an external
  // URL without an explicit protocol part.
  return (strpos($path, '//') === 0)
    // Leading control characters may be ignored or mishandled by browsers, so
    // assume such a path may lead to an external location. The \p{C} character
    // class matches all UTF-8 control, unassigned, and private characters.
    || (preg_match('/^\p{C}/u', $path) !== 0)
    // Avoid calling drupal_strip_dangerous_protocols() if there is any slash
    // (/), hash (#) or question_mark (?) before the colon (:) occurrence - if
    // any - as this would clearly mean it is not a URL.
    || ($colonpos !== FALSE
      && !preg_match('![/?#]!', substr($path, 0, $colonpos))
      && drupal_strip_dangerous_protocols($path) == $path);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
