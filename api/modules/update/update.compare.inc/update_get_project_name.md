# update_get_project_name()

- **Type:** Function
- **File:** [`modules/update/update.compare.inc`](_file.md), lines 255–264 · [local source](../../../../source/modules/update/update.compare.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc#L255-L264)
- **Module/theme:** update

## Signature

```php
function update_get_project_name($file)
```

## Documentation

```text
Determines what project a given file object belongs to.

@param $file
  A file object as returned by system_get_files_database().

@return
  The canonical project short name.

@see system_get_files_database()
```

## Code

```php
function update_get_project_name($file) {
  $project_name = '';
  if (isset($file->info['project'])) {
    $project_name = $file->info['project'];
  }
  elseif (isset($file->info['package']) && (strpos($file->info['package'], 'Core') === 0)) {
    $project_name = 'drupal';
  }
  return $project_name;
}
```

---
_Drupal 7.103 · [modules/update/update.compare.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
