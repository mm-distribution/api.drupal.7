# UserPasswordResetTestCase::getConfirmURL()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 560–566 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L560-L566)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
public function getConfirmURL($reset_url)
```

## Documentation

```text
Turns a password reset URL into a 'confirm' URL.
```

## Code

```php
  public function getConfirmURL($reset_url) {
    // Last part is always the hash; replace with "confirm".
    $parts = explode('/', $reset_url);
    array_pop($parts);
    array_push($parts, 'confirm');
    return implode('/', $parts);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
