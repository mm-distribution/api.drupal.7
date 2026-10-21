# _form_test_tableselect_form_builder()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 614–639 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L614-L639)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_tableselect_form_builder($form, $form_state, $element_properties)
```

## Documentation

```text
Build a form to test the tableselect element.

@param $form_state
  The form_state
@param $element_properties
  An array of element properties for the tableselect element.

@return
  A form with a tableselect element and a submit button.
```

## Code

```php
function _form_test_tableselect_form_builder($form, $form_state, $element_properties) {
  list($header, $options) = _form_test_tableselect_get_data();

  $form['tableselect'] = $element_properties;

  $form['tableselect'] += array(
    '#prefix' => '<div id="tableselect-wrapper">',
    '#suffix' => '</div>',
    '#type' => 'tableselect',
    '#header' => $header,
    '#options' => $options,
    '#multiple' => FALSE,
    '#empty' => t('Empty text.'),
    '#ajax' => array(
      'callback' => '_form_test_tableselect_ajax_callback',
      'wrapper' => 'tableselect-wrapper',
    ),
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
