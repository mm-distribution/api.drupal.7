# hook_filter_format_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 287–289 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L287-L289)
- **Module/theme:** filter
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_filter_format_insert($format)
```

## Documentation

```text
Perform actions when a new text format has been created.

@param $format
  The format object of the format being updated.

@see hook_filter_format_update()
@see hook_filter_format_disable()
```

## Code

```php
function hook_filter_format_insert($format) {
  mymodule_cache_rebuild();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_filter_format_insert()".

- [filter_test_filter_format_insert()](../../simpletest/tests/filter_test.module/filter_test_filter_format_insert.md) — `modules/simpletest/tests/filter_test.module`

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
