# contact_update_7002()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 136–147 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L136-L147)
- **Module/theme:** contact
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function contact_update_7002()
```

## Documentation

```text
Enable the 'access user contact forms' for registered users by default.
```

## Code

```php
function contact_update_7002() {
  // Do not use user_role_grant_permission() since it relies on
  // hook_permission(), which will not run for contact module if it is
  // disabled.
  db_merge('role_permission')
    ->key(array(
      'rid' => DRUPAL_AUTHENTICATED_RID,
      'permission' => 'access user contact forms',
      'module' => 'contact',
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
