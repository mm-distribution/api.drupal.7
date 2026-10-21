# _menu_link_parents_set()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3606–3619 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3606-L3619)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_link_parents_set(&$item, $parent)
```

## Documentation

```text
Sets the p1 through p9 values for a menu link being saved.
```

## Code

```php
function _menu_link_parents_set(&$item, $parent) {
  $i = 1;
  while ($i < $item['depth']) {
    $p = 'p' . $i++;
    $item[$p] = $parent[$p];
  }
  $p = 'p' . $i++;
  // The parent (p1 - p9) corresponding to the depth always equals the mlid.
  $item[$p] = $item['mlid'];
  while ($i <= MENU_MAX_DEPTH) {
    $p = 'p' . $i++;
    $item[$p] = 0;
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
