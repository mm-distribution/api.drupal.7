# module_test_enable()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.install`](_file.md), lines 38–41 · [local source](../../../../../source/modules/simpletest/tests/module_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.install#L38-L41)
- **Module/theme:** batch_test
- **Implements:** [hook_enable()](../../../system/system.api.php/hook_enable.md)

## Signature

```php
function module_test_enable()
```

## Documentation

```text
Implements hook_enable().
```

## Code

```php
function module_test_enable() {
  $record = array('data' => 'Data inserted in hook_enable()');
  drupal_write_record('module_test', $record);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
