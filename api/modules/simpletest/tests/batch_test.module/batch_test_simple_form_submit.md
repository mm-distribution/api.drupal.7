# batch_test_simple_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 121–128 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L121-L128)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_simple_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for the simple form.
```

## Code

```php
function batch_test_simple_form_submit($form, &$form_state) {
  batch_test_stack(NULL, TRUE);

  $function = '_batch_test_' . $form_state['values']['batch'];
  batch_set($function());

  $form_state['redirect'] = 'batch-test/redirect';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
