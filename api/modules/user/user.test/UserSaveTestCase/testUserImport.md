# UserSaveTestCase::testUserImport()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2164–2188 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2164-L2188)
- **Class:** [UserSaveTestCase](../UserSaveTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserImport()
```

## Documentation

```text
Test creating a user with arbitrary uid.
```

## Code

```php
  function testUserImport() {
    // User ID must be a number that is not in the database.
    $max_uid = db_query('SELECT MAX(uid) FROM {users}')->fetchField();
    $test_uid = $max_uid + mt_rand(1000, 1000000);
    $test_name = $this->randomName();

    // Create the base user, based on drupalCreateUser().
    $user = array(
      'name' => $test_name,
      'uid' => $test_uid,
      'mail' => $test_name . '@example.com',
      'is_new' => TRUE,
      'pass' => user_password(),
      'status' => 1,
    );
    $user_by_return = user_save(drupal_anonymous_user(), $user);
    $this->assertTrue($user_by_return, 'Loading user by return of user_save().');

    // Test if created user exists.
    $user_by_uid = user_load($test_uid);
    $this->assertTrue($user_by_uid, 'Loading user by uid.');

    $user_by_name = user_load_by_name($test_name);
    $this->assertTrue($user_by_name, 'Loading user by name.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
