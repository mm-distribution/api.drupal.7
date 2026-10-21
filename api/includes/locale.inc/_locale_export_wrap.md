# _locale_export_wrap()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1841–1864 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1841-L1864)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_export_wrap($str, $len)
```

## Documentation

```text
Custom word wrapping for Portable Object (Template) files.
```

## Code

```php
function _locale_export_wrap($str, $len) {
  $words = explode(' ', $str);
  $return = array();

  $cur = "";
  $nstr = 1;
  while (count($words)) {
    $word = array_shift($words);
    if ($nstr) {
      $cur = $word;
      $nstr = 0;
    }
    elseif (strlen("$cur $word") > $len) {
      $return[] = $cur . " ";
      $cur = $word;
    }
    else {
      $cur = "$cur $word";
    }
  }
  $return[] = $cur;

  return implode("\n", $return);
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
