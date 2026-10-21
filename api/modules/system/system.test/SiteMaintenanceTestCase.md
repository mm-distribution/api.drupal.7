# SiteMaintenanceTestCase

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 1184–1316 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1184-L1316)
- **Module/theme:** system

## Signature

```php
class SiteMaintenanceTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests site maintenance functionality.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

### $user

```php
protected $user;
```

## Methods (derived index)

- [getInfo()](SiteMaintenanceTestCase/getInfo.md)
- [setUp()](SiteMaintenanceTestCase/setUp.md)
- [testSiteMaintenance()](SiteMaintenanceTestCase/testSiteMaintenance.md) — Verify site maintenance mode functionality.
- [testCronSiteMaintenance()](SiteMaintenanceTestCase/testCronSiteMaintenance.md) — Verify access to cron.php with custom 403 page during maintenance mode.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
