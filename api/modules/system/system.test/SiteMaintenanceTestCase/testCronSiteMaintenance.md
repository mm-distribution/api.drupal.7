# SiteMaintenanceTestCase::testCronSiteMaintenance()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1286–1315 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1286-L1315)
- **Class:** [SiteMaintenanceTestCase](../SiteMaintenanceTestCase.md)
- **Module/theme:** system

## Signature

```php
function testCronSiteMaintenance()
```

## Documentation

```text
Verify access to cron.php with custom 403 page during maintenance mode.
```

## Code

```php
  function testCronSiteMaintenance() {
    global $base_url;

    // Set custom 403 page.
    $this->drupalLogin($this->admin_user);
    $edit = array(
      'title' => $this->randomName(10),
      'body' => array(LANGUAGE_NONE => array(array('value' => $this->randomName(100)))),
    );
    $node = $this->drupalCreateNode($edit);

    // Use a custom 403 page.
    $this->drupalPost('admin/config/system/site-information', array('site_403' => 'node/' . $node->nid), t('Save configuration'));

    // Turn on maintenance mode.
    $edit = array(
      'maintenance_mode' => 1,
    );
    $this->drupalPost('admin/config/development/maintenance', $edit, t('Save configuration'));
    $this->drupalLogout();

    // Access cron.php without valid cron key.
    $this->drupalGet($base_url . '/cron.php', array('external' => TRUE));
    $this->assertResponse(503);

    // Access cron.php with valid cron key.
    $key = variable_get('cron_key', 'drupal');
    $this->drupalGet($base_url . '/cron.php', array('external' => TRUE, 'query' => array('cron_key' => $key)));
    $this->assertResponse(503);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
