# JavaScriptTestCase::testGetLibrary()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2014–2029 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2014-L2029)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetLibrary()
```

## Documentation

```text
Tests retrieval of libraries via drupal_get_library().
```

## Code

```php
  function testGetLibrary() {
    // Retrieve all libraries registered by a module.
    $libraries = drupal_get_library('common_test');
    $this->assertTrue(isset($libraries['farbtastic']), 'Retrieved all module libraries.');
    // Retrieve all libraries for a module not implementing hook_library().
    // Note: This test installs Locale module.
    $libraries = drupal_get_library('locale');
    $this->assertEqual($libraries, array(), 'Retrieving libraries from a module not implementing hook_library() returns an emtpy array.');

    // Retrieve a specific library by module and name.
    $farbtastic = drupal_get_library('common_test', 'farbtastic');
    $this->assertEqual($farbtastic['version'], '5.3', 'Retrieved a single library.');
    // Retrieve a non-existing library by module and name.
    $farbtastic = drupal_get_library('common_test', 'foo');
    $this->assertIdentical($farbtastic, FALSE, 'Retrieving a non-existing library returns FALSE.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
