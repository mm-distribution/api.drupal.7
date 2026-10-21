# file_get_file_references()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 1102–1123 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L1102-L1123)
- **Module/theme:** file
- **Topics:** [file-module-api](../../../topics/file-module-api.md)

## Signature

```php
function file_get_file_references($file, $field = NULL, $age = FIELD_LOAD_REVISION, $field_type = 'file', $check_access = TRUE)
```

## Documentation

```text
Retrieves a list of references to a file.

@param $file
  A file object.
@param $field
  (optional) A field array to be used for this check. If given, limits the
  reference check to the given field.
@param $age
  (optional) A constant that specifies which references to count. Use
  FIELD_LOAD_REVISION to retrieve all references within all revisions or
  FIELD_LOAD_CURRENT to retrieve references only in the current revisions.
@param $field_type
  (optional) The name of a field type. If given, limits the reference check
  to fields of the given type.
@param $check_access
  (optional) A boolean that specifies whether the permissions of the current
  user should be checked when retrieving references. If FALSE, all
  references to the file are returned. If TRUE, only references from
  entities that the current user has access to are returned. Defaults to
  TRUE for backwards compatibility reasons, but FALSE is recommended for
  most situations.

@return
  An integer value.
```

## Code

```php
function file_get_file_references($file, $field = NULL, $age = FIELD_LOAD_REVISION, $field_type = 'file', $check_access = TRUE) {
  $references = drupal_static(__FUNCTION__, array());
  $fields = isset($field) ? array($field['field_name'] => $field) : field_info_fields();

  foreach ($fields as $field_name => $file_field) {
    if ((empty($field_type) || $file_field['type'] == $field_type) && !isset($references[$field_name])) {
      // Get each time this file is used within a field.
      $query = new EntityFieldQuery();
      $query
        ->fieldCondition($file_field, 'fid', $file->fid)
        ->age($age);
      if (!$check_access) {
        // Neutralize the 'entity_field_access' query tag added by
        // field_sql_storage_field_storage_query().
        $query->addTag('DANGEROUS_ACCESS_CHECK_OPT_OUT');
      }
      $references[$field_name] = $query->execute();
    }
  }

  return isset($field) ? $references[$field['field_name']] : array_filter($references);
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
