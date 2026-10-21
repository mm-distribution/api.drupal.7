# UserPasswordResetTestCase::testResetInvalidation()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 927–933 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L927-L933)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testResetInvalidation()
```

## Documentation

```text
Make sure that password reset URLs are invalidated when the user's email
address changes.
```

## Code

```php
  function testResetInvalidation() {
    $account = $this->drupalCreateUser();
    $original_reset_url = user_pass_reset_url($account);
    user_save($account, array('mail' => '1' . $account->mail));
    $this->drupalGet($original_reset_url);
    $this->assertText('You have tried to use a one-time login link that has either been used or is no longer valid. Please request a new one using the form below.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
