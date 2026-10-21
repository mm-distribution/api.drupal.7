# module_test_install()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.install`](_file.md), lines 30–33 · [local source](../../../../../source/modules/simpletest/tests/module_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.install#L30-L33)
- **Module/theme:** batch_test
- **Implements:** [hook_install()](../../../system/system.api.php/hook_install.md)

## Signature

```php
function module_test_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function module_test_install() {
  $record = array('data' => 'Data inserted in hook_install()');
  drupal_write_record('module_test', $record);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
