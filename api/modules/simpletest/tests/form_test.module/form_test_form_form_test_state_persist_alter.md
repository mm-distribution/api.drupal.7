# form_test_form_form_test_state_persist_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1684–1690 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1684-L1690)
- **Module/theme:** batch_test
- **Implements:** [hook_form_FORM_ID_alter()](../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function form_test_form_form_test_state_persist_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

@see form_test_state_persist()
```

## Code

```php
function form_test_form_form_test_state_persist_alter(&$form, &$form_state) {
  // Simulate a form alter implementation inserting form elements that enable
  // caching of the form, e.g. elements having #ajax.
  if (!empty($_REQUEST['cache'])) {
    $form_state['cache'] = TRUE;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
