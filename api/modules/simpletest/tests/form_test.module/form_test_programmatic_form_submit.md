# form_test_programmatic_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1775–1777 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1775-L1777)
- **Module/theme:** batch_test

## Signature

```php
function form_test_programmatic_form_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for programmatic form submissions.

To test that the submission handler is correctly executed, we store the
submitted values in a place we can access from the caller context.
```

## Code

```php
function form_test_programmatic_form_submit($form, &$form_state) {
  $form_state['storage']['programmatic_form_submit'] = $form_state['values'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
