# drupal_match_path()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 312–332 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L312-L332)

## Signature

```php
function drupal_match_path($path, $patterns)
```

## Documentation

```text
Check if a path matches any pattern in a set of patterns.

@param $path
  The path to match.
@param $patterns
  String containing a set of patterns separated by \n, \r or \r\n.

@return
  Boolean value: TRUE if the path matches a pattern, FALSE otherwise.
```

## Code

```php
function drupal_match_path($path, $patterns) {
  $regexps = &drupal_static(__FUNCTION__);

  if (!isset($regexps[$patterns])) {
    // Convert path settings to a regular expression.
    // Therefore replace newlines with a logical or, /* with asterisks and the <front> with the frontpage.
    $to_replace = array(
      '/(\r\n?|\n)/', // newlines
      '/\\\\\*/',     // asterisks
      '/(^|\|)\\\\<front\\\\>($|\|)/' // <front>
    );
    $replacements = array(
      '|',
      '.*',
      '\1' . preg_quote(variable_get('site_frontpage', 'node'), '/') . '\2'
    );
    $patterns_quoted = preg_quote($patterns, '/');
    $regexps[$patterns] = '/^(' . preg_replace($to_replace, $replacements, $patterns_quoted) . ')$/';
  }
  return (bool)preg_match($regexps[$patterns], $path);
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
