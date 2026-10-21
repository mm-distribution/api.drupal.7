# UserRolesAssignmentTestCase::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2819–2823 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2819-L2823)
- **Class:** [UserRolesAssignmentTestCase](../UserRolesAssignmentTestCase.md)
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
    $this->admin_user = $this->drupalCreateUser(array('administer permissions', 'administer users'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
