# drupal_sort_title()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6710–6718 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6710-L6718)

## Signature

```php
function drupal_sort_title($a, $b)
```

## Documentation

```text
Array sorting callback; sorts elements by 'title' key.
```

## Code

```php
function drupal_sort_title($a, $b) {
  if (!isset($b['title'])) {
    return -1;
  }
  if (!isset($a['title'])) {
    return 1;
  }
  return strcasecmp($a['title'], $b['title']);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
