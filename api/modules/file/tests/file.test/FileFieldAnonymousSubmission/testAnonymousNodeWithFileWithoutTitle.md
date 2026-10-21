# FileFieldAnonymousSubmission::testAnonymousNodeWithFileWithoutTitle()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1865–1868 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1865-L1868)
- **Class:** [FileFieldAnonymousSubmission](../FileFieldAnonymousSubmission.md)
- **Module/theme:** file_module_test

## Signature

```php
function testAnonymousNodeWithFileWithoutTitle()
```

## Documentation

```text
Tests file submission for an anonymous visitor with a missing node title.
```

## Code

```php
  function testAnonymousNodeWithFileWithoutTitle() {
    $this->drupalLogout();
    $this->_testNodeWithFileWithoutTitle();
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
