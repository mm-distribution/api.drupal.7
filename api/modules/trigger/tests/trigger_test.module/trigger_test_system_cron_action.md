# trigger_test_system_cron_action()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 81–84 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L81-L84)
- **Module/theme:** trigger_test

## Signature

```php
function trigger_test_system_cron_action()
```

## Documentation

```text
Action fired during the "cron run" trigger test.
```

## Code

```php
function trigger_test_system_cron_action() {
  // Indicate successful execution by setting a persistent variable.
  variable_set('trigger_test_system_cron_action', TRUE);
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
