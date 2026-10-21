# form_test_form_rebuild_preserve_values_form_add_more()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1636–1640 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1636-L1640)
- **Module/theme:** batch_test

## Signature

```php
function form_test_form_rebuild_preserve_values_form_add_more($form, &$form_state)
```

## Documentation

```text
Button submit handler for form_test_form_rebuild_preserve_values_form().
```

## Code

```php
function form_test_form_rebuild_preserve_values_form_add_more($form, &$form_state) {
  // Rebuild, to test preservation of input values.
  $form_state['storage']['add_more'] = TRUE;
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
