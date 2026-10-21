# EarlyBootstrapTestCase::testHookBoot()

- **Type:** Method
- **File:** [`modules/simpletest/tests/boot.test`](../_file.md), lines 22–37 · [local source](../../../../../../source/modules/simpletest/tests/boot.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot.test#L22-L37)
- **Class:** [EarlyBootstrapTestCase](../EarlyBootstrapTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testHookBoot()
```

## Documentation

```text
Test hook_boot() on both regular and "early exit" pages.
```

## Code

```php
  public function testHookBoot() {
    $paths = array('', 'early_exit');
    foreach ($paths as $path) {
      // Empty the module_implements() caches.
      module_implements(NULL, FALSE, TRUE);
      // Do a request to the front page, which will call module_implements()
      // during hook_boot().
      $this->drupalGet($path);
      // Reset the static cache so we get implementation data from the persistent
      // cache.
      drupal_static_reset();
      // Make sure we get a full list of all modules implementing hook_help().
      $modules = module_implements('help');
      $this->assertTrue(in_array('boot_test_2', $modules));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/boot.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot.test) · Licensed GPL-2.0-or-later (see LICENSE)._
