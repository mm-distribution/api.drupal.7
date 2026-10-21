# trigger_theme()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 201–208 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L201-L208)
- **Module/theme:** trigger
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function trigger_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function trigger_theme() {
  return array(
    'trigger_display' => array(
      'render element' => 'element',
      'file' => 'trigger.admin.inc',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
