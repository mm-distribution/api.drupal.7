# FieldAttachOtherTestCase::testFieldAttachCache()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 941–1025 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L941-L1025)
- **Class:** [FieldAttachOtherTestCase](../FieldAttachOtherTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachCache()
```

## Documentation

```text
Test field cache.
```

## Code

```php
  function testFieldAttachCache() {
    // Initialize random values and a test entity.
    $entity_init = field_test_create_stub_entity(1, 1, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;
    $values = $this->_generateTestFieldValues($this->field['cardinality']);

    // Non-cacheable entity type.
    $entity_type = 'test_entity';
    $cid = "field:$entity_type:{$entity_init->ftid}";

    // Check that no initial cache entry is present.
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Non-cached: no initial cache entry');

    // Save, and check that no cache entry is present.
    $entity = clone($entity_init);
    $entity->{$this->field_name}[$langcode] = $values;
    field_attach_insert($entity_type, $entity);
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Non-cached: no cache entry on insert');

    // Load, and check that no cache entry is present.
    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Non-cached: no cache entry on load');


    // Cacheable entity type.
    $entity_type = 'test_cacheable_entity';
    $cid = "field:$entity_type:{$entity_init->ftid}";
    $instance = $this->instance;
    $instance['entity_type'] = $entity_type;
    field_create_instance($instance);

    // Check that no initial cache entry is present.
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Cached: no initial cache entry');

    // Save, and check that no cache entry is present.
    $entity = clone($entity_init);
    $entity->{$this->field_name}[$langcode] = $values;
    field_attach_insert($entity_type, $entity);
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Cached: no cache entry on insert');

    // Load a single field, and check that no cache entry is present.
    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity), FIELD_LOAD_CURRENT, array('field_id' => $this->field_id));
    $cache = cache_get($cid, 'cache_field');
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Cached: no cache entry on loading a single field');

    // Load, and check that a cache entry is present with the expected values.
    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $cache = cache_get($cid, 'cache_field');
    $this->assertEqual($cache->data[$this->field_name][$langcode], $values, 'Cached: correct cache entry on load');

    // Update with different values, and check that the cache entry is wiped.
    $values = $this->_generateTestFieldValues($this->field['cardinality']);
    $entity = clone($entity_init);
    $entity->{$this->field_name}[$langcode] = $values;
    field_attach_update($entity_type, $entity);
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Cached: no cache entry on update');

    // Load, and check that a cache entry is present with the expected values.
    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $cache = cache_get($cid, 'cache_field');
    $this->assertEqual($cache->data[$this->field_name][$langcode], $values, 'Cached: correct cache entry on load');

    // Create a new revision, and check that the cache entry is wiped.
    $entity_init = field_test_create_stub_entity(1, 2, $this->instance['bundle']);
    $values = $this->_generateTestFieldValues($this->field['cardinality']);
    $entity = clone($entity_init);
    $entity->{$this->field_name}[$langcode] = $values;
    field_attach_update($entity_type, $entity);
    $cache = cache_get($cid, 'cache_field');
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Cached: no cache entry on new revision creation');

    // Load, and check that a cache entry is present with the expected values.
    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $cache = cache_get($cid, 'cache_field');
    $this->assertEqual($cache->data[$this->field_name][$langcode], $values, 'Cached: correct cache entry on load');

    // Delete, and check that the cache entry is wiped.
    field_attach_delete($entity_type, $entity);
    $this->assertFalse(cache_get($cid, 'cache_field'), 'Cached: no cache entry after delete');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
