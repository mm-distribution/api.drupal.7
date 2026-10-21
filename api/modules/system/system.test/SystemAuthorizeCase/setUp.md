# SystemAuthorizeCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2971–2979 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2971-L2979)
- **Class:** [SystemAuthorizeCase](../SystemAuthorizeCase.md)
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
    parent::setUp(array('system_test'));

    variable_set('allow_authorize_operations', TRUE);

    // Create an administrator user.
    $this->admin_user = $this->drupalCreateUser(array('administer software updates'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
