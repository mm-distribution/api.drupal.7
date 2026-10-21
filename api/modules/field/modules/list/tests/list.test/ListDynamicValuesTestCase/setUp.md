# ListDynamicValuesTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 130–163 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L130-L163)
- **Class:** [ListDynamicValuesTestCase](../ListDynamicValuesTestCase.md)
- **Module/theme:** list_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('list', 'field_test', 'list_test'));

    $this->field_name = 'test_list';
    $this->field = array(
      'field_name' => $this->field_name,
      'type' => 'list_text',
      'cardinality' => 1,
      'settings' => array(
        'allowed_values_function' => 'list_test_dynamic_values_callback',
      ),
    );
    $this->field = field_create_field($this->field);

    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'required' => TRUE,
      'widget' => array(
        'type' => 'options_select',
      ),
    );
    $this->instance = field_create_instance($this->instance);
    $this->test = array(
      'id' => mt_rand(1, 10),
      // Make sure this does not equal the ID so that
      // list_test_dynamic_values_callback() always returns 4 values.
      'vid' => mt_rand(20, 30),
      'bundle' => 'test_bundle',
      'label' => $this->randomName(),
    );
    $this->entity = call_user_func_array('field_test_create_stub_entity', $this->test);
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
