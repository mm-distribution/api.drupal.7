# EnableDisableTestCase::testEntityInfoCacheWatchdog()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 300–305 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L300-L305)
- **Class:** [EnableDisableTestCase](../EnableDisableTestCase.md)
- **Module/theme:** system

## Signature

```php
function testEntityInfoCacheWatchdog()
```

## Documentation

```text
Tests entity info cache after enabling a module with a dependency on an entity providing module.

@see entity_cache_test_watchdog()
```

## Code

```php
  function testEntityInfoCacheWatchdog() {
    module_enable(array('entity_cache_test'));
    $info = variable_get('entity_cache_test');
    $this->assertEqual($info['label'], 'Entity Cache Test', 'Entity info label is correct.');
    $this->assertEqual($info['controller class'], 'DrupalDefaultEntityController', 'Entity controller class info is correct.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
