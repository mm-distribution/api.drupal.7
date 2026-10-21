# module_test_test_hook()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.file.inc`](_file.md), lines 11–13 · [local source](../../../../../source/modules/simpletest/tests/module_test.file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.file.inc#L11-L13)
- **Module/theme:** batch_test

## Signature

```php
function module_test_test_hook()
```

## Documentation

```text
Implements hook_test_hook().
```

## Code

```php
function module_test_test_hook() {
  return array('module_test' => 'success!');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.file.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
