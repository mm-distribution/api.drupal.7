# update_get_available()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 398–447 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L398-L447)
- **Module/theme:** update

## Signature

```php
function update_get_available($refresh = FALSE)
```

## Documentation

```text
Tries to get update information from cache and refreshes it when necessary.

In addition to checking the cache lifetime, this function also ensures that
there are no .info files for enabled modules or themes that have a newer
modification timestamp than the last time we checked for available update
data. If any .info file was modified, it almost certainly means a new version
of something was installed. Without fresh available update data, the logic in
update_calculate_project_data() will be wrong and produce confusing, bogus
results.

@param $refresh
  (optional) Boolean to indicate if this method should refresh the cache
  automatically if there's no data. Defaults to FALSE.

@return
  Array of data about available releases, keyed by project shortname.

@see update_refresh()
@see update_get_projects()
```

## Code

```php
function update_get_available($refresh = FALSE) {
  module_load_include('inc', 'update', 'update.compare');
  $needs_refresh = FALSE;

  // Grab whatever data we currently have cached in the DB.
  $available = _update_get_cached_available_releases();
  $num_avail = count($available);

  $projects = update_get_projects();
  foreach ($projects as $key => $project) {
    // If there's no data at all, we clearly need to fetch some.
    if (empty($available[$key])) {
      update_create_fetch_task($project);
      $needs_refresh = TRUE;
      continue;
    }

    // See if the .info file is newer than the last time we checked for data,
    // and if so, mark this project's data as needing to be re-fetched. Any
    // time an admin upgrades their local installation, the .info file will
    // be changed, so this is the only way we can be sure we're not showing
    // bogus information right after they upgrade.
    if ($project['info']['_info_file_ctime'] > $available[$key]['last_fetch']) {
      $available[$key]['fetch_status'] = UPDATE_FETCH_PENDING;
    }

    // If we have project data but no release data, we need to fetch. This
    // can be triggered when we fail to contact a release history server.
    if (empty($available[$key]['releases'])) {
      $available[$key]['fetch_status'] = UPDATE_FETCH_PENDING;
    }

    // If we think this project needs to fetch, actually create the task now
    // and remember that we think we're missing some data.
    if (!empty($available[$key]['fetch_status']) && $available[$key]['fetch_status'] == UPDATE_FETCH_PENDING) {
      update_create_fetch_task($project);
      $needs_refresh = TRUE;
    }
  }

  if ($needs_refresh && $refresh) {
    // Attempt to drain the queue of fetch tasks.
    update_fetch_data();
    // After processing the queue, we've (hopefully) got better data, so pull
    // the latest from the cache again and use that directly.
    $available = _update_get_cached_available_releases();
  }

  return $available;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
