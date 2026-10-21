# DashboardBlocksTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/dashboard/dashboard.test`](../_file.md), lines 12–18 · [local source](../../../../../source/modules/dashboard/dashboard.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test#L12-L18)
- **Class:** [DashboardBlocksTestCase](../DashboardBlocksTestCase.md)
- **Module/theme:** dashboard

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Dashboard blocks',
      'description' => 'Test blocks as used by the dashboard.',
      'group' => 'Dashboard',
    );
  }
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.test](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test) · Licensed GPL-2.0-or-later (see LICENSE)._
