# EntityPropertiesTestCase::testEntityLabel()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3852–3878 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3852-L3878)
- **Class:** [EntityPropertiesTestCase](../EntityPropertiesTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testEntityLabel()
```

## Documentation

```text
Tests label key and label callback of an entity.
```

## Code

```php
  function testEntityLabel() {
    $entity_types = array(
      'test_entity_no_label',
      'test_entity_label',
      'test_entity_label_callback',
    );

    $entity = field_test_create_stub_entity();

    foreach ($entity_types as $entity_type) {
      $label = entity_label($entity_type, $entity);

      switch ($entity_type) {
        case 'test_entity_no_label':
          $this->assertFalse($label, 'Entity with no label property or callback returned FALSE.');
          break;

        case 'test_entity_label':
          $this->assertEqual($label, $entity->ftlabel, 'Entity with label key returned correct label.');
          break;

        case 'test_entity_label_callback':
          $this->assertEqual($label, 'label callback ' . $entity->ftlabel, 'Entity with label callback returned correct label.');
          break;
      }
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
