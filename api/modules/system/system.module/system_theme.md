# system_theme()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 159–214 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L159-L214)
- **Module/theme:** system
- **Implements:** [hook_theme()](../system.api.php/hook_theme.md)

## Signature

```php
function system_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function system_theme() {
  return array_merge(drupal_common_theme(), array(
    'system_themes_page' => array(
      'variables' => array('theme_groups' => NULL),
      'file' => 'system.admin.inc',
    ),
    'system_settings_form' => array(
      'render element' => 'form',
    ),
    'confirm_form' => array(
      'render element' => 'form',
    ),
    'system_modules_fieldset' => array(
      'render element' => 'form',
      'file' => 'system.admin.inc',
    ),
    'system_modules_incompatible' => array(
      'variables' => array('message' => NULL),
      'file' => 'system.admin.inc',
    ),
    'system_modules_uninstall' => array(
      'render element' => 'form',
      'file' => 'system.admin.inc',
    ),
    'status_report' => array(
      'render element' => 'requirements',
      'file' => 'system.admin.inc',
    ),
    'admin_page' => array(
      'variables' => array('blocks' => NULL),
      'file' => 'system.admin.inc',
    ),
    'admin_block' => array(
      'variables' => array('block' => NULL),
      'file' => 'system.admin.inc',
    ),
    'admin_block_content' => array(
      'variables' => array('content' => NULL),
      'file' => 'system.admin.inc',
    ),
    'system_admin_index' => array(
      'variables' => array('menu_items' => NULL),
      'file' => 'system.admin.inc',
    ),
    'system_powered_by' => array(
      'variables' => array(),
    ),
    'system_compact_link' => array(
      'variables' => array(),
    ),
    'system_date_time_settings' => array(
      'render element' => 'form',
      'file' => 'system.admin.inc',
    ),
  ));
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
