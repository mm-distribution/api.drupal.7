# translation_menu()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 57–70 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L57-L70)
- **Module/theme:** translation
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function translation_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function translation_menu() {
  $items = array();
  $items['node/%node/translate'] = array(
    'title' => 'Translate',
    'page callback' => 'translation_node_overview',
    'page arguments' => array(1),
    'access callback' => '_translation_tab_access',
    'access arguments' => array(1),
    'type' => MENU_LOCAL_TASK,
    'weight' => 2,
    'file' => 'translation.pages.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
