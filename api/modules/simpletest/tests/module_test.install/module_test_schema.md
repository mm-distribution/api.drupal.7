# module_test_schema()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.install`](_file.md), lines 11–25 · [local source](../../../../../source/modules/simpletest/tests/module_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.install#L11-L25)
- **Module/theme:** batch_test
- **Implements:** [hook_schema()](../../../system/system.api.php/hook_schema.md)

## Signature

```php
function module_test_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function module_test_schema() {
  $schema['module_test'] = array(
    'description' => 'Dummy table to test the behavior of hook_schema() during module installation.',
    'fields' => array(
      'data' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'An example data column for the module.',
      ),
    ),
  );
  return $schema;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
