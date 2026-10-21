# batch_test_multistep_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 153–172 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L153-L172)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_multistep_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for the multistep form.
```

## Code

```php
function batch_test_multistep_form_submit($form, &$form_state) {
  batch_test_stack(NULL, TRUE);

  switch ($form_state['storage']['step']) {
    case 1:
      batch_set(_batch_test_batch_1());
      break;
    case 2:
      batch_set(_batch_test_batch_2());
      break;
  }

  if ($form_state['storage']['step'] < 2) {
    $form_state['storage']['step']++;
    $form_state['rebuild'] = TRUE;
  }

  // This will only be effective on the last step.
  $form_state['redirect'] = 'batch-test/redirect';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
