# menu_get_names()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1800–1811 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1800-L1811)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_names()
```

## Documentation

```text
Build a list of named menus.
```

## Code

```php
function menu_get_names() {
  $names = &drupal_static(__FUNCTION__);

  if (empty($names)) {
    $names = db_select('menu_links')
      ->distinct()
      ->fields('menu_links', array('menu_name'))
      ->orderBy('menu_name')
      ->execute()->fetchCol();
  }
  return $names;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
