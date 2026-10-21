# batch_test_chained_form_submit_3()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 232–240 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L232-L240)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_chained_form_submit_3($form, &$form_state)
```

## Documentation

```text
Submit handler #3 for the chained form.
```

## Code

```php
function batch_test_chained_form_submit_3($form, &$form_state) {
  batch_test_stack('submit handler 3');
  batch_test_stack('value = ' . $form_state['values']['value']);

  $form_state['values']['value']++;

  // This redirect should not be taken into account.
  $form_state['redirect'] = 'should/be/discarded';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
