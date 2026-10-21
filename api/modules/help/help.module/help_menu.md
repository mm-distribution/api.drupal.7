# help_menu()

- **Type:** Function
- **File:** [`modules/help/help.module`](_file.md), lines 11–33 · [local source](../../../../source/modules/help/help.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.module#L11-L33)
- **Module/theme:** help
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function help_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function help_menu() {
  $items['admin/help'] = array(
    'title' => 'Help',
    'description' => 'Reference for usage, configuration, and modules.',
    'page callback' => 'help_main',
    'access arguments' => array('access administration pages'),
    'weight' => 9,
    'file' => 'help.admin.inc',
  );

  foreach (module_implements('help', TRUE) as $module) {
    $items['admin/help/' . $module] = array(
      'title' => $module,
      'page callback' => 'help_page',
      'page arguments' => array(2),
      'access arguments' => array('access administration pages'),
      'type' => MENU_VISIBLE_IN_BREADCRUMB,
      'file' => 'help.admin.inc',
    );
  }

  return $items;
}
```

---
_Drupal 7.103 · [modules/help/help.module](https://github.com/drupal/drupal/blob/7.103/modules/help/help.module) · Licensed GPL-2.0-or-later (see LICENSE)._
