# filter_test_filter_format_insert()

- **Type:** Function
- **File:** [`modules/simpletest/tests/filter_test.module`](_file.md), lines 11–13 · [local source](../../../../../source/modules/simpletest/tests/filter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module#L11-L13)
- **Module/theme:** batch_test
- **Implements:** [hook_filter_format_insert()](../../../filter/filter.api.php/hook_filter_format_insert.md)

## Signature

```php
function filter_test_filter_format_insert($format)
```

## Documentation

```text
Implements hook_filter_format_insert().
```

## Code

```php
function filter_test_filter_format_insert($format) {
  drupal_set_message('hook_filter_format_insert invoked.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/filter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
