# _update_build_fetch_url()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 294–319 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L294-L319)
- **Module/theme:** update

## Signature

```php
function _update_build_fetch_url($project, $site_key = '')
```

## Documentation

```text
Generates the URL to fetch information about project updates.

This figures out the right URL to use, based on the project's .info file and
the global defaults. Appends optional query arguments when the site is
configured to report usage stats.

@param $project
  The array of project information from update_get_projects().
@param $site_key
  (optional) The anonymous site key hash. Defaults to an empty string.

@return
  The URL for fetching information about updates to the specified project.

@see update_fetch_data()
@see _update_process_fetch_task()
@see update_get_projects()
```

## Code

```php
function _update_build_fetch_url($project, $site_key = '') {
  $name = $project['name'];
  $url = _update_get_fetch_url_base($project);
  $url .= '/' . $name . '/' . DRUPAL_CORE_COMPATIBILITY;

  // Only append usage information if we have a site key and the project is
  // enabled. We do not want to record usage statistics for disabled projects.
  if (!empty($site_key) && (strpos($project['project_type'], 'disabled') === FALSE)) {
    // Append the site key.
    $url .= (strpos($url, '?') !== FALSE) ? '&' : '?';
    $url .= 'site_key=';
    $url .= rawurlencode($site_key);

    // Append the version.
    if (!empty($project['info']['version'])) {
      $url .= '&version=';
      $url .= rawurlencode($project['info']['version']);
    }

    // Append the list of modules or themes enabled.
    $list = array_keys($project['includes']);
    $url .= '&list=';
    $url .= rawurlencode(implode(',', $list));
  }
  return $url;
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
