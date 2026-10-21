# _trigger_tab_information()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 659–671 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L659-L671)
- **Module/theme:** trigger

## Signature

```php
function _trigger_tab_information()
```

## Documentation

```text
Gathers information about tabs on the triggers administration screen.

@return
  Array of modules that have triggers, with the keys being the
  machine-readable name of the module, and the values being the
  human-readable name of the module.
```

## Code

```php
function _trigger_tab_information() {
  // Gather information about all triggers and modules.
  $trigger_info = _trigger_get_all_info();
  $modules = system_get_info('module');
  $modules = array_intersect_key($modules, $trigger_info);

  $return_info = array();
  foreach ($modules as $name => $info) {
    $return_info[$name] = $info['name'];
  }

  return $return_info;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
