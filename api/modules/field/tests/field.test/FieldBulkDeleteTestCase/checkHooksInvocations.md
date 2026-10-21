# FieldBulkDeleteTestCase::checkHooksInvocations()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3563–3582 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3563-L3582)
- **Class:** [FieldBulkDeleteTestCase](../FieldBulkDeleteTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function checkHooksInvocations($expected_hooks, $actual_hooks)
```

## Documentation

```text
Tests that the expected hooks have been invoked on the expected entities.

@param $expected_hooks
  An array keyed by hook name, with one entry per expected invocation.
  Each entry is the value of the "$entity" parameter the hook is expected
  to have been passed.
@param $actual_hooks
  The array of actual hook invocations recorded by field_test_memorize().
```

## Code

```php
  function checkHooksInvocations($expected_hooks, $actual_hooks) {
    foreach ($expected_hooks as $hook => $invocations) {
      $actual_invocations = $actual_hooks[$hook];

      // Check that the number of invocations is correct.
      $this->assertEqual(count($actual_invocations), count($invocations), "$hook() was called the expected number of times.");

      // Check that the hook was called for each expected argument.
      foreach ($invocations as $argument) {
        $found = FALSE;
        foreach ($actual_invocations as $actual_arguments) {
          if ($actual_arguments[1] == $argument) {
            $found = TRUE;
            break;
          }
        }
        $this->assertTrue($found, "$hook() was called on expected argument");
      }
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
