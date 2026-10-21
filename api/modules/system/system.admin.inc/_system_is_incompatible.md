# _system_is_incompatible()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 757–768 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L757-L768)
- **Module/theme:** system

## Signature

```php
function _system_is_incompatible(&$incompatible, $files, $file)
```

## Documentation

```text
Recursively check compatibility.

@param $incompatible
  An associative array which at the end of the check contains all
  incompatible files as the keys, their values being TRUE.
@param $files
  The set of files that will be tested.
@param $file
  The file at which the check starts.
@return
  Returns TRUE if an incompatible file is found, NULL (no return value)
  otherwise.
```

## Code

```php
function _system_is_incompatible(&$incompatible, $files, $file) {
  if (isset($incompatible[$file->name])) {
    return TRUE;
  }
  // Recursively traverse required modules, looking for incompatible modules.
  foreach ($file->requires as $requires) {
    if (isset($files[$requires]) && _system_is_incompatible($incompatible, $files, $files[$requires])) {
      $incompatible[$file->name] = TRUE;
      return TRUE;
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
