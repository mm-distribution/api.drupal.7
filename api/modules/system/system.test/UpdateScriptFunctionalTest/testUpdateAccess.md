# UpdateScriptFunctionalTest::testUpdateAccess()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2542–2568 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2542-L2568)
- **Class:** [UpdateScriptFunctionalTest](../UpdateScriptFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testUpdateAccess()
```

## Documentation

```text
Tests access to the update script.
```

## Code

```php
  function testUpdateAccess() {
    // Try accessing update.php without the proper permission.
    $regular_user = $this->drupalCreateUser();
    $this->drupalLogin($regular_user);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertResponse(403);

    // Try accessing update.php as an anonymous user.
    $this->drupalLogout();
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertResponse(403);

    // Access the update page with the proper permission.
    $this->drupalLogin($this->update_user);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertResponse(200);

    // Access the update page as user 1.
    $user1 = user_load(1);
    $user1->pass_raw = user_password();
    require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
    $user1->pass = user_hash_password(trim($user1->pass_raw));
    db_query("UPDATE {users} SET pass = :pass WHERE uid = :uid", array(':pass' => $user1->pass, ':uid' => $user1->uid));
    $this->drupalLogin($user1);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
