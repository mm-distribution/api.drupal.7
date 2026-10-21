# UrlAlterFunctionalTest::testGetQInitialized()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 206–209 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L206-L209)
- **Class:** [UrlAlterFunctionalTest](../UrlAlterFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetQInitialized()
```

## Documentation

```text
Tests that $_GET['q'] is initialized when the request path is empty.
```

## Code

```php
  function testGetQInitialized() {
    $this->drupalGet('');
    $this->assertText("\$_GET['q'] is non-empty with an empty request path.", "\$_GET['q'] is initialized with an empty request path.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
