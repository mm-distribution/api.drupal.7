# menu_list_system_menus()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1816–1823 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1816-L1823)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_list_system_menus()
```

## Documentation

```text
Returns an array containing the names of system-defined (default) menus.
```

## Code

```php
function menu_list_system_menus() {
  return array(
    'navigation' => 'Navigation',
    'management' => 'Management',
    'user-menu' => 'User menu',
    'main-menu' => 'Main menu',
  );
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
