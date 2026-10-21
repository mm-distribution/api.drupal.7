# DashboardBlocksTestCase::setUp()

- **Type:** Method
- **File:** [`modules/dashboard/dashboard.test`](../_file.md), lines 20–36 · [local source](../../../../../source/modules/dashboard/dashboard.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test#L20-L36)
- **Class:** [DashboardBlocksTestCase](../DashboardBlocksTestCase.md)
- **Module/theme:** dashboard

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

    // Create and log in an administrative user having access to the dashboard.
    $admin_user = $this->drupalCreateUser(array('access dashboard', 'administer blocks', 'access administration pages', 'administer modules'));
    $this->drupalLogin($admin_user);

    // Make sure that the dashboard is using the same theme as the rest of the
    // site (and in particular, the same theme used on 403 pages). This forces
    // the dashboard blocks to be the same for an administrator as for a
    // regular user, and therefore lets us test that the dashboard blocks
    // themselves are specifically removed for a user who does not have access
    // to the dashboard page.
    theme_enable(array('stark'));
    variable_set('theme_default', 'stark');
    variable_set('admin_theme', 'stark');
  }
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.test](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test) · Licensed GPL-2.0-or-later (see LICENSE)._
