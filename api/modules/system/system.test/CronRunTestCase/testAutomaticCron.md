# CronRunTestCase::testAutomaticCron()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 837–866 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L837-L866)
- **Class:** [CronRunTestCase](../CronRunTestCase.md)
- **Module/theme:** system

## Signature

```php
function testAutomaticCron()
```

## Documentation

```text
Ensure that the automatic cron run feature is working.

In these tests we do not use REQUEST_TIME to track start time, because we
need the exact time when cron is triggered.
```

## Code

```php
  function testAutomaticCron() {
    // Ensure cron does not run when the cron threshold is enabled and was
    // not passed.
    $cron_last = time();
    $cron_safe_threshold = 100;
    variable_set('cron_last', $cron_last);
    variable_set('cron_safe_threshold', $cron_safe_threshold);
    $this->drupalGet('');
    $this->assertTrue($cron_last == variable_get('cron_last', NULL), 'Cron does not run when the cron threshold is not passed.');

    // Test if cron runs when the cron threshold was passed.
    $cron_last = time() - 200;
    variable_set('cron_last', $cron_last);
    $this->drupalGet('');
    sleep(1);
    $this->assertTrue($cron_last < variable_get('cron_last', NULL), 'Cron runs when the cron threshold is passed.');

    // Disable the cron threshold through the interface.
    $admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($admin_user);
    $this->drupalPost('admin/config/system/cron', array('cron_safe_threshold' => 0), t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'));
    $this->drupalLogout();

    // Test if cron does not run when the cron threshold is disabled.
    $cron_last = time() - 200;
    variable_set('cron_last', $cron_last);
    $this->drupalGet('');
    $this->assertTrue($cron_last == variable_get('cron_last', NULL), 'Cron does not run when the cron threshold is disabled.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
