# FieldTranslationsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3166–3194 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3166-L3194)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
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
    parent::setUp('locale', 'field_test');

    $this->field_name = drupal_strtolower($this->randomName() . '_field_name');

    $this->entity_type = 'test_entity';

    $field = array(
      'field_name' => $this->field_name,
      'type' => 'test_field',
      'cardinality' => 4,
      'translatable' => TRUE,
    );
    field_create_field($field);
    $this->field = field_read_field($this->field_name);

    $instance = array(
      'field_name' => $this->field_name,
      'entity_type' => $this->entity_type,
      'bundle' => 'test_bundle',
    );
    field_create_instance($instance);
    $this->instance = field_read_instance('test_entity', $this->field_name, 'test_bundle');

    require_once DRUPAL_ROOT . '/includes/locale.inc';
    for ($i = 0; $i < 3; ++$i) {
      locale_add_language('l' . $i, $this->randomString(), $this->randomString());
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
