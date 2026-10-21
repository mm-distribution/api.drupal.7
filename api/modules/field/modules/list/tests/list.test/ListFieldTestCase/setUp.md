# ListFieldTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 24–47 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L24-L47)
- **Class:** [ListFieldTestCase](../ListFieldTestCase.md)
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
    parent::setUp('field_test');

    $this->field_name = 'test_list';
    $this->field = array(
      'field_name' => $this->field_name,
      'type' => 'list_integer',
      'cardinality' => 1,
      'settings' => array(
        'allowed_values' => array(1 => 'One', 2 => 'Two', 3 => 'Three'),
      ),
    );
    $this->field = field_create_field($this->field);

    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'options_buttons',
      ),
    );
    $this->instance = field_create_instance($this->instance);
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
