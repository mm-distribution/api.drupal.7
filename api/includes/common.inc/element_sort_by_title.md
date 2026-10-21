# element_sort_by_title()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6636–6640 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6636-L6640)

## Signature

```php
function element_sort_by_title($a, $b)
```

## Documentation

```text
Array sorting callback; sorts elements by title.
```

## Code

```php
function element_sort_by_title($a, $b) {
  $a_title = (is_array($a) && isset($a['#title'])) ? $a['#title'] : '';
  $b_title = (is_array($b) && isset($b['#title'])) ? $b['#title'] : '';
  return strnatcasecmp($a_title, $b_title);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
