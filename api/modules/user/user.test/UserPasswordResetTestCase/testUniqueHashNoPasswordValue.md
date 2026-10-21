# UserPasswordResetTestCase::testUniqueHashNoPasswordValue()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 938–958 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L938-L958)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUniqueHashNoPasswordValue()
```

## Documentation

```text
Test uniqueness of output from user_pass_rehash() with no passwords.
```

## Code

```php
  function testUniqueHashNoPasswordValue() {
    $timestamp = REQUEST_TIME;

    // Minimal user objects are sufficient.
    $user = drupal_anonymous_user();
    $user->login = $timestamp - 1000;
    $user->pass = '';

    $user_a = clone $user;
    $user_a->uid = 12;
    $user_a->mail = '3user@example.com';

    $user_b = clone $user;
    $user_b->uid = 123;
    $user_b->mail = 'user@example.com';

    $hash_a = user_pass_rehash($user_a->pass, $timestamp, $user_a->login, $user_a->uid, $user_a->mail);
    $hash_b = user_pass_rehash($user_b->pass, $timestamp, $user_b->login, $user_b->uid, $user_b->mail);

    $this->assertNotEqual($hash_a, $hash_b, "No user_pass_rehash() hash collision for different users with no stored password.");
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
