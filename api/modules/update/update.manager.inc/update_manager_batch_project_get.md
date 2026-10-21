# update_manager_batch_project_get()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 869–908 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L869-L908)
- **Module/theme:** update
- **Topics:** [update_manager_file](../../../topics/update_manager_file.md)

## Signature

```php
function update_manager_batch_project_get($project, $url, &$context)
```

## Documentation

```text
Implements callback_batch_operation().

Downloads, unpacks, and verifies a project.

This function assumes that the provided URL points to a file archive of some
sort. The URL can have any scheme that we have a file stream wrapper to
support. The file is downloaded to a local cache.

@param string $project
  The short name of the project to download.
@param string $url
  The URL to download a specific project release archive file.
@param array $context
  Reference to an array used for Batch API storage.

@see update_manager_download_page()
```

## Code

```php
function update_manager_batch_project_get($project, $url, &$context) {
  // This is here to show the user that we are in the process of downloading.
  if (!isset($context['sandbox']['started'])) {
    $context['sandbox']['started'] = TRUE;
    $context['message'] = t('Downloading %project', array('%project' => $project));
    $context['finished'] = 0;
    return;
  }

  // Actually try to download the file.
  if (!($local_cache = update_manager_file_get($url))) {
    $context['results']['errors'][$project] = t('Failed to download %project from %url', array('%project' => $project, '%url' => $url));
    return;
  }

  // Extract it.
  $extract_directory = _update_manager_extract_directory();
  try {
    update_manager_archive_extract($local_cache, $extract_directory);
  }
  catch (Exception $e) {
    $context['results']['errors'][$project] = $e->getMessage();
    return;
  }

  // Verify it.
  $archive_errors = update_manager_archive_verify($project, $local_cache, $extract_directory);
  if (!empty($archive_errors)) {
    // We just need to make sure our array keys don't collide, so use the
    // numeric keys from the $archive_errors array.
    foreach ($archive_errors as $key => $error) {
      $context['results']['errors']["$project-$key"] = $error;
    }
    return;
  }

  // Yay, success.
  $context['results']['projects'][$project] = $url;
  $context['finished'] = 1;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
