# form_test_storage_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 751–810 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L751-L810)
- **Module/theme:** batch_test

## Signature

```php
function form_test_storage_form($form, &$form_state)
```

## Documentation

```text
A multistep form for testing the form storage.

It uses two steps for editing a virtual "thing". Any changes to it are saved
in the form storage and have to be present during any step. By setting the
request parameter "cache" the form can be tested with caching enabled, as
it would be the case, if the form would contain some #ajax callbacks.

@see form_test_storage_form_submit()
```

## Code

```php
function form_test_storage_form($form, &$form_state) {
  if ($form_state['rebuild']) {
    $form_state['input'] = array();
  }
  // Initialize
  if (empty($form_state['storage'])) {
    if (empty($form_state['input'])) {
      $_SESSION['constructions'] = 0;
    }
    // Put the initial thing into the storage
    $form_state['storage'] = array(
      'thing' => array(
        'title' => 'none',
        'value' => '',
      ),
    );
  }
  // Count how often the form is constructed.
  $_SESSION['constructions']++;
  drupal_set_message("Form constructions: " . $_SESSION['constructions']);

  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => 'Title',
    '#default_value' => $form_state['storage']['thing']['title'],
    '#required' => TRUE,
  );
  $form['value'] = array(
    '#type' => 'textfield',
    '#title' => 'Value',
    '#default_value' => $form_state['storage']['thing']['value'],
    '#element_validate' => array('form_test_storage_element_validate_value_cached'),
  );
  $form['continue_button'] = array(
    '#type' => 'button',
    '#value' => 'Reset',
    // Rebuilds the form without keeping the values.
  );
  $form['continue_submit'] = array(
    '#type' => 'submit',
    '#value' => 'Continue submit',
    '#submit' => array('form_storage_test_form_continue_submit'),
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Save',
  );

  if (isset($_REQUEST['cache'])) {
    // Manually activate caching, so we can test that the storage keeps working
    // when it's enabled.
    $form_state['cache'] = TRUE;
  }

  if (isset($_REQUEST['immutable'])) {
    $form_state['build_info']['immutable'] = TRUE;
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
