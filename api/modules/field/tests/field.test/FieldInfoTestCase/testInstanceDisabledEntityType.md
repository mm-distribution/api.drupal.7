# FieldInfoTestCase::testInstanceDisabledEntityType()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1473–1491 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1473-L1491)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testInstanceDisabledEntityType()
```

## Documentation

```text
Test that instances on disabled entity types are filtered out.
```

## Code

```php
  function testInstanceDisabledEntityType() {
    // For this test the field type and the entity type must be exposed by
    // different modules.
    $field_definition = array(
      'field_name' => 'field',
      'type' => 'test_field',
    );
    field_create_field($field_definition);
    $instance_definition = array(
      'field_name' => 'field',
      'entity_type' => 'comment',
      'bundle' => 'comment_node_article',
    );
    field_create_instance($instance_definition);

    // Disable coment module. This clears field_info cache.
    module_disable(array('comment'));
    $this->assertNull(field_info_instance('comment', 'field', 'comment_node_article'), 'No instances are returned on disabled entity types.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
