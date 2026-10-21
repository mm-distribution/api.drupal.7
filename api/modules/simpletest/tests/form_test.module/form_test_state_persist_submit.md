# form_test_state_persist_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1674–1677 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1674-L1677)
- **Module/theme:** batch_test

## Signature

```php
function form_test_state_persist_submit($form, &$form_state)
```

## Documentation

```text
Submit handler.

@see form_test_state_persist()
```

## Code

```php
function form_test_state_persist_submit($form, &$form_state) {
  drupal_set_message($form_state['value']);
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
