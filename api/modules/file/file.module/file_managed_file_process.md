# file_managed_file_process()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 373–512 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L373-L512)
- **Module/theme:** file

## Signature

```php
function file_managed_file_process($element, &$form_state, $form)
```

## Documentation

```text
Process function to expand the managed_file element type.

Expands the file type to include Upload and Remove buttons, as well as
support for a default value.
```

## Code

```php
function file_managed_file_process($element, &$form_state, $form) {
  $fid = isset($element['#value']['fid']) ? $element['#value']['fid'] : 0;

  // Set some default element properties.
  $element['#progress_indicator'] = empty($element['#progress_indicator']) ? 'none' : $element['#progress_indicator'];
  $element['#file'] = $fid ? file_load($fid) : FALSE;
  $element['#tree'] = TRUE;

  $ajax_settings = array(
    'path' => 'file/ajax/' . implode('/', $element['#array_parents']) . '/' . $form['form_build_id']['#value'],
    'wrapper' => $element['#id'] . '-ajax-wrapper',
    'effect' => 'fade',
    'progress' => array(
      'type' => $element['#progress_indicator'],
      'message' => $element['#progress_message'],
    ),
  );

  // Set up the buttons first since we need to check if they were clicked.
  $element['upload_button'] = array(
    '#name' => implode('_', $element['#parents']) . '_upload_button',
    '#type' => 'submit',
    '#value' => t('Upload'),
    '#validate' => array(),
    '#submit' => array('file_managed_file_submit'),
    '#limit_validation_errors' => array($element['#parents']),
    '#ajax' => $ajax_settings,
    '#weight' => -5,
  );

  // Force the progress indicator for the remove button to be either 'none' or
  // 'throbber', even if the upload button is using something else.
  $ajax_settings['progress']['type'] = ($element['#progress_indicator'] == 'none') ? 'none' : 'throbber';
  $ajax_settings['progress']['message'] = NULL;
  $ajax_settings['effect'] = 'none';
  $element['remove_button'] = array(
    '#name' => implode('_', $element['#parents']) . '_remove_button',
    '#type' => 'submit',
    '#value' => t('Remove'),
    '#validate' => array(),
    '#submit' => array('file_managed_file_submit'),
    '#limit_validation_errors' => array($element['#parents']),
    '#ajax' => $ajax_settings,
    '#weight' => -5,
  );

  $element['fid'] = array(
    '#type' => 'hidden',
    '#value' => $fid,
  );

  // Add progress bar support to the upload if possible.
  if ($element['#progress_indicator'] == 'bar' && $implementation = file_progress_implementation()) {
    $upload_progress_key = mt_rand();

    if ($implementation == 'uploadprogress') {
      $element['UPLOAD_IDENTIFIER'] = array(
        '#type' => 'hidden',
        '#value' => $upload_progress_key,
        '#attributes' => array('class' => array('file-progress')),
        // Uploadprogress extension requires this field to be at the top of the
        // form.
        '#weight' => -20,
      );
    }
    elseif ($implementation == 'apc') {
      $element['APC_UPLOAD_PROGRESS'] = array(
        '#type' => 'hidden',
        '#value' => $upload_progress_key,
        '#attributes' => array('class' => array('file-progress')),
        // Uploadprogress extension requires this field to be at the top of the
        // form.
        '#weight' => -20,
      );
    }

    // Add the upload progress callback.
    $element['upload_button']['#ajax']['progress']['path'] = 'file/progress/' . $upload_progress_key;
  }

  // The file upload field itself.
  $element['upload'] = array(
    '#name' => 'files[' . implode('_', $element['#parents']) . ']',
    '#type' => 'file',
    // This #title will not actually be used as the upload field's HTML label,
    // since the theme function for upload fields never passes the element
    // through theme('form_element'). Instead the parent element's #title is
    // used as the label (see below). That is usually a more meaningful label
    // anyway.
    '#title' => t('Choose a file'),
    '#title_display' => 'invisible',
    // Set the ID manually so the desired field label can be associated with it
    // below. Use the same method for setting the ID that the form API
    // autogenerator does.
    '#id' => drupal_html_id('edit-' . implode('-', array_merge($element['#parents'], array('upload')))),
    '#size' => $element['#size'],
    '#theme_wrappers' => array(),
    '#weight' => -10,
  );

  // Indicate that $element['#title'] should be used as the HTML label for the
  // file upload field.
  $element['#label_for'] = $element['upload']['#id'];

  if ($fid && $element['#file']) {
    $element['filename'] = array(
      '#type' => 'markup',
      '#markup' => theme('file_link', array('file' => $element['#file'])) . ' ',
      '#weight' => -10,
    );
    // Anonymous users who have uploaded a temporary file need a
    // non-session-based token added so file_managed_file_value() can check
    // that they have permission to use this file on subsequent submissions of
    // the same form (for example, after an Ajax upload or form validation
    // error).
    if (!$GLOBALS['user']->uid && $element['#file']->status != FILE_STATUS_PERMANENT) {
      $element['fid_token'] = array(
        '#type' => 'hidden',
        '#value' => drupal_hmac_base64('file-' . $fid, drupal_get_private_key() . drupal_get_hash_salt()),
      );
    }
  }

  // Add the extension list to the page as JavaScript settings.
  if (isset($element['#upload_validators']['file_validate_extensions'][0])) {
    $extension_list = implode(',', array_filter(explode(' ', $element['#upload_validators']['file_validate_extensions'][0])));
    $element['upload']['#attached']['js'] = array(
      array(
        'type' => 'setting',
        'data' => array('file' => array('elements' => array('#' . $element['upload']['#id'] => $extension_list)))
      )
    );
  }

  // Prefix and suffix used for Ajax replacement.
  $element['#prefix'] = '<div id="' . $element['#id'] . '-ajax-wrapper">';
  $element['#suffix'] = '</div>';

  return $element;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
