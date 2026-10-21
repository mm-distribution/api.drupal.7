# trigger_assign()

- **Type:** Function
- **File:** [`modules/trigger/trigger.admin.inc`](_file.md), lines 20–39 · [local source](../../../../source/modules/trigger/trigger.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc#L20-L39)
- **Module/theme:** trigger

## Signature

```php
function trigger_assign($module_to_display = NULL)
```

## Documentation

```text
Builds a form that allows users to assign actions to triggers.

@param $module_to_display
  Which tab of triggers to display. E.g., 'node' for all node-related
  triggers.

@return
  HTML form.

@see trigger_menu()
```

## Code

```php
function trigger_assign($module_to_display = NULL) {
  // If no type is specified we default to node actions, since they
  // are the most common.
  if (!isset($module_to_display)) {
    drupal_goto('admin/structure/trigger/node');
  }

  $build = array();
  $trigger_info = module_invoke_all('trigger_info');
  drupal_alter('trigger_info', $trigger_info);
  foreach ($trigger_info as $module => $hooks) {
    if ($module == $module_to_display) {
      foreach ($hooks as $hook => $description) {
        $form_id = 'trigger_' . $hook . '_assign_form';
        $build[$form_id] = drupal_get_form($form_id, $module, $hook, $description['label']);
      }
    }
  }
  return $build;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
