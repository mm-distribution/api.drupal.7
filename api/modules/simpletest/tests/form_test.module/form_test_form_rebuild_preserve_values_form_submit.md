# form_test_form_rebuild_preserve_values_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1645–1648 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1645-L1648)
- **Module/theme:** batch_test

## Signature

```php
function form_test_form_rebuild_preserve_values_form_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for form_test_form_rebuild_preserve_values_form().
```

## Code

```php
function form_test_form_rebuild_preserve_values_form_submit($form, &$form_state) {
  // Finish the workflow. Do not rebuild.
  drupal_set_message(t('Form values: %values', array('%values' => var_export($form_state['values'], TRUE))));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
