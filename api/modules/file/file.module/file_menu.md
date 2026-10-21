# file_menu()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 36–54 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L36-L54)
- **Module/theme:** file
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function file_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function file_menu() {
  $items = array();

  $items['file/ajax'] = array(
    'page callback' => 'file_ajax_upload',
    'delivery callback' => 'ajax_deliver',
    'access arguments' => array('access content'),
    'theme callback' => 'ajax_base_page_theme',
    'type' => MENU_CALLBACK,
  );
  $items['file/progress'] = array(
    'page callback' => 'file_ajax_progress',
    'access arguments' => array('access content'),
    'theme callback' => 'ajax_base_page_theme',
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
