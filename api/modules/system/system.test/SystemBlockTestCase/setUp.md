# SystemBlockTestCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1756–1762 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1756-L1762)
- **Class:** [SystemBlockTestCase](../SystemBlockTestCase.md)
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
    parent::setUp('block');

    // Create and login user
    $admin_user = $this->drupalCreateUser(array('administer blocks', 'access administration pages'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
