# PasswordHashingTest::testLongPassword()

- **Type:** Method
- **File:** [`modules/simpletest/tests/password.test`](../_file.md), lines 64–81 · [local source](../../../../../../source/modules/simpletest/tests/password.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test#L64-L81)
- **Class:** [PasswordHashingTest](../PasswordHashingTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testLongPassword()
```

## Documentation

```text
Verifies that passwords longer than 512 bytes are not hashed.
```

## Code

```php
  public function testLongPassword() {
    $password = str_repeat('x', 512);
    $result = user_hash_password($password);
    $this->assertFalse(empty($result), '512 byte long password is allowed.');
    $password = str_repeat('x', 513);
    $result = user_hash_password($password);
    $this->assertFalse($result, '513 byte long password is not allowed.');
    // Check a string of 3-byte UTF-8 characters.
    $password = str_repeat('€', 170);
    $result = user_hash_password($password);
    $this->assertFalse(empty($result), '510 byte long password is allowed.');
    $password .= 'xx';
    $result = user_hash_password($password);
    $this->assertFalse(empty($result), '512 byte long password is allowed.');
    $password = str_repeat('€', 171);
    $result = user_hash_password($password);
    $this->assertFalse($result, '513 byte long password is not allowed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/password.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test) · Licensed GPL-2.0-or-later (see LICENSE)._
