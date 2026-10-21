# update_get_update_list()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1147–1190 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1147-L1190)

## Signature

```php
function update_get_update_list()
```

## Documentation

```text
Returns a list of all the pending database updates.

@return
  An associative array keyed by module name which contains all information
  about database updates that need to be run, and any updates that are not
  going to proceed due to missing requirements. The system module will
  always be listed first.

  The subarray for each module can contain the following keys:
  - start: The starting update that is to be processed. If this does not
      exist then do not process any updates for this module as there are
      other requirements that need to be resolved.
  - warning: Any warnings about why this module can not be updated.
  - pending: An array of all the pending updates for the module including
      the update number and the description from source code comment for
      each update function. This array is keyed by the update number.
```

## Code

```php
function update_get_update_list() {
  // Make sure that the system module is first in the list of updates.
  $ret = array('system' => array());

  $modules = drupal_get_installed_schema_version(NULL, FALSE, TRUE);
  foreach ($modules as $module => $schema_version) {
    // Skip uninstalled and incompatible modules.
    if ($schema_version == SCHEMA_UNINSTALLED || update_check_incompatibility($module)) {
      continue;
    }
    // Otherwise, get the list of updates defined by this module.
    $updates = drupal_get_schema_versions($module);
    if ($updates !== FALSE) {
      // module_invoke returns NULL for nonexisting hooks, so if no updates
      // are removed, it will == 0.
      $last_removed = module_invoke($module, 'update_last_removed');
      if ($schema_version < $last_removed) {
        $ret[$module]['warning'] = '<em>' . $module . '</em> module can not be updated. Its schema version is ' . $schema_version . '. Updates up to and including ' . $last_removed . ' have been removed in this release. In order to update <em>' . $module . '</em> module, you will first <a href="http://drupal.org/upgrade">need to upgrade</a> to the last version in which these updates were available.';
        continue;
      }

      $updates = drupal_map_assoc($updates);
      foreach (array_keys($updates) as $update) {
        if ($update > $schema_version) {
          // The description for an update comes from its Doxygen.
          $func = new ReflectionFunction($module . '_update_' . $update);
          $description = str_replace(array("\n", '*', '/'), '', $func->getDocComment());
          $ret[$module]['pending'][$update] = "$update - $description";
          if (!isset($ret[$module]['start'])) {
            $ret[$module]['start'] = $update;
          }
        }
      }
      if (!isset($ret[$module]['start']) && isset($ret[$module]['pending'])) {
        $ret[$module]['start'] = $schema_version;
      }
    }
  }

  if (empty($ret['system'])) {
    unset($ret['system']);
  }
  return $ret;
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
