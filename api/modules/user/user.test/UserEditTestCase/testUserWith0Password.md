# UserEditTestCase::testUserWith0Password()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2328–2342 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2328-L2342)
- **Class:** [UserEditTestCase](../UserEditTestCase.md)
- **Module/theme:** user

## Signature

```php
public function testUserWith0Password()
```

## Documentation

```text
Tests setting the password to "0".
```

## Code

```php
  public function testUserWith0Password() {
    $admin = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($admin);
    // Create a regular user.
    $user1 = $this->drupalCreateUser(array());

    $edit = array('pass[pass1]' => '0', 'pass[pass2]' => '0');
    $this->drupalPost("user/" . $user1->uid . "/edit", $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));

    $this->drupalLogout();
    $user1->pass_raw = '0';
    $this->drupalLogin($user1);
    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
