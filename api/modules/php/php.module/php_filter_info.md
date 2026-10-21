# php_filter_info()

- **Type:** Function
- **File:** [`modules/php/php.module`](_file.md), lines 138–147 · [local source](../../../../source/modules/php/php.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module#L138-L147)
- **Module/theme:** php
- **Implements:** [hook_filter_info()](../../filter/filter.api.php/hook_filter_info.md)

## Signature

```php
function php_filter_info()
```

## Documentation

```text
Implements hook_filter_info().

Provide PHP code filter. Use with care.
```

## Code

```php
function php_filter_info() {
  $filters['php_code'] = array(
    'title' => t('PHP evaluator'),
    'description' => t('Executes a piece of PHP code. The usage of this filter should be restricted to administrators only!'),
    'process callback' => 'php_eval',
    'tips callback' => '_php_filter_tips',
    'cache' => FALSE,
  );
  return $filters;
}
```

---
_Drupal 7.103 · [modules/php/php.module](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module) · Licensed GPL-2.0-or-later (see LICENSE)._
