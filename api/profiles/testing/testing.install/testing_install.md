# testing_install()

- **Type:** Function
- **File:** [`profiles/testing/testing.install`](_file.md), lines 14–21 · [local source](../../../../source/profiles/testing/testing.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/profiles/testing/testing.install#L14-L21)
- **Module/theme:** testing
- **Implements:** [hook_install()](../../../modules/system/system.api.php/hook_install.md)

## Signature

```php
function testing_install()
```

## Documentation

```text
Implements hook_install().

Perform actions to set up the site for this profile.

@see system_install()
```

## Code

```php
function testing_install() {
  // Allow visitor account creation, but with administrative approval.
  variable_set('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL);

  // Enable default permissions for system roles.
  user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access content'));
  user_role_grant_permissions(DRUPAL_AUTHENTICATED_RID, array('access content'));
}
```

---
_Drupal 7.103 · [profiles/testing/testing.install](https://github.com/drupal/drupal/blob/7.103/profiles/testing/testing.install) · Licensed GPL-2.0-or-later (see LICENSE)._
