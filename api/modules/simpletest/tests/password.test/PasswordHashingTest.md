# PasswordHashingTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/password.test`](_file.md), lines 11–82 · [local source](../../../../../source/modules/simpletest/tests/password.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test#L11-L82)
- **Module/theme:** batch_test

## Signature

```php
class PasswordHashingTest extends DrupalWebTestCase
```

## Documentation

```text
Unit tests for password hashing API.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

## Methods (derived index)

- [getInfo()](PasswordHashingTest/getInfo.md)
- [setUp()](PasswordHashingTest/setUp.md)
- [testPasswordHashing()](PasswordHashingTest/testPasswordHashing.md) — Test password hashing.
- [testLongPassword()](PasswordHashingTest/testLongPassword.md) — Verifies that passwords longer than 512 bytes are not hashed.

---
_Drupal 7.103 · [modules/simpletest/tests/password.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test) · Licensed GPL-2.0-or-later (see LICENSE)._
