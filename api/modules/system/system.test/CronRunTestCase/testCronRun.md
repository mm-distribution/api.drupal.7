# CronRunTestCase::testCronRun()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 813–829 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L813-L829)
- **Class:** [CronRunTestCase](../CronRunTestCase.md)
- **Module/theme:** system

## Signature

```php
function testCronRun()
```

## Documentation

```text
Test cron runs.
```

## Code

```php
  function testCronRun() {
    global $base_url;

    // Run cron anonymously without any cron key.
    $this->drupalGet($base_url . '/cron.php', array('external' => TRUE));
    $this->assertResponse(403);

    // Run cron anonymously with a random cron key.
    $key = $this->randomName(16);
    $this->drupalGet($base_url . '/cron.php', array('external' => TRUE, 'query' => array('cron_key' => $key)));
    $this->assertResponse(403);

    // Run cron anonymously with the valid cron key.
    $key = variable_get('cron_key', 'drupal');
    $this->drupalGet($base_url . '/cron.php', array('external' => TRUE, 'query' => array('cron_key' => $key)));
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
