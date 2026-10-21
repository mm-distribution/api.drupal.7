# menu_set_custom_theme()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1793–1795 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1793-L1795)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_set_custom_theme()
```

## Documentation

```text
Sets a custom theme for the current page, if there is one.
```

## Code

```php
function menu_set_custom_theme() {
  menu_get_custom_theme(TRUE);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
