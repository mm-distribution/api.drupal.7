# AccessDeniedTestCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1060–1065 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1060-L1065)
- **Class:** [AccessDeniedTestCase](../AccessDeniedTestCase.md)
- **Module/theme:** system

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

    // Create an administrative user.
    $this->admin_user = $this->drupalCreateUser(array('access administration pages', 'administer site configuration', 'administer blocks'));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
