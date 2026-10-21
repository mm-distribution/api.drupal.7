# update_delete_file_if_stale()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 990–997 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L990-L997)
- **Module/theme:** update

## Signature

```php
function update_delete_file_if_stale($path)
```

## Documentation

```text
Deletes stale files and directories from the update manager disk cache.

Files and directories older than 6 hours and development snapshots older than
5 minutes are considered stale. We only cache development snapshots for 5
minutes since otherwise updated snapshots might not be downloaded as
expected.

When checking file ages, we need to use the ctime, not the mtime
(modification time) since many (all?) tar implementations go out of their way
to set the mtime on the files they create to the timestamps recorded in the
tarball. We want to see the last time the file was changed on disk, which is
left alone by tar and correctly set to the time the archive file was
unpacked.

@param $path
  A string containing a file path or (streamwrapper) URI.
```

## Code

```php
function update_delete_file_if_stale($path) {
  if (file_exists($path)) {
    $filectime = filectime($path);
    if (REQUEST_TIME - $filectime > DRUPAL_MAXIMUM_TEMP_FILE_AGE || (preg_match('/.*-dev\.(tar\.gz|zip)/i', $path) && REQUEST_TIME - $filectime > 300)) {
      file_unmanaged_delete_recursive($path);
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
