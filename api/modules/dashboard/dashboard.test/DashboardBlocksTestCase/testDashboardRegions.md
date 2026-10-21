# DashboardBlocksTestCase::testDashboardRegions()

- **Type:** Method
- **File:** [`modules/dashboard/dashboard.test`](../_file.md), lines 66–83 · [local source](../../../../../source/modules/dashboard/dashboard.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test#L66-L83)
- **Class:** [DashboardBlocksTestCase](../DashboardBlocksTestCase.md)
- **Module/theme:** dashboard

## Signature

```php
function testDashboardRegions()
```

## Documentation

```text
Tests that dashboard regions are displayed or hidden properly.
```

## Code

```php
  function testDashboardRegions() {
    $dashboard_regions = dashboard_region_descriptions();

    // Ensure blocks can be placed in dashboard regions.
    $this->drupalGet('admin/dashboard/configure');
    foreach ($dashboard_regions as $region => $description) {
      $elements = $this->xpath('//option[@value=:region]', array(':region' => $region));
      $this->assertTrue(!empty($elements), format_string('%region is an available choice on the dashboard block configuration page.', array('%region' => $region)));
    }

    // Ensure blocks cannot be placed in dashboard regions on the standard
    // blocks configuration page.
    $this->drupalGet('admin/structure/block');
    foreach ($dashboard_regions as $region => $description) {
      $elements = $this->xpath('//option[@value=:region]', array(':region' => $region));
      $this->assertTrue(empty($elements), format_string('%region is not an available choice on the block configuration page.', array('%region' => $region)));
    }
  }
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.test](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test) · Licensed GPL-2.0-or-later (see LICENSE)._
