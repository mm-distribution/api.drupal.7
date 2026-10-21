# file_ajax_progress()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 311–334 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L311-L334)
- **Module/theme:** file

## Signature

```php
function file_ajax_progress($key)
```

## Documentation

```text
Menu callback for upload progress.

@param $key
  The unique key for this upload process.
```

## Code

```php
function file_ajax_progress($key) {
  $progress = array(
    'message' => t('Starting upload...'),
    'percentage' => -1,
  );

  $implementation = file_progress_implementation();
  if ($implementation == 'uploadprogress') {
    $status = uploadprogress_get_info($key);
    if (isset($status['bytes_uploaded']) && !empty($status['bytes_total'])) {
      $progress['message'] = t('Uploading... (@current of @total)', array('@current' => format_size($status['bytes_uploaded']), '@total' => format_size($status['bytes_total'])));
      $progress['percentage'] = round(100 * $status['bytes_uploaded'] / $status['bytes_total']);
    }
  }
  elseif ($implementation == 'apc') {
    $status = apc_fetch('upload_' . $key);
    if (isset($status['current']) && !empty($status['total'])) {
      $progress['message'] = t('Uploading... (@current of @total)', array('@current' => format_size($status['current']), '@total' => format_size($status['total'])));
      $progress['percentage'] = round(100 * $status['current'] / $status['total']);
    }
  }

  drupal_json_output($progress);
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
