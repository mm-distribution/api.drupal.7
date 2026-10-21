# ProfileTestCase::setUp()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 15–23 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L15-L23)
- **Class:** [ProfileTestCase](../ProfileTestCase.md)
- **Module/theme:** profile

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('profile');
    variable_set('user_register', USER_REGISTER_VISITORS);

    $this->admin_user = $this->drupalCreateUser(array('administer users', 'access user profiles', 'administer blocks'));

    // This is the user whose profile will be edited.
    $this->normal_user = $this->drupalCreateUser();
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
