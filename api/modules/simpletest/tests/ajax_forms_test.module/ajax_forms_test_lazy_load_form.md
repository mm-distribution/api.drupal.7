# ajax_forms_test_lazy_load_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 484–497 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L484-L497)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_lazy_load_form($form, &$form_state)
```

## Documentation

```text
Form builder: Builds a form that triggers a simple AJAX callback.
```

## Code

```php
function ajax_forms_test_lazy_load_form($form, &$form_state) {
  $form['add_files'] = array(
    '#type' => 'checkbox',
    '#default_value' => FALSE,
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
    '#ajax' => array(
      'callback' => 'ajax_forms_test_lazy_load_form_ajax',
    ),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
