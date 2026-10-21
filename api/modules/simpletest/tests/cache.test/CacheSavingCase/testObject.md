# CacheSavingCase::testObject()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 143–152 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L143-L152)
- **Class:** [CacheSavingCase](../CacheSavingCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testObject()
```

## Documentation

```text
Test the saving and restoring of an object.
```

## Code

```php
  function testObject() {
    $test_object = new stdClass();
    $test_object->test1 = $this->randomName(100);
    $test_object->test2 = 100;
    $test_object->test3 = array('drupal1', 'drupal2' => 'drupal3', 'drupal4' => array('drupal5', 'drupal6'));

    cache_set('test_object', $test_object, 'cache');
    $cache = cache_get('test_object', 'cache');
    $this->assertTrue(isset($cache->data) && $cache->data == $test_object, 'Object is saved and restored properly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
