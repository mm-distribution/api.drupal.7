# FormsArbitraryRebuildTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2112–2135 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2112-L2135)
- **Class:** [FormsArbitraryRebuildTestCase](../FormsArbitraryRebuildTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('form_test');
    // Auto-create a field for testing.
    $field = array(
      'field_name' => 'test_multiple',
      'type' => 'text',
      'cardinality' => -1,
      'translatable' => FALSE,
    );
    field_create_field($field);

    $instance = array(
      'entity_type' => 'node',
      'field_name' => 'test_multiple',
      'bundle' => 'page',
      'label' => 'Test a multiple valued field',
      'widget' => array(
        'type' => 'text_textfield',
        'weight' => 0,
      ),
    );
    field_create_instance($instance);
    variable_set('user_register', USER_REGISTER_VISITORS);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
