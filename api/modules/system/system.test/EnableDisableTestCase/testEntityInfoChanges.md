# EnableDisableTestCase::testEntityInfoChanges()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 277–293 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L277-L293)
- **Class:** [EnableDisableTestCase](../EnableDisableTestCase.md)
- **Module/theme:** system

## Signature

```php
function testEntityInfoChanges()
```

## Documentation

```text
Ensures entity info cache is updated after changes.
```

## Code

```php
  function testEntityInfoChanges() {
    module_enable(array('entity_cache_test'));
    $entity_info = entity_get_info();
    $this->assertTrue(isset($entity_info['entity_cache_test']), 'Test entity type found.');

    // Change the label of the test entity type and make sure changes appear
    // after flushing caches.
    variable_set('entity_cache_test_label', 'New label.');
    drupal_flush_all_caches();
    $info = entity_get_info('entity_cache_test');
    $this->assertEqual($info['label'], 'New label.', 'New label appears in entity info.');

    // Disable the providing module and make sure the entity type is gone.
    module_disable(array('entity_cache_test', 'entity_cache_test_dependency'));
    $entity_info = entity_get_info();
    $this->assertFalse(isset($entity_info['entity_cache_test']), 'Entity type of the providing module is gone.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
