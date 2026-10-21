# update_theme()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 270–292 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L270-L292)
- **Module/theme:** update
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function update_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function update_theme() {
  return array(
    'update_manager_update_form' => array(
      'render element' => 'form',
      'file' => 'update.manager.inc',
    ),
    'update_last_check' => array(
      'variables' => array('last' => NULL),
    ),
    'update_report' => array(
      'variables' => array('data' => NULL),
      'file' => 'update.report.inc',
    ),
    'update_version' => array(
      'variables' => array('version' => NULL, 'tag' => NULL, 'class' => array()),
      'file' => 'update.report.inc',
    ),
    'update_status_label' => array(
      'variables' => array('status' => NULL),
      'file' => 'update.report.inc',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
