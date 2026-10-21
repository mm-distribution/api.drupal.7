# form_test_user_register_form_rebuild()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1913–1916 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1913-L1916)
- **Module/theme:** batch_test

## Signature

```php
function form_test_user_register_form_rebuild($form, &$form_state)
```

## Documentation

```text
Submit callback that just lets the form rebuild.
```

## Code

```php
function form_test_user_register_form_rebuild($form, &$form_state) {
  drupal_set_message('Form rebuilt.');
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
