# DashboardBlocksTestCase::testDashboardAccess()

- **Type:** Method
- **File:** [`modules/dashboard/dashboard.test`](../_file.md), lines 41–61 · [local source](../../../../../source/modules/dashboard/dashboard.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test#L41-L61)
- **Class:** [DashboardBlocksTestCase](../DashboardBlocksTestCase.md)
- **Module/theme:** dashboard

## Signature

```php
function testDashboardAccess()
```

## Documentation

```text
Tests adding a block to the dashboard and checking access to it.
```

## Code

```php
  function testDashboardAccess() {
    // Add a new custom block to a dashboard region.
    $custom_block = array();
    $custom_block['info'] = $this->randomName(8);
    $custom_block['title'] = $this->randomName(8);
    $custom_block['body[value]'] = $this->randomName(32);
    $custom_block['regions[stark]'] = 'dashboard_main';
    $this->drupalPost('admin/structure/block/add', $custom_block, t('Save block'));

    // Ensure admin access.
    $this->drupalGet('admin/dashboard');
    $this->assertResponse(200, 'Admin has access to the dashboard.');
    $this->assertRaw($custom_block['title'], 'Admin has access to a dashboard block.');

    // Ensure non-admin access is denied.
    $normal_user = $this->drupalCreateUser();
    $this->drupalLogin($normal_user);
    $this->drupalGet('admin/dashboard');
    $this->assertResponse(403, 'Non-admin has no access to the dashboard.');
    $this->assertNoText($custom_block['title'], 'Non-admin has no access to a dashboard block.');
  }
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.test](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test) · Licensed GPL-2.0-or-later (see LICENSE)._
