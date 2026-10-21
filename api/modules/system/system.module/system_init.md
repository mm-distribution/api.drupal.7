# system_init()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1928–1965 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1928-L1965)
- **Module/theme:** system
- **Implements:** [hook_init()](../system.api.php/hook_init.md)

## Signature

```php
function system_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function system_init() {
  $path = drupal_get_path('module', 'system');
  // Add the CSS for this module. These aren't in system.info, because they
  // need to be in the CSS_SYSTEM group rather than the CSS_DEFAULT group.
  drupal_add_css($path . '/system.base.css', array('group' => CSS_SYSTEM, 'every_page' => TRUE));
  if (path_is_admin(current_path())) {
    drupal_add_css($path . '/system.admin.css', array('group' => CSS_SYSTEM));
  }
  drupal_add_css($path . '/system.menus.css', array('group' => CSS_SYSTEM, 'every_page' => TRUE));
  drupal_add_css($path . '/system.messages.css', array('group' => CSS_SYSTEM, 'every_page' => TRUE));
  drupal_add_css($path . '/system.theme.css', array('group' => CSS_SYSTEM, 'every_page' => TRUE));

  // Ignore slave database servers for this request.
  //
  // In Drupal's distributed database structure, new data is written to the
  // master and then propagated to the slave servers.  This means there is a
  // lag between when data is written to the master and when it is available on
  // the slave. At these times, we will want to avoid using a slave server
  // temporarily. For example, if a user posts a new node then we want to
  // disable the slave server for that user temporarily to allow the slave
  // server to catch up. That way, that user will see their changes immediately
  // while for other users we still get the benefits of having a slave server,
  // just with slightly stale data.  Code that wants to disable the slave
  // server should use the db_ignore_slave() function to set
  // $_SESSION['ignore_slave_server'] to the timestamp after which the slave
  // can be re-enabled.
  if (isset($_SESSION['ignore_slave_server'])) {
    if ($_SESSION['ignore_slave_server'] >= REQUEST_TIME) {
      Database::ignoreTarget('default', 'slave');
    }
    else {
      unset($_SESSION['ignore_slave_server']);
    }
  }

  // Add CSS/JS files from module .info files.
  system_add_module_assets();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
