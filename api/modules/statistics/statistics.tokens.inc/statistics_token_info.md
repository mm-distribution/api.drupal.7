# statistics_token_info()

- **Type:** Function
- **File:** [`modules/statistics/statistics.tokens.inc`](_file.md), lines 11–29 · [local source](../../../../source/modules/statistics/statistics.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.tokens.inc#L11-L29)
- **Module/theme:** statistics
- **Implements:** [hook_token_info()](../../system/system.api.php/hook_token_info.md)

## Signature

```php
function statistics_token_info()
```

## Documentation

```text
Implements hook_token_info().
```

## Code

```php
function statistics_token_info() {
  $node['total-count'] = array(
    'name' => t("Number of views"),
    'description' => t("The number of visitors who have read the node."),
  );
  $node['day-count'] = array(
    'name' => t("Views today"),
    'description' => t("The number of visitors who have read the node today."),
  );
  $node['last-view'] = array(
    'name' => t("Last view"),
    'description' => t("The date on which a visitor last read the node."),
    'type' => 'date',
  );

  return array(
    'tokens' => array('node' => $node),
  );
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
