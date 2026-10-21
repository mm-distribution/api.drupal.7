# SiteMaintenanceTestCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1196–1204 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1196-L1204)
- **Class:** [SiteMaintenanceTestCase](../SiteMaintenanceTestCase.md)
- **Module/theme:** system

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Create a user allowed to access site in maintenance mode.
    $this->user = $this->drupalCreateUser(array('access site in maintenance mode'));
    // Create an administrative user.
    $this->admin_user = $this->drupalCreateUser(array('administer site configuration', 'access site in maintenance mode'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
