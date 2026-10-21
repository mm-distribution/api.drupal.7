# toolbar_menu()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 57–65 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L57-L65)
- **Module/theme:** toolbar
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function toolbar_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function toolbar_menu() {
  $items['toolbar/toggle'] = array(
    'title' => 'Toggle drawer visibility',
    'type' => MENU_CALLBACK,
    'page callback' => 'toolbar_toggle_page',
    'access arguments' => array('access toolbar'),
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
