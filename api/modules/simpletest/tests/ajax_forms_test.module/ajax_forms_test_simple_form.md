# ajax_forms_test_simple_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 44–71 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L44-L71)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_simple_form($form, &$form_state)
```

## Documentation

```text
A basic form used to test form_state['values'] during callback.
```

## Code

```php
function ajax_forms_test_simple_form($form, &$form_state) {
  $form = array();
  $form['select'] = array(
    '#type' => 'select',
    '#options' => array(
      'red' => 'red',
      'green' => 'green',
      'blue' => 'blue'),
    '#ajax' => array(
      'callback' => 'ajax_forms_test_simple_form_select_callback',
    ),
    '#suffix' => '<div id="ajax_selected_color">No color yet selected</div>',
  );

  $form['checkbox'] = array(
    '#type' => 'checkbox',
    '#title' => t('Test checkbox'),
    '#ajax' => array(
       'callback' => 'ajax_forms_test_simple_form_checkbox_callback',
    ),
    '#suffix' => '<div id="ajax_checkbox_value">No action yet</div>',
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('submit'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
