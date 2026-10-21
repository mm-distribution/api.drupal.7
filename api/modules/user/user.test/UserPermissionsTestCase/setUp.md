# UserPermissionsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1690–1699 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1690-L1699)
- **Class:** [UserPermissionsTestCase](../UserPermissionsTestCase.md)
- **Module/theme:** user

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

    $this->admin_user = $this->drupalCreateUser(array('administer permissions', 'access user profiles', 'administer site configuration', 'administer modules', 'administer users'));

    // Find the new role ID - it must be the maximum.
    $all_rids = array_keys($this->admin_user->roles);
    sort($all_rids);
    $this->rid = array_pop($all_rids);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
