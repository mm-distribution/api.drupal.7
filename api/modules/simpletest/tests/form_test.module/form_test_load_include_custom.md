# form_test_load_include_custom()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1938–1951 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1938-L1951)
- **Module/theme:** batch_test

## Signature

```php
function form_test_load_include_custom($form, &$form_state)
```

## Documentation

```text
Menu callback for testing custom form includes.
```

## Code

```php
function form_test_load_include_custom($form, &$form_state) {
  $form['button'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#submit' => array('form_test_load_include_submit'),
  );
  // Specify the include file and enable form caching. That way the form is
  // cached when it is submitted, but needs to find the specified submit handler
  // in the include.
  // Filename is a bit weird here: modules/simpletest/tests/form_test.file.inc
  form_load_include($form_state, 'inc', 'form_test', 'form_test.file');
  $form_state['cache'] = TRUE;
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
