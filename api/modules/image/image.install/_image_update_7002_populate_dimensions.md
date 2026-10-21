# _image_update_7002_populate_dimensions()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 314–351 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L314-L351)
- **Module/theme:** image
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function _image_update_7002_populate_dimensions($table, $field_name, &$last_fid)
```

## Documentation

```text
Populate image dimensions in a specific table.

@param $table
  The name of the database table to be updated.
@param $columns
  Keyed array of columns this table is supposed to have.
@param $last_fid
  The fid of the last image to have been processed.

@return
  The number of images that were processed.
```

## Code

```php
function _image_update_7002_populate_dimensions($table, $field_name, &$last_fid) {
  // Define how many images to process per pass.
  $images_per_pass = 100;

  // Query the database for fid / URI pairs.
  $query = db_select($table, NULL, array('fetch' => PDO::FETCH_ASSOC));
  $query->join('file_managed', NULL, $table . '.' . $field_name . '_fid = file_managed.fid');

  if ($last_fid) {
    $query->condition('file_managed.fid', $last_fid, '>');
  }

  $result = $query->fields('file_managed', array('fid', 'uri'))
    ->orderBy('file_managed.fid')
    ->range(0, $images_per_pass)
    ->execute();

  $count = 0;
  foreach ($result as $file) {
    $count++;
    $info = image_get_info($file['uri']);

    if (is_array($info)) {
      db_update($table)
        ->fields(array(
          $field_name . '_width' => $info['width'],
          $field_name . '_height' => $info['height'],
        ))
        ->condition($field_name . '_fid', $file['fid'])
        ->execute();
    }
  }

  // If less than the requested number of rows were returned then this table
  // has been fully processed.
  $last_fid = ($count < $images_per_pass) ? NULL : $file['fid'];
  return $count;
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
