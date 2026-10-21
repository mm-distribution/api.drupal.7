# aggregator_permission()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 295–304 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L295-L304)
- **Module/theme:** aggregator
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function aggregator_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function aggregator_permission() {
  return array(
    'administer news feeds' => array(
      'title' => t('Administer news feeds'),
    ),
    'access news feeds' => array(
      'title' => t('View news feeds'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
