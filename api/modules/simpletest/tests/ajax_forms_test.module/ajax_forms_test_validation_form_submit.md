# ajax_forms_test_validation_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 468–470 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L468-L470)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_validation_form_submit($form, $form_state)
```

## Documentation

```text
Submit handler for the validation form.
```

## Code

```php
function ajax_forms_test_validation_form_submit($form, $form_state) {
  drupal_set_message(t("Validation form submitted"));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
