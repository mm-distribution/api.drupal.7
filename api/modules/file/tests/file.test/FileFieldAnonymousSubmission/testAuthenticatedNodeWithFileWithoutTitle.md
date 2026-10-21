# FileFieldAnonymousSubmission::testAuthenticatedNodeWithFileWithoutTitle()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1873–1881 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1873-L1881)
- **Class:** [FileFieldAnonymousSubmission](../FileFieldAnonymousSubmission.md)
- **Module/theme:** file_module_test

## Signature

```php
function testAuthenticatedNodeWithFileWithoutTitle()
```

## Documentation

```text
Tests file submission for an authenticated user with a missing node title.
```

## Code

```php
  function testAuthenticatedNodeWithFileWithoutTitle() {
    $admin_user = $this->drupalCreateUser(array(
      'bypass node access',
      'access content overview',
      'administer nodes',
    ));
    $this->drupalLogin($admin_user);
    $this->_testNodeWithFileWithoutTitle();
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
