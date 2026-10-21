# update_calculate_project_data()

- **Type:** Function
- **File:** [`modules/update/update.compare.inc`](_file.md), lines 341–368 · [local source](../../../../source/modules/update/update.compare.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc#L341-L368)
- **Module/theme:** update

## Signature

```php
function update_calculate_project_data($available)
```

## Documentation

```text
Calculates the current update status of all projects on the site.

The results of this function are expensive to compute, especially on sites
with lots of modules or themes, since it involves a lot of comparisons and
other operations. Therefore, we cache the results into the {cache_update}
table using the 'update_project_data' cache ID. However, since this is not
the data about available updates fetched from the network, it is ok to
invalidate it somewhat quickly. If we keep this data for very long, site
administrators are more likely to see incorrect results if they upgrade to a
newer version of a module or theme but do not visit certain pages that
automatically clear this cache.

@param array $available
  Data about available project releases.

@return
  An array of installed projects with current update status information.

@see update_get_available()
@see update_get_projects()
@see update_process_project_info()
@see update_project_cache()
```

## Code

```php
function update_calculate_project_data($available) {
  // Retrieve the projects from cache, if present.
  $projects = update_project_cache('update_project_data');
  // If $projects is empty, then the cache must be rebuilt.
  // Otherwise, return the cached data and skip the rest of the function.
  if (!empty($projects)) {
    return $projects;
  }
  $projects = update_get_projects();
  update_process_project_info($projects);
  foreach ($projects as $project => $project_info) {
    if (isset($available[$project])) {
      update_calculate_project_update_status($project, $projects[$project], $available[$project]);
    }
    else {
      $projects[$project]['status'] = UPDATE_UNKNOWN;
      $projects[$project]['reason'] = t('No available releases found');
    }
  }
  // Give other modules a chance to alter the status (for example, to allow a
  // contrib module to provide fine-grained settings to ignore specific
  // projects or releases).
  drupal_alter('update_status', $projects);

  // Cache the site's update status for at most 1 hour.
  _update_cache_set('update_project_data', $projects, REQUEST_TIME + 3600);
  return $projects;
}
```

---
_Drupal 7.103 · [modules/update/update.compare.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
