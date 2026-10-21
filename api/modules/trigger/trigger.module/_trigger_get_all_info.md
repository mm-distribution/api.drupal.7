# _trigger_get_all_info()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 640–649 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L640-L649)
- **Module/theme:** trigger

## Signature

```php
function _trigger_get_all_info()
```

## Documentation

```text
Retrieves and caches information from hook_trigger_info() implementations.

@return
  Array of all triggers.
```

## Code

```php
function _trigger_get_all_info() {
  $triggers = &drupal_static(__FUNCTION__);

  if (!isset($triggers)) {
    $triggers = module_invoke_all('trigger_info');
    drupal_alter('trigger_info', $triggers);
  }

  return $triggers;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
