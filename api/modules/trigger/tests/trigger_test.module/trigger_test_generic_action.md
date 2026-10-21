# trigger_test_generic_action()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 125–128 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L125-L128)
- **Module/theme:** trigger_test

## Signature

```php
function trigger_test_generic_action($context)
```

## Documentation

```text
Action fired during the "taxonomy", "comment", and "user" trigger tests.
```

## Code

```php
function trigger_test_generic_action($context) {
  // Indicate successful execution by setting a persistent variable.
  variable_set('trigger_test_generic_action', TRUE);
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
