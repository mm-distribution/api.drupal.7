# form_test_load_include_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.file.inc`](_file.md), lines 12–30 · [local source](../../../../../source/modules/simpletest/tests/form_test.file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.file.inc#L12-L30)
- **Module/theme:** batch_test

## Signature

```php
function form_test_load_include_menu($form, &$form_state)
```

## Documentation

```text
Form constructor for testing FAPI file inclusion of the file specified in
hook_menu().
```

## Code

```php
function form_test_load_include_menu($form, &$form_state) {
  // Submit the form via Ajax. That way the FAPI has to care about including
  // the file specified in hook_menu().
  $ajax_wrapper_id = drupal_html_id('form-test-load-include-menu-ajax-wrapper');
  $form['ajax_wrapper'] = array(
    '#markup' => '<div id="' . $ajax_wrapper_id . '"></div>',
  );
  $form['button'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#submit' => array('form_test_load_include_submit'),
    '#ajax' => array(
      'wrapper' => $ajax_wrapper_id,
      'method' => 'append',
      'callback' => 'form_test_load_include_menu_ajax',
    ),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.file.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
