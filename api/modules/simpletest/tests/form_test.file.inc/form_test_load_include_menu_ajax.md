# form_test_load_include_menu_ajax()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.file.inc`](_file.md), lines 42–48 · [local source](../../../../../source/modules/simpletest/tests/form_test.file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.file.inc#L42-L48)
- **Module/theme:** batch_test

## Signature

```php
function form_test_load_include_menu_ajax($form)
```

## Documentation

```text
Ajax callback for the file inclusion via menu test.
```

## Code

```php
function form_test_load_include_menu_ajax($form) {
  // We don't need to return anything, since #ajax['method'] is 'append', which
  // does not remove the original #ajax['wrapper'] element, and status messages
  // are automatically added by the Ajax framework as long as there's a wrapper
  // element to add them to.
  return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.file.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
