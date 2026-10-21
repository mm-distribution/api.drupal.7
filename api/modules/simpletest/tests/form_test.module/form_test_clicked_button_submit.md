# form_test_clicked_button_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1853–1855 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1853-L1855)
- **Module/theme:** batch_test

## Signature

```php
function form_test_clicked_button_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for the form_test_clicked_button() form.
```

## Code

```php
function form_test_clicked_button_submit($form, &$form_state) {
  drupal_set_message('Submit handler for form_test_clicked_button executed.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
