# FileFieldAnonymousSubmission::setUp()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1786–1794 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1786-L1794)
- **Class:** [FileFieldAnonymousSubmission](../FileFieldAnonymousSubmission.md)
- **Module/theme:** file_module_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Allow node submissions by anonymous users.
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array(
      'create article content',
      'access content',
    ));
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
