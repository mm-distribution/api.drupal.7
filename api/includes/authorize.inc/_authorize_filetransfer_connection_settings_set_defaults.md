# _authorize_filetransfer_connection_settings_set_defaults()

- **Type:** Function
- **File:** [`includes/authorize.inc`](_file.md), lines 171–186 · [local source](../../../source/includes/authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc#L171-L186)

## Signature

```php
function _authorize_filetransfer_connection_settings_set_defaults(&$element, $key, array $defaults)
```

## Documentation

```text
Sets the default settings on a file transfer connection form recursively.

The default settings for the file transfer connection forms are saved in
the database. The settings are stored as a nested array in the case of a
settings form that has fieldsets or otherwise uses a nested structure.
Therefore, to properly add defaults, we need to walk through all the
children form elements and process those defaults recursively.

@param $element
  Reference to the Form API form element we're operating on.
@param $key
  The key for our current form element, if any.
@param array $defaults
  The default settings for the file transfer backend we're operating on.
```

## Code

```php
function _authorize_filetransfer_connection_settings_set_defaults(&$element, $key, array $defaults) {
  // If we're operating on a form element which isn't a fieldset, and we have
  // a default setting saved, stash it in #default_value.
  if (!empty($key) && isset($defaults[$key]) && isset($element['#type']) && $element['#type'] != 'fieldset') {
    $element['#default_value'] = $defaults[$key];
  }
  // Now, we walk through all the child elements, and recursively invoke
  // ourself on each one. Since the $defaults settings array can be nested
  // (because of #tree, any values inside fieldsets will be nested), if
  // there's a subarray of settings for the form key we're currently
  // processing, pass in that subarray to the recursive call. Otherwise, just
  // pass on the whole $defaults array.
  foreach (element_children($element) as $child_key) {
    _authorize_filetransfer_connection_settings_set_defaults($element[$child_key], $child_key, ((isset($defaults[$key]) && is_array($defaults[$key])) ? $defaults[$key] : $defaults));
  }
}
```

---
_Drupal 7.103 · [includes/authorize.inc](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
