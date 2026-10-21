# update_prepare_d7_bootstrap()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 81–318 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L81-L318)

## Signature

```php
function update_prepare_d7_bootstrap()
```

## Documentation

```text
Performs extra steps required to bootstrap when using a Drupal 6 database.

Users who still have a Drupal 6 database (and are in the process of
updating to Drupal 7) need extra help before a full bootstrap can be
achieved. This function does the necessary preliminary work that allows
the bootstrap to be successful.

No access check has been performed when this function is called, so no
irreversible changes to the database are made here.
```

## Code

```php
function update_prepare_d7_bootstrap() {
  // Allow the bootstrap to proceed even if a Drupal 6 settings.php file is
  // still being used.
  include_once DRUPAL_ROOT . '/includes/install.inc';
  drupal_bootstrap(DRUPAL_BOOTSTRAP_CONFIGURATION);
  global $databases, $db_url, $db_prefix, $update_rewrite_settings;
  if (empty($databases) && !empty($db_url)) {
    $databases = update_parse_db_url($db_url, $db_prefix);
    // Record the fact that the settings.php file will need to be rewritten.
    $update_rewrite_settings = TRUE;
    $settings_file = conf_path() . '/settings.php';
    $writable = drupal_verify_install_file($settings_file, FILE_EXIST|FILE_READABLE|FILE_WRITABLE);
    $requirements = array(
      'settings file' => array(
        'title' => 'Settings file',
        'value' => $writable ? 'The settings file is writable.' : 'The settings file is not writable.',
        'severity' => $writable ? REQUIREMENT_OK : REQUIREMENT_ERROR,
        'description' => $writable ? '' : 'Drupal requires write permissions to <em>' . $settings_file . '</em> during the update process. If you are unsure how to grant file permissions, consult the <a href="http://drupal.org/server-permissions">online handbook</a>.',
      ),
    );
    update_extra_requirements($requirements);
  }

  // The new {blocked_ips} table is used in Drupal 7 to store a list of
  // banned IP addresses. If this table doesn't exist then we are still
  // running on a Drupal 6 database, so we suppress the unavoidable errors
  // that occur by creating a static list.
  $GLOBALS['conf']['blocked_ips'] = array();

  // Check that PDO is available and that the correct PDO database driver is
  // loaded. Bootstrapping to DRUPAL_BOOTSTRAP_DATABASE will result in a fatal
  // error otherwise.
  $message = '';
  $pdo_link = 'http://drupal.org/requirements/pdo';
  // Check that PDO is loaded.
  if (!extension_loaded('pdo')) {
    $message = '<h2>PDO is required!</h2><p>Drupal 7 requires PHP ' . DRUPAL_MINIMUM_PHP . ' or higher with the PHP Data Objects (PDO) extension enabled.</p>';
  }
  // The PDO::ATTR_DEFAULT_FETCH_MODE constant is not available in the PECL
  // version of PDO.
  elseif (!defined('PDO::ATTR_DEFAULT_FETCH_MODE')) {
    $message = '<h2>The wrong version of PDO is installed!</h2><p>Drupal 7 requires the PHP Data Objects (PDO) extension from PHP core to be enabled. This system has the older PECL version installed.';
    $pdo_link = 'http://drupal.org/requirements/pdo#pecl';
  }
  // Check that the correct driver is loaded for the database being updated.
  // If we have no driver information (for example, if someone tried to create
  // the Drupal 7 $databases array themselves but did not do it correctly),
  // this message will be confusing, so do not perform the check; instead, just
  // let the database connection fail in the code that follows.
  elseif (isset($databases['default']['default']['driver']) && !in_array($databases['default']['default']['driver'], PDO::getAvailableDrivers())) {
    $message = '<h2>A PDO database driver is required!</h2><p>You need to enable the PDO_' . strtoupper($databases['default']['default']['driver']) . ' database driver for PHP ' . DRUPAL_MINIMUM_PHP . ' or higher so that Drupal 7 can access the database.</p>';
  }
  if ($message) {
    print $message . '<p>See the <a href="' . $pdo_link . '">system requirements page</a> for more information.</p>';
    exit();
  }

  // Allow the database system to work even if the registry has not been
  // created yet.
  drupal_bootstrap(DRUPAL_BOOTSTRAP_DATABASE);

  // If the site has not updated to Drupal 7 yet, check to make sure that it is
  // running an up-to-date version of Drupal 6 before proceeding. Note this has
  // to happen AFTER the database bootstraps because of
  // drupal_get_installed_schema_version().
  $system_schema = drupal_get_installed_schema_version('system');
  if ($system_schema < 7000) {
    $has_required_schema = $system_schema >= REQUIRED_D6_SCHEMA_VERSION;
    $requirements = array(
      'drupal 6 version' => array(
        'title' => 'Drupal 6 version',
        'value' => $has_required_schema ? 'You are running a current version of Drupal 6.' : 'You are not running a current version of Drupal 6',
        'severity' => $has_required_schema ? REQUIREMENT_OK : REQUIREMENT_ERROR,
        'description' => $has_required_schema ? '' : 'Please update your Drupal 6 installation to the most recent version before attempting to upgrade to Drupal 7',
      ),
    );

    // Make sure that the database environment is properly set up.
    try {
      db_run_tasks(db_driver());
    }
    catch (DatabaseTaskException $e) {
      $requirements['database tasks'] = array(
        'title' => 'Database environment',
        'value' => 'There is a problem with your database environment',
        'severity' => REQUIREMENT_ERROR,
        'description' => $e->getMessage(),
      );
    }

    update_extra_requirements($requirements);

    // Allow a D6 session to work, since the upgrade has not been performed yet.
    $d6_session_name = update_get_d6_session_name();
    if (!empty($_COOKIE[$d6_session_name])) {
      // Set the current sid to the one found in the D6 cookie.
      $sid = $_COOKIE[$d6_session_name];
      $_COOKIE[session_name()] = $sid;
      session_id($sid);
    }

    // Upgrading from D6 to D7.{0,1,2,3,4,8,...} is different than upgrading
    // from D6 to D7.{5,6,7} which should be considered broken. To be able to
    // properly handle this difference in node_update_7012 we need to keep track
    // of whether a D6 > D7 upgrade or a D7 > D7 update is running.
    // Since variable_set() is not available here, the D6 status is being saved
    // in a local variable to be able to store it later.
    $update_d6 = TRUE;
  }

  // Create the registry tables.
  if (!db_table_exists('registry')) {
    $schema['registry'] = array(
      'fields' => array(
        'name'   => array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''),
        'type'   => array('type' => 'varchar', 'length' => 9, 'not null' => TRUE, 'default' => ''),
        'filename'   => array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''),
        'module'   => array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''),
        'weight'   => array('type' => 'int', 'not null' => TRUE, 'default' => 0),
      ),
      'primary key' => array('name', 'type'),
      'indexes' => array(
        'hook' => array('type', 'weight', 'module'),
      ),
    );
    db_create_table('registry', $schema['registry']);
  }
  if (!db_table_exists('registry_file')) {
    $schema['registry_file'] = array(
      'fields' => array(
        'filename'   => array('type' => 'varchar', 'length' => 255, 'not null' => TRUE),
        'hash'   => array('type' => 'varchar', 'length' => 64, 'not null' => TRUE),
      ),
      'primary key' => array('filename'),
    );
    db_create_table('registry_file', $schema['registry_file']);
  }

  // Older versions of Drupal 6 do not include the semaphore table, which is
  // required to bootstrap, so we add it now so that we can bootstrap and
  // provide a reasonable error message.
  if (!db_table_exists('semaphore')) {
    $semaphore = array(
      'description' => 'Table for holding semaphores, locks, flags, etc. that cannot be stored as Drupal variables since they must not be cached.',
      'fields' => array(
        'name' => array(
          'description' => 'Primary Key: Unique name.',
          'type' => 'varchar',
          'length' => 255,
          'not null' => TRUE,
          'default' => ''
        ),
        'value' => array(
          'description' => 'A value for the semaphore.',
          'type' => 'varchar',
          'length' => 255,
          'not null' => TRUE,
          'default' => ''
        ),
        'expire' => array(
          'description' => 'A Unix timestamp with microseconds indicating when the semaphore should expire.',
          'type' => 'float',
          'size' => 'big',
          'not null' => TRUE
        ),
      ),
      'indexes' => array(
        'value' => array('value'),
        'expire' => array('expire'),
      ),
      'primary key' => array('name'),
    );
    db_create_table('semaphore', $semaphore);
  }

  // The new cache_bootstrap bin is required to bootstrap to
  // DRUPAL_BOOTSTRAP_SESSION, so create it here rather than in
  // update_fix_d7_requirements().
  if (!db_table_exists('cache_bootstrap')) {
    $cache_bootstrap = array(
      'description' => 'Cache table for data required to bootstrap Drupal, may be routed to a shared memory cache.',
      'fields' => array(
        'cid' => array(
          'description' => 'Primary Key: Unique cache ID.',
          'type' => 'varchar',
          'length' => 255,
          'not null' => TRUE,
          'default' => '',
        ),
        'data' => array(
          'description' => 'A collection of data to cache.',
          'type' => 'blob',
          'not null' => FALSE,
          'size' => 'big',
        ),
        'expire' => array(
          'description' => 'A Unix timestamp indicating when the cache entry should expire, or 0 for never.',
          'type' => 'int',
          'not null' => TRUE,
          'default' => 0,
        ),
        'created' => array(
          'description' => 'A Unix timestamp indicating when the cache entry was created.',
          'type' => 'int',
          'not null' => TRUE,
          'default' => 0,
        ),
        'serialized' => array(
          'description' => 'A flag to indicate whether content is serialized (1) or not (0).',
          'type' => 'int',
          'size' => 'small',
          'not null' => TRUE,
          'default' => 0,
        ),
      ),
      'indexes' => array(
        'expire' => array('expire'),
      ),
      'primary key' => array('cid'),
    );
    db_create_table('cache_bootstrap', $cache_bootstrap);
  }

  // Set a valid timezone for 6 -> 7 upgrade process.
  drupal_bootstrap(DRUPAL_BOOTSTRAP_VARIABLES);
  $timezone_offset = variable_get('date_default_timezone', 0);
  if (is_numeric($timezone_offset)) {
    // Save the original offset.
    variable_set('date_temporary_timezone', $timezone_offset);
    // Set the timezone for this request only.
    $GLOBALS['conf']['date_default_timezone'] = 'UTC';
  }

  // This allows update functions to tell if an upgrade from D6 is running.
  if (!empty($update_d6)) {
    variable_set('update_d6', TRUE);
  }
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
