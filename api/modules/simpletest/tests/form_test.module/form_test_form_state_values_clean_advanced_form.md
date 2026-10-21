# form_test_form_state_values_clean_advanced_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1094–1107 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1094-L1107)
- **Module/theme:** batch_test

## Signature

```php
function form_test_form_state_values_clean_advanced_form($form, &$form_state)
```

## Documentation

```text
Form constructor for the form_state_values_clean() test.
```

## Code

```php
function form_test_form_state_values_clean_advanced_form($form, &$form_state) {
  // Build an example form containing a managed file and a submit form element.
  $form['image'] = array(
    '#type' => 'managed_file',
    '#title' => t('Image'),
    '#upload_location' => 'public://',
    '#default_value' => 0,
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
