# update_process_project_info()

- **Type:** Function
- **File:** [`modules/update/update.compare.inc`](_file.md), lines 276–315 · [local source](../../../../source/modules/update/update.compare.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc#L276-L315)
- **Module/theme:** update

## Signature

```php
function update_process_project_info(&$projects)
```

## Documentation

```text
Determines version and type information for currently installed projects.

Processes the list of projects on the system to figure out the currently
installed versions, and other information that is required before we can
compare against the available releases to produce the status report.

@param $projects
  Array of project information from update_get_projects().
```

## Code

```php
function update_process_project_info(&$projects) {
  foreach ($projects as $key => $project) {
    // Assume an official release until we see otherwise.
    $install_type = 'official';

    $info = $project['info'];

    if (isset($info['version'])) {
      // Check for development snapshots
      if (preg_match('@(dev|HEAD)@', $info['version'])) {
        $install_type = 'dev';
      }

      // Figure out what the currently installed major version is. We need
      // to handle both contribution (e.g. "5.x-1.3", major = 1) and core
      // (e.g. "5.1", major = 5) version strings.
      $matches = array();
      if (preg_match('/^(\d+\.x-)?(\d+)\..*$/', $info['version'], $matches)) {
        $info['major'] = $matches[2];
      }
      elseif (!isset($info['major'])) {
        // This would only happen for version strings that don't follow the
        // drupal.org convention. We let contribs define "major" in their
        // .info in this case, and only if that's missing would we hit this.
        $info['major'] = -1;
      }
    }
    else {
      // No version info available at all.
      $install_type = 'unknown';
      $info['version'] = t('Unknown');
      $info['major'] = -1;
    }

    // Finally, save the results we care about into the $projects array.
    $projects[$key]['existing_version'] = $info['version'];
    $projects[$key]['existing_major'] = $info['major'];
    $projects[$key]['install_type'] = $install_type;
  }
}
```

---
_Drupal 7.103 · [modules/update/update.compare.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.compare.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
