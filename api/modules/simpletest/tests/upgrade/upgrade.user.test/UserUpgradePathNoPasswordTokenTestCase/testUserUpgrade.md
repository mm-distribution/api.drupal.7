# UserUpgradePathNoPasswordTokenTestCase::testUserUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.user.test`](../_file.md), lines 62–68 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test#L62-L68)
- **Class:** [UserUpgradePathNoPasswordTokenTestCase](../UserUpgradePathNoPasswordTokenTestCase.md)
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
    $this->assertEqual(variable_get('user_mail_register_no_approval_required_body'), '[user:name], [site:name], [site:url], [site:url-brief], [user:mail], [date:medium], [site:login-url], [user:edit-url], [user:one-time-login-url].', 'Existing email templates have been modified (password token not involved).');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
