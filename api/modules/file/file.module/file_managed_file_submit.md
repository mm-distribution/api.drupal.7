# file_managed_file_submit()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 655–691 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L655-L691)
- **Module/theme:** file

## Signature

```php
function file_managed_file_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for upload / remove buttons of managed_file elements.

@see file_managed_file_process()
```

## Code

```php
function file_managed_file_submit($form, &$form_state) {
  // Determine whether it was the upload or the remove button that was clicked,
  // and set $element to the managed_file element that contains that button.
  $parents = $form_state['triggering_element']['#array_parents'];
  $button_key = array_pop($parents);
  $element = drupal_array_get_nested_value($form, $parents);

  // No action is needed here for the upload button, because all file uploads on
  // the form are processed by file_managed_file_value() regardless of which
  // button was clicked. Action is needed here for the remove button, because we
  // only remove a file in response to its remove button being clicked.
  if ($button_key == 'remove_button') {
    // If it's a temporary file we can safely remove it immediately, otherwise
    // it's up to the implementing module to clean up files that are in use.
    if ($element['#file'] && $element['#file']->status == 0) {
      file_delete($element['#file']);
    }
    // Update both $form_state['values'] and $form_state['input'] to reflect
    // that the file has been removed, so that the form is rebuilt correctly.
    // $form_state['values'] must be updated in case additional submit handlers
    // run, and for form building functions that run during the rebuild, such as
    // when the managed_file element is part of a field widget.
    // $form_state['input'] must be updated so that file_managed_file_value()
    // has correct information during the rebuild.
    $values_element = $element['#extended'] ? $element['fid'] : $element;
    form_set_value($values_element, NULL, $form_state);
    drupal_array_set_nested_value($form_state['input'], $values_element['#parents'], NULL);
  }

  // Set the form to rebuild so that $form is correctly updated in response to
  // processing the file removal. Since this function did not change $form_state
  // if the upload button was clicked, a rebuild isn't necessary in that
  // situation and setting $form_state['redirect'] to FALSE would suffice.
  // However, we choose to always rebuild, to keep the form processing workflow
  // consistent between the two buttons.
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
