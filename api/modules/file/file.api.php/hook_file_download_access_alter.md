# hook_file_download_access_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/file/file.api.php`](_file.md), lines 55–60 · [local source](../../../../source/modules/file/file.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.api.php#L55-L60)
- **Module/theme:** file

## Signature

```php
function hook_file_download_access_alter(&$grants, $file_item, $entity_type, $entity)
```

## Documentation

```text
Alter the access rules applied to a file download.

Entities that implement file management set the access rules for their
individual files. Module may use this hook to create custom access rules
for file downloads.

@see hook_file_download_access().

@param $grants
  An array of grants gathered by hook_file_download_access(). The array is
  keyed by the module that defines the entity type's access control; the
  values are Boolean grant responses for each module.
@param array $file_item
  The array of information about the file to alter access for.
@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  The $entity to which $file is referenced.
```

## Code

```php
function hook_file_download_access_alter(&$grants, $file_item, $entity_type, $entity) {
  // For our example module, we always enforce the rules set by node module.
  if (isset($grants['node'])) {
    $grants = array('node' => $grants['node']);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_download_access_alter()".

_None found._

---
_Drupal 7.103 · [modules/file/file.api.php](https://github.com/drupal/drupal/blob/7.103/modules/file/file.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
