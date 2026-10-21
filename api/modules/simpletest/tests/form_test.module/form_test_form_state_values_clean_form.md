# form_test_form_state_values_clean_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1069–1080 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1069-L1080)
- **Module/theme:** batch_test

## Signature

```php
function form_test_form_state_values_clean_form($form, &$form_state)
```

## Documentation

```text
Form builder for form_state_values_clean() test.
```

## Code

```php
function form_test_form_state_values_clean_form($form, &$form_state) {
  // Build an example form containing multiple submit and button elements; not
  // only on the top-level.
  $form = array('#tree' => TRUE);
  $form['foo'] = array('#type' => 'submit', '#value' => t('Submit'));
  $form['bar'] = array('#type' => 'submit', '#value' => t('Submit'));
  $form['beer'] = array('#type' => 'value', '#value' => 1000);
  $form['baz']['foo'] = array('#type' => 'button', '#value' => t('Submit'));
  $form['baz']['baz'] = array('#type' => 'submit', '#value' => t('Submit'));
  $form['baz']['beer'] = array('#type' => 'value', '#value' => 2000);
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
