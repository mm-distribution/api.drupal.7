# _menu_check_rebuild()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2748–2758 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2748-L2758)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_check_rebuild()
```

## Documentation

```text
Checks whether a menu_rebuild() is necessary.
```

## Code

```php
function _menu_check_rebuild() {
  // To absolutely ensure that the menu rebuild is required, re-load the
  // variables in case they were set by another process.
  $variables = variable_initialize();
  if (empty($variables['menu_rebuild_needed']) && !empty($variables['menu_masks'])) {
    unset($GLOBALS['conf']['menu_rebuild_needed']);
    $GLOBALS['conf']['menu_masks'] = $variables['menu_masks'];
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
