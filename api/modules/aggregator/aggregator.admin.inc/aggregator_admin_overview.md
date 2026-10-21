# aggregator_admin_overview()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 11–13 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L11-L13)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_admin_overview()
```

## Documentation

```text
Page callback: Displays the Aggregator module administration page.
```

## Code

```php
function aggregator_admin_overview() {
  return aggregator_view();
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
