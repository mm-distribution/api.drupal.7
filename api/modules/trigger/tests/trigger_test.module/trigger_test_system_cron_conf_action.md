# trigger_test_system_cron_conf_action()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 89–93 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L89-L93)
- **Module/theme:** trigger_test

## Signature

```php
function trigger_test_system_cron_conf_action($object, $context)
```

## Documentation

```text
Implement a configurable Drupal action.
```

## Code

```php
function trigger_test_system_cron_conf_action($object, $context) {
  // Indicate successful execution by incrementing a persistent variable.
  $value = variable_get('trigger_test_system_cron_conf_action', 0) + 1;
  variable_set('trigger_test_system_cron_conf_action', $value);
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
