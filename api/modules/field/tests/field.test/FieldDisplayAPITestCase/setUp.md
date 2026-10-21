# FieldDisplayAPITestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2190–2232 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2190-L2232)
- **Class:** [FieldDisplayAPITestCase](../FieldDisplayAPITestCase.md)
- **Module/theme:** field_test_schema_alter

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

    // Create a field and instance.
    $this->field_name = 'test_field';
    $this->label = $this->randomName();
    $this->cardinality = 4;

    $this->field = array(
      'field_name' => $this->field_name,
      'type' => 'test_field',
      'cardinality' => $this->cardinality,
    );
    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'label' => $this->label,
      'display' => array(
        'default' => array(
          'type' => 'field_test_default',
          'settings' => array(
            'test_formatter_setting' => $this->randomName(),
          ),
        ),
        'teaser' => array(
          'type' => 'field_test_default',
          'settings' => array(
            'test_formatter_setting' => $this->randomName(),
          ),
        ),
      ),
    );
    field_create_field($this->field);
    field_create_instance($this->instance);

    // Create an entity with values.
    $this->values = $this->_generateTestFieldValues($this->cardinality);
    $this->entity = field_test_create_stub_entity();
    $this->is_new = TRUE;
    $this->entity->{$this->field_name}[LANGUAGE_NONE] = $this->values;
    field_test_entity_save($this->entity);
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
