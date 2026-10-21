# file_managed_file_value()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 517–615 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L517-L615)
- **Module/theme:** file

## Signature

```php
function file_managed_file_value(&$element, $input = FALSE, $form_state = NULL)
```

## Documentation

```text
The #value_callback for a managed_file type element.
```

## Code

```php
function file_managed_file_value(&$element, $input = FALSE, $form_state = NULL) {
  $fid = 0;
  $force_default = FALSE;

  // Find the current value of this field from the form state.
  $form_state_fid = $form_state['values'];
  foreach ($element['#parents'] as $parent) {
    $form_state_fid = isset($form_state_fid[$parent]) ? $form_state_fid[$parent] : 0;
  }

  if ($element['#extended'] && isset($form_state_fid['fid'])) {
    $fid = $form_state_fid['fid'];
  }
  elseif (is_numeric($form_state_fid)) {
    $fid = $form_state_fid;
  }

  // Process any input and save new uploads.
  if ($input !== FALSE) {
    $return = $input;

    // Uploads take priority over all other values.
    if ($file = file_managed_file_save_upload($element)) {
      $fid = $file->fid;
    }
    else {
      // Check for #filefield_value_callback values.
      // Because FAPI does not allow multiple #value_callback values like it
      // does for #element_validate and #process, this fills the missing
      // functionality to allow File fields to be extended through FAPI.
      if (isset($element['#file_value_callbacks'])) {
        foreach ($element['#file_value_callbacks'] as $callback) {
          $callback($element, $input, $form_state);
        }
      }
      // If a FID was submitted, load the file (and check access if it's not a
      // public file) to confirm it exists and that the current user has access
      // to it.
      if (isset($input['fid']) && ($file = file_load($input['fid']))) {
        // By default the public:// file scheme provided by Drupal core is the
        // only one that allows files to be publicly accessible to everyone, so
        // it is the only one for which the file access checks are bypassed.
        // Other modules which provide publicly accessible streams of their own
        // in hook_stream_wrappers() can add the corresponding scheme to the
        // 'file_public_schema' variable to bypass file access checks for those
        // as well. This should only be done for schemes that are completely
        // publicly accessible, with no download restrictions; for security
        // reasons all other schemes must go through the file_download_access()
        // check.
        if (!in_array(file_uri_scheme($file->uri), variable_get('file_public_schema', array('public'))) && !file_download_access($file->uri)) {
          $force_default = TRUE;
        }
        // Temporary files that belong to other users should never be allowed.
        elseif ($file->status != FILE_STATUS_PERMANENT) {
          if ($GLOBALS['user']->uid && $file->uid != $GLOBALS['user']->uid) {
            $force_default = TRUE;
          }
          // Since file ownership can't be determined for anonymous users, they
          // are not allowed to reuse temporary files at all. But they do need
          // to be able to reuse their own files from earlier submissions of
          // the same form, so to allow that, check for the token added by
          // file_managed_file_process().
          elseif (!$GLOBALS['user']->uid) {
            $token = drupal_array_get_nested_value($form_state['input'], array_merge($element['#parents'], array('fid_token')));
            if ($token !== drupal_hmac_base64('file-' . $file->fid, drupal_get_private_key() . drupal_get_hash_salt())) {
              $force_default = TRUE;
            }
          }
        }
        // If all checks pass, allow the file to be changed.
        if (!$force_default) {
          $fid = $file->fid;
        }
      }
    }
  }

  // If there is no input or if the default value was requested above, use the
  // default value.
  if ($input === FALSE || $force_default) {
    if ($element['#extended']) {
      $default_fid = isset($element['#default_value']['fid']) ? $element['#default_value']['fid'] : 0;
      $return = isset($element['#default_value']) ? $element['#default_value'] : array('fid' => 0);
    }
    else {
      $default_fid = isset($element['#default_value']) ? $element['#default_value'] : 0;
      $return = array('fid' => 0);
    }

    // Confirm that the file exists when used as a default value.
    if ($default_fid && $file = file_load($default_fid)) {
      $fid = $file->fid;
    }
  }

  $return['fid'] = $fid;

  return $return;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
