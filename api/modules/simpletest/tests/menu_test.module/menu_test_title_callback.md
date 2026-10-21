# menu_test_title_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 561–563 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L561-L563)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_title_callback($title, $case_no = 3)
```

## Documentation

```text
Concatenates a string, by using the t() function and a case number.

@param $title
  Title string.
@param $case_number
  The current case number which is tests (defaults to 3).
```

## Code

```php
function menu_test_title_callback($title, $case_no = 3) {
  return t($title) . ' - Case ' . $case_no;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
