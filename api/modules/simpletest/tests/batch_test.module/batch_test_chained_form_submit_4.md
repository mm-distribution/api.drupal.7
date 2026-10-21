# batch_test_chained_form_submit_4()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 245–254 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L245-L254)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_chained_form_submit_4($form, &$form_state)
```

## Documentation

```text
Submit handler #4 for the chained form.
```

## Code

```php
function batch_test_chained_form_submit_4($form, &$form_state) {
  batch_test_stack('submit handler 4');
  batch_test_stack('value = ' . $form_state['values']['value']);

  $form_state['values']['value']++;
  batch_set(_batch_test_batch_3());

  // This is the redirect that should prevail.
  $form_state['redirect'] = 'batch-test/redirect';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
