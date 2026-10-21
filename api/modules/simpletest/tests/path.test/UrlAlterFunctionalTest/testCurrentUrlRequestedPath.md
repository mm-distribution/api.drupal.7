# UrlAlterFunctionalTest::testCurrentUrlRequestedPath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 197–201 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L197-L201)
- **Class:** [UrlAlterFunctionalTest](../UrlAlterFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testCurrentUrlRequestedPath()
```

## Documentation

```text
Test current_path() and request_path().
```

## Code

```php
  function testCurrentUrlRequestedPath() {
    $this->drupalGet('url-alter-test/bar');
    $this->assertRaw('request_path=url-alter-test/bar', 'request_path() returns the requested path.');
    $this->assertRaw('current_path=url-alter-test/foo', 'current_path() returns the internal path.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
