# filter_test_filter_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/filter_test.module`](_file.md), lines 32–44 · [local source](../../../../../source/modules/simpletest/tests/filter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module#L32-L44)
- **Module/theme:** batch_test
- **Implements:** [hook_filter_info()](../../../filter/filter.api.php/hook_filter_info.md)

## Signature

```php
function filter_test_filter_info()
```

## Documentation

```text
Implements hook_filter_info().
```

## Code

```php
function filter_test_filter_info() {
  $filters['filter_test_uncacheable'] = array(
    'title' => 'Uncacheable filter',
    'description' => 'Does nothing, but makes a text format uncacheable.',
    'cache' => FALSE,
  );
  $filters['filter_test_replace'] = array(
    'title' => 'Testing filter',
    'description' => 'Replaces all content with filter and text format information.',
    'process callback' => 'filter_test_replace',
  );
  return $filters;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/filter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
