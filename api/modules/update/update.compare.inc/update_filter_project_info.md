# update_filter_project_info()

- **Type:** Function
- **File:** [`modules/update/update.compare.inc`](_file.md), lines 826–838 · [local source](../../../../source/modules/update/update.compare.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc#L826-L838)
- **Module/theme:** update

## Signature

```php
function update_filter_project_info($info)
```

## Documentation

```text
Filters the project .info data to only save attributes we need.

@param array $info
  Array of .info file data as returned by drupal_parse_info_file().

@return
  Array of .info file data we need for the update manager.

@see _update_process_info_list()
```

## Code

```php
function update_filter_project_info($info) {
  $whitelist = array(
    '_info_file_ctime',
    'datestamp',
    'major',
    'name',
    'package',
    'project',
    'project status url',
    'version',
  );
  return array_intersect_key($info, drupal_map_assoc($whitelist));
}
```

---
_Drupal 7.103 · [modules/update/update.compare.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
