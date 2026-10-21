# JavaScriptTestCase::testAddFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1564–1572 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1564-L1572)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddFile()
```

## Documentation

```text
Test adding a JavaScript file.
```

## Code

```php
  function testAddFile() {
    $javascript = drupal_add_js('misc/collapse.js');
    $this->assertTrue(array_key_exists('misc/jquery.js', $javascript), 'jQuery is added when a file is added.');
    $this->assertTrue(array_key_exists('misc/drupal.js', $javascript), 'Drupal.js is added when file is added.');
    $this->assertTrue(array_key_exists('misc/collapse.js', $javascript), 'JavaScript files are correctly added.');
    $this->assertEqual(base_path(), $javascript['settings']['data'][0]['basePath'], 'Base path JavaScript setting is correctly set.');
    url('', array('prefix' => &$prefix));
    $this->assertEqual(empty($prefix) ? '' : $prefix, $javascript['settings']['data'][1]['pathPrefix'], 'Path prefix JavaScript setting is correctly set.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
