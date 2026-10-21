# UserUpgradePathPasswordTokenTestCase::testUserUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.user.test`](../_file.md), lines 26–35 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test#L26-L35)
- **Class:** [UserUpgradePathPasswordTokenTestCase](../UserUpgradePathPasswordTokenTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testUserUpgrade()
```

## Documentation

```text
Test a successful upgrade.
```

## Code

```php
  public function testUserUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');
    $this->assertEqual(variable_get('user_mail_register_no_approval_required_body'), ', [user:name], [site:name], [site:url], [site:url-brief], [user:mail], [date:medium], [site:login-url], [user:edit-url], [user:one-time-login-url].', 'Existing email templates have been modified (password token involved).');
    // Check that a non-md5 hash was untouched.
    $pass = db_query('SELECT pass FROM {users} WHERE uid = 3')->fetchField();
    $this->assertEqual('$S$DAK00p3Dkojkf4O/UizYxenguXnjv', $pass, 'Pre-existing non-MD5 password hash was not altered');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
