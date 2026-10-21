# EntityPropertiesTestCase::testEntityKeys()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3883–3890 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3883-L3890)
- **Class:** [EntityPropertiesTestCase](../EntityPropertiesTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testEntityKeys()
```

## Documentation

```text
Tests entity_extract_ids() with an empty entity info.
```

## Code

```php
  function testEntityKeys(){
    $entity_type = 'test_entity2';
    $entity = field_test_create_stub_entity();
    list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

    $this->assertNull($id, 'Entity id for test_entity2 returned NULL.');
    $this->assertNull($vid, 'Entity vid for test_entity2 returned NULL.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
