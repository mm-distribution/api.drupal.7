# batch_test_chained_form_submit_1()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 202–213 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L202-L213)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_chained_form_submit_1($form, &$form_state)
```

## Documentation

```text
Submit handler #1 for the chained form.
```

## Code

```php
function batch_test_chained_form_submit_1($form, &$form_state) {
  batch_test_stack(NULL, TRUE);

  batch_test_stack('submit handler 1');
  batch_test_stack('value = ' . $form_state['values']['value']);

  $form_state['values']['value']++;
  batch_set(_batch_test_batch_1());

  // This redirect should not be taken into account.
  $form_state['redirect'] = 'should/be/discarded';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
