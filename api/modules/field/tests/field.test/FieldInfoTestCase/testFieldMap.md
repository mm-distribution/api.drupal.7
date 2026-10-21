# FieldInfoTestCase::testFieldMap()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1496–1565 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1496-L1565)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldMap()
```

## Documentation

```text
Test field_info_field_map().
```

## Code

```php
  function testFieldMap() {
    // We will overlook fields created by the 'standard' install profile.
    $exclude = field_info_field_map();

    // Create a new bundle for 'test_entity' entity type.
    field_test_create_bundle('test_bundle_2');

    // Create a couple fields.
    $fields  = array(
      array(
        'field_name' => 'field_1',
        'type' => 'test_field',
      ),
      array(
        'field_name' => 'field_2',
        'type' => 'hidden_test_field',
      ),
    );
    foreach ($fields as $field) {
      field_create_field($field);
    }

    // Create a couple instances.
    $instances = array(
      array(
        'field_name' => 'field_1',
        'entity_type' => 'test_entity',
        'bundle' => 'test_bundle',
      ),
      array(
        'field_name' => 'field_1',
        'entity_type' => 'test_entity',
        'bundle' => 'test_bundle_2',
      ),
      array(
        'field_name' => 'field_2',
        'entity_type' => 'test_entity',
        'bundle' => 'test_bundle',
      ),
      array(
        'field_name' => 'field_2',
        'entity_type' => 'test_cacheable_entity',
        'bundle' => 'test_bundle',
      ),
    );
    foreach ($instances as $instance) {
      field_create_instance($instance);
    }

    $expected = array(
      'field_1' => array(
        'type' => 'test_field',
        'bundles' => array(
          'test_entity' => array('test_bundle', 'test_bundle_2'),
        ),
      ),
      'field_2' => array(
        'type' => 'hidden_test_field',
        'bundles' => array(
          'test_entity' => array('test_bundle'),
          'test_cacheable_entity' => array('test_bundle'),
        ),
      ),
    );

    // Check that the field map is correct.
    $map = field_info_field_map();
    $map = array_diff_key($map, $exclude);
    $this->assertEqual($map, $expected);
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
