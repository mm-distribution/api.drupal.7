# ThemeRegistryTestCase::testRaceCondition()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 575–605 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L575-L605)
- **Class:** [ThemeRegistryTestCase](../ThemeRegistryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRaceCondition()
```

## Documentation

```text
Tests the behavior of the theme registry class.
```

## Code

```php
  function testRaceCondition() {
    $_SERVER['REQUEST_METHOD'] = 'GET';
    $cid = 'test_theme_registry';

    // Directly instantiate the theme registry, this will cause a base cache
    // entry to be written in __construct().
    $registry = new ThemeRegistry($cid, 'cache');

    $this->assertTrue(cache_get($cid), 'Cache entry was created.');

    // Trigger a cache miss for an offset.
    $this->assertTrue($registry['theme_test_template_test'], 'Offset was returned correctly from the theme registry.');
    // This will cause the ThemeRegistry class to write an updated version of
    // the cache entry when it is destroyed, usually at the end of the request.
    // Before that happens, manually delete the cache entry we created earlier
    // so that the new entry is written from scratch.
    cache_clear_all($cid, 'cache');

    // Destroy the class so that it triggers a cache write for the offset.
    unset($registry);

    $this->assertTrue(cache_get($cid), 'Cache entry was created.');

    // Create a new instance of the class. Confirm that both the offset
    // requested previously, and one that has not yet been requested are both
    // available.
    $registry = new ThemeRegistry($cid, 'cache');

    $this->assertTrue($registry['theme_test_template_test'], 'Offset was returned correctly from the theme registry');
    $this->assertTrue($registry['theme_test_template_test_2'], 'Offset was returned correctly from the theme registry');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
