# file_file_download()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 123–228 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L123-L228)
- **Module/theme:** file
- **Implements:** [hook_file_download()](../../system/system.api.php/hook_file_download.md)

## Signature

```php
function file_file_download($uri, $field_type = 'file')
```

## Documentation

```text
Implements hook_file_download().

This function takes an extra parameter $field_type so that it may
be re-used by other File-like modules, such as Image.
```

## Code

```php
function file_file_download($uri, $field_type = 'file') {
  global $user;

  // Get the file record based on the URI. If not in the database just return.
  $files = file_load_multiple(array(), array('uri' => $uri));
  if (count($files)) {
    foreach ($files as $item) {
      // Since some database servers sometimes use a case-insensitive comparison
      // by default, double check that the filename is an exact match.
      if ($item->uri === $uri) {
        $file = $item;
        break;
      }
    }
  }
  if (!isset($file)) {
    return;
  }

  // Find out which (if any) fields of this type contain the file.
  $references = file_get_file_references($file, NULL, FIELD_LOAD_CURRENT, $field_type, FALSE);

  // Stop processing if there are no references in order to avoid returning
  // headers for files controlled by other modules. Make an exception for
  // temporary files where the host entity has not yet been saved (for example,
  // an image preview on a node/add form) in which case, allow download by the
  // file's owner. For anonymous file owners, only the browser session that
  // uploaded the file should be granted access.
  if (empty($references) && ($file->status == FILE_STATUS_PERMANENT || $file->uid != $user->uid || (!$user->uid && empty($_SESSION['anonymous_allowed_file_ids'][$file->fid])))) {
      return;
  }

  // Default to allow access.
  $denied = FALSE;
  // Loop through all references of this file. If a reference explicitly allows
  // access to the field to which this file belongs, no further checks are done
  // and download access is granted. If a reference denies access, eventually
  // existing additional references are checked. If all references were checked
  // and no reference denied access, access is granted as well. If at least one
  // reference denied access, access is denied.
  foreach ($references as $field_name => $field_references) {
    foreach ($field_references as $entity_type => $type_references) {
      foreach ($type_references as $id => $reference) {
        // Try to load $entity and $field.
        $entity = entity_load($entity_type, array($id));
        $entity = reset($entity);
        $field = field_info_field($field_name);

        // Load the field item that references the file.
        $field_item = NULL;
        if ($entity) {
          // Load all field items for that entity.
          $field_items = field_get_items($entity_type, $entity, $field_name);

          // Find the field item with the matching URI.
          foreach ($field_items as $item) {
            if ($item['uri'] == $uri) {
              $field_item = $item;
              break;
            }
          }
        }

        // Check that $entity, $field and $field_item were loaded successfully
        // and check if access to that field is not disallowed. If any of these
        // checks fail, stop checking access for this reference.
        if (empty($entity) || empty($field) || empty($field_item) || !field_access('view', $field, $entity_type, $entity)) {
          $denied = TRUE;
          break;
        }

        // Invoke hook and collect grants/denies for download access.
        // Default to FALSE and let entities overrule this ruling.
        $grants = array('system' => FALSE);
        foreach (module_implements('file_download_access') as $module) {
          $grants = array_merge($grants, array($module => module_invoke($module, 'file_download_access', $field_item, $entity_type, $entity)));
        }
        // Allow other modules to alter the returned grants/denies.
        drupal_alter('file_download_access', $grants, $field_item, $entity_type, $entity);

        if (in_array(TRUE, $grants)) {
          // If TRUE is returned, access is granted and no further checks are
          // necessary.
          $denied = FALSE;
          break 3;
        }

        if (in_array(FALSE, $grants)) {
          // If an implementation returns FALSE, access to this entity is denied
          // but the file could belong to another entity to which the user might
          // have access. Continue with these.
          $denied = TRUE;
        }
      }
    }
  }

  // Access specifically denied.
  if ($denied) {
    return -1;
  }

  // Access is granted.
  $headers = file_get_content_headers($file);
  return $headers;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
