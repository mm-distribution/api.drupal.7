# trigger_forms()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 215–225 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L215-L225)
- **Module/theme:** trigger
- **Implements:** [hook_forms()](../../system/system.api.php/hook_forms.md)

## Signature

```php
function trigger_forms()
```

## Documentation

```text
Implements hook_forms().

We re-use code by using the same assignment form definition for each hook.
```

## Code

```php
function trigger_forms() {
  $trigger_info = _trigger_get_all_info();
  $forms = array();
  foreach ($trigger_info as $module => $hooks) {
    foreach ($hooks as $hook => $description) {
      $forms['trigger_' . $hook . '_assign_form'] = array('callback' => 'trigger_assign_form');
    }
  }

  return $forms;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
