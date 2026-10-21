# form_test_double_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1997–2002 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1997-L2002)
- **Module/theme:** batch_test

## Signature

```php
function form_test_double_form()
```

## Documentation

```text
Menu callback returns two instances of the same form.
```

## Code

```php
function form_test_double_form() {
  return array(
    'form1' => drupal_get_form('form_test_html_id'),
    'form2' => drupal_get_form('form_test_html_id'),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
