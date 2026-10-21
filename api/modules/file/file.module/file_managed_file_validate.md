# file_managed_file_validate()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 620–648 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L620-L648)
- **Module/theme:** file

## Signature

```php
function file_managed_file_validate(&$element, &$form_state)
```

## Documentation

```text
An #element_validate callback for the managed_file element.
```

## Code

```php
function file_managed_file_validate(&$element, &$form_state) {
  // If referencing an existing file, only allow if there are existing
  // references. This prevents unmanaged files from being deleted if this
  // item were to be deleted.
  $clicked_button = end($form_state['triggering_element']['#parents']);
  if ($clicked_button != 'remove_button' && !empty($element['fid']['#value'])) {
    if ($file = file_load($element['fid']['#value'])) {
      if ($file->status == FILE_STATUS_PERMANENT) {
        $references = file_usage_list($file);
        if (empty($references)) {
          form_error($element, t('The file used in the !name field may not be referenced.', array('!name' => $element['#title'])));
        }
      }
    }
    else {
      form_error($element, t('The file referenced by the !name field does not exist.', array('!name' => $element['#title'])));
    }
  }

  // Check required property based on the FID.
  if ($element['#required'] && empty($element['fid']['#value']) && !in_array($clicked_button, array('upload_button', 'remove_button'))) {
    form_error($element['upload'], t('!name field is required.', array('!name' => $element['#title'])));
  }

  // Consolidate the array value of this field to a single FID.
  if (!$element['#extended']) {
    form_set_value($element, $element['fid']['#value'], $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
