# _locale_import_shorten_comments()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1472–1484 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1472-L1484)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_shorten_comments($comment)
```

## Documentation

```text
Generate a short, one string version of the passed comment array

@param $comment
  An array of strings containing a comment.

@return
  Short one string version of the comment.
```

## Code

```php
function _locale_import_shorten_comments($comment) {
  $comm = '';
  while (count($comment)) {
    $test = $comm . substr(array_shift($comment), 1) . ', ';
    if (strlen($comm) < 130) {
      $comm = $test;
    }
    else {
      break;
    }
  }
  return trim(substr($comm, 0, -2));
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
