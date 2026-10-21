# trigger_test_generic_any_action()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 133–136 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L133-L136)
- **Module/theme:** trigger_test

## Signature

```php
function trigger_test_generic_any_action($context)
```

## Documentation

```text
Action fired during the additional trigger tests.
```

## Code

```php
function trigger_test_generic_any_action($context) {
  // Indicate successful execution by setting a persistent variable.
  variable_set('trigger_test_generic_any_action', variable_get('trigger_test_generic_any_action', 0) + 1);
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
