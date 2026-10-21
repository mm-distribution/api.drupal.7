# module_test_altered_test_hook()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.implementations.inc`](_file.md), lines 8–10 · [local source](../../../../../source/modules/simpletest/tests/module_test.implementations.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.implementations.inc#L8-L10)
- **Module/theme:** batch_test

## Signature

```php
function module_test_altered_test_hook()
```

## Documentation

```text
Implements hook_altered_test_hook()

@see module_test_module_implements_alter()
```

## Code

```php
function module_test_altered_test_hook() {
  return __FUNCTION__;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.implementations.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.implementations.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
