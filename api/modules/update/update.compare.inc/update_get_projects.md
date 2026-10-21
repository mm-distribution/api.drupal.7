# update_get_projects()

- **Type:** Function
- **File:** [`modules/update/update.compare.inc`](_file.md), lines 56–78 · [local source](../../../../source/modules/update/update.compare.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc#L56-L78)
- **Module/theme:** update

## Signature

```php
function update_get_projects()
```

## Documentation

```text
Fetches an array of installed and enabled projects.

This is only responsible for generating an array of projects (taking into
account projects that include more than one module or theme). Other
information like the specific version and install type (official release,
dev snapshot, etc) is handled later in update_process_project_info() since
that logic is only required when preparing the status report, not for
fetching the available release data.

This array is fairly expensive to construct, since it involves a lot of disk
I/O, so we cache the results into the {cache_update} table using the
'update_project_projects' cache ID. However, since this is not the data about
available updates fetched from the network, it is acceptable to invalidate it
somewhat quickly. If we keep this data for very long, site administrators are
more likely to see incorrect results if they upgrade to a newer version of a
module or theme but do not visit certain pages that automatically clear this
cache.

@return
  An associative array of currently enabled projects keyed by the
  machine-readable project short name. Each project contains:
  - name: The machine-readable project short name.
  - info: An array with values from the main .info file for this project.
    - name: The human-readable name of the project.
    - package: The package that the project is grouped under.
    - version: The version of the project.
    - project: The Drupal.org project name.
    - datestamp: The date stamp of the project's main .info file.
    - _info_file_ctime: The maximum file change time for all of the .info
      files included in this project.
  - datestamp: The date stamp when the project was released, if known.
  - includes: An associative array containing all projects included with this
    project, keyed by the machine-readable short name with the human-readable
    name as value.
  - project_type: The type of project. Allowed values are 'module' and
    'theme'.
  - project_status: This indicates if the project is enabled and will always
    be TRUE, as the function only returns enabled projects.
  - sub_themes: If the project is a theme it contains an associative array of
    all sub-themes.
  - base_themes: If the project is a theme it contains an associative array
    of all base-themes.

@see update_process_project_info()
@see update_calculate_project_data()
@see update_project_cache()
```

## Code

```php
function update_get_projects() {
  $projects = &drupal_static(__FUNCTION__, array());
  if (empty($projects)) {
    // Retrieve the projects from cache, if present.
    $projects = update_project_cache('update_project_projects');
    if (empty($projects)) {
      // Still empty, so we have to rebuild the cache.
      $module_data = system_rebuild_module_data();
      $theme_data = system_rebuild_theme_data();
      _update_process_info_list($projects, $module_data, 'module', TRUE);
      _update_process_info_list($projects, $theme_data, 'theme', TRUE);
      if (variable_get('update_check_disabled', FALSE)) {
        _update_process_info_list($projects, $module_data, 'module', FALSE);
        _update_process_info_list($projects, $theme_data, 'theme', FALSE);
      }
      // Allow other modules to alter projects before fetching and comparing.
      drupal_alter('update_projects', $projects);
      // Cache the site's project data for at most 1 hour.
      _update_cache_set('update_project_projects', $projects, REQUEST_TIME + 3600);
    }
  }
  return $projects;
}
```

---
_Drupal 7.103 · [modules/update/update.compare.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
