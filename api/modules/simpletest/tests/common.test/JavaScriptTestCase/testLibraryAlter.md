# JavaScriptTestCase::testLibraryAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1966–1975 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1966-L1975)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLibraryAlter()
```

## Documentation

```text
Adds a JavaScript library to the page and alters it.

@see common_test_library_alter()
```

## Code

```php
  function testLibraryAlter() {
    // Verify that common_test altered the title of Farbtastic.
    $library = drupal_get_library('system', 'farbtastic');
    $this->assertEqual($library['title'], 'Farbtastic: Altered Library', 'Registered libraries were altered.');

    // common_test_library_alter() also added a dependency on jQuery Form.
    drupal_add_library('system', 'farbtastic');
    $scripts = drupal_get_js();
    $this->assertTrue(strpos($scripts, 'misc/jquery.form.js'), 'Altered library dependencies are added to the page.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
