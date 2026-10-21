# UserPasswordResetTestCase::generateResetURL()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 553–555 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L553-L555)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
public function generateResetURL($account, $bypass_form = FALSE)
```

## Documentation

```text
Generates login link.
```

## Code

```php
  public function generateResetURL($account, $bypass_form = FALSE) {
    return user_pass_reset_url($account) . ($bypass_form ? '/login' : '');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
