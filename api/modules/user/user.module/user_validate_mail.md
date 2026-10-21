# user_validate_mail()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 677–684 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L677-L684)
- **Module/theme:** user

## Signature

```php
function user_validate_mail($mail)
```

## Documentation

```text
Validates a user's email address.

Checks that a user's email address exists and follows all standard
validation rules. Returns error messages when the address is invalid.

@param $mail
  A user's email address.

@return
  If the address is invalid, a human-readable error message is returned.
  If the address is valid, nothing is returned.
```

## Code

```php
function user_validate_mail($mail) {
  if (!$mail) {
    return t('You must enter an e-mail address.');
  }
  if (!valid_email_address($mail)) {
    return t('The e-mail address %mail is not valid.', array('%mail' => $mail));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
