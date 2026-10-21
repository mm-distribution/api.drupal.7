# CronRunTestCase::testManualCron()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 931–942 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L931-L942)
- **Class:** [CronRunTestCase](../CronRunTestCase.md)
- **Module/theme:** system

## Signature

```php
function testManualCron()
```

## Documentation

```text
Ensure that the manual cron run is working.
```

## Code

```php
  function testManualCron() {
    $admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($admin_user);

    $this->drupalGet('admin/reports/status/run-cron');
    $this->assertResponse(403);

    $this->drupalGet('admin/reports/status');
    $this->clickLink(t('run cron manually'));
    $this->assertResponse(200);
    $this->assertText(t('Cron ran successfully.'));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
