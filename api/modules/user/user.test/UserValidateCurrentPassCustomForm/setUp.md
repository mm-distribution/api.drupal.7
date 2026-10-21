# UserValidateCurrentPassCustomForm::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2981–2986 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2981-L2986)
- **Class:** [UserValidateCurrentPassCustomForm](../UserValidateCurrentPassCustomForm.md)
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
    parent::setUp('user_form_test');
    // Create two users
    $this->accessUser = $this->drupalCreateUser(array('access content'));
    $this->adminUser = $this->drupalCreateUser(array('administer users'));
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
