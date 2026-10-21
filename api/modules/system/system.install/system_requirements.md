# system_requirements()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 11–592 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L11-L592)
- **Module/theme:** system
- **Implements:** [hook_requirements()](../system.api.php/hook_requirements.md)

## Signature

```php
function system_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().
```

## Code

```php
function system_requirements($phase) {
  global $base_url;
  $requirements = array();
  // Ensure translations don't break during installation.
  $t = get_t();

  // Report Drupal version
  if ($phase == 'runtime') {
    $requirements['drupal'] = array(
      'title' => $t('Drupal'),
      'value' => VERSION,
      'severity' => REQUIREMENT_INFO,
      'weight' => -10,
    );

    // Display the currently active installation profile, if the site
    // is not running the default installation profile.
    $profile = drupal_get_profile();
    if ($profile != 'standard') {
      $info = system_get_info('module', $profile);
      $requirements['install_profile'] = array(
        'title' => $t('Install profile'),
        'value' => $t('%profile_name (%profile-%version)', array(
          '%profile_name' => $info['name'],
          '%profile' => $profile,
          '%version' => $info['version']
        )),
        'severity' => REQUIREMENT_INFO,
        'weight' => -9
      );
    }
  }

  // Web server information.
  $software = $_SERVER['SERVER_SOFTWARE'];
  $requirements['webserver'] = array(
    'title' => $t('Web server'),
    'value' => $software,
  );

  // Test PHP version and show link to phpinfo() if it's available
  $phpversion = phpversion();
  if (function_exists('phpinfo')) {
    $requirements['php'] = array(
      'title' => $t('PHP'),
      'value' => ($phase == 'runtime') ? $phpversion .' ('. l($t('more information'), 'admin/reports/status/php') .')' : $phpversion,
    );
  }
  else {
    $requirements['php'] = array(
      'title' => $t('PHP'),
      'value' => $phpversion,
      'description' => $t('The phpinfo() function has been disabled for security reasons. To see your server\'s phpinfo() information, change your PHP settings or contact your server administrator. For more information, <a href="@phpinfo">Enabling and disabling phpinfo()</a> handbook page.', array('@phpinfo' => 'http://drupal.org/node/243993')),
      'severity' => REQUIREMENT_INFO,
    );
  }

  if (version_compare($phpversion, DRUPAL_MINIMUM_PHP) < 0) {
    $requirements['php']['description'] = $t('Your PHP installation is too old. Drupal requires at least PHP %version.', array('%version' => DRUPAL_MINIMUM_PHP));
    $requirements['php']['severity'] = REQUIREMENT_ERROR;
    // If PHP is old, it's not safe to continue with the requirements check.
    return $requirements;
  }
  // Check that htmlspecialchars() is secure if the site is running any PHP
  // version older than 5.2.5. We don't simply require 5.2.5, because Ubuntu
  // 8.04 ships with PHP 5.2.4, but includes the necessary security patch.
  elseif (version_compare($phpversion, '5.2.5') < 0 && strlen(@htmlspecialchars(chr(0xC0) . chr(0xAF), ENT_QUOTES, 'UTF-8'))) {
    $requirements['php']['description'] = $t('Your PHP installation is too old. Drupal requires at least PHP 5.2.5, or PHP @version with the htmlspecialchars security patch backported.', array('@version' => DRUPAL_MINIMUM_PHP));
    $requirements['php']['severity'] = REQUIREMENT_ERROR;
    // If PHP is old, it's not safe to continue with the requirements check.
    return $requirements;
  }

  // Test PHP register_globals setting.
  $requirements['php_register_globals'] = array(
    'title' => $t('PHP register globals'),
  );
  $register_globals = trim(ini_get('register_globals'));
  // Unfortunately, ini_get() may return many different values, and we can't
  // be certain which values mean 'on', so we instead check for 'not off'
  // since we never want to tell the user that their site is secure
  // (register_globals off), when it is in fact on. We can only guarantee
  // register_globals is off if the value returned is 'off', '', or 0.
  if (!empty($register_globals) && strtolower($register_globals) != 'off') {
    $requirements['php_register_globals']['description'] = $t('<em>register_globals</em> is enabled. Drupal requires this configuration directive to be disabled. Your site may not be secure when <em>register_globals</em> is enabled. The PHP manual has instructions for <a href="http://php.net/configuration.changes">how to change configuration settings</a>.');
    $requirements['php_register_globals']['severity'] = REQUIREMENT_ERROR;
    $requirements['php_register_globals']['value'] = $t("Enabled ('@value')", array('@value' => $register_globals));
  }
  else {
    $requirements['php_register_globals']['value'] = $t('Disabled');
  }

  // Test for PHP extensions.
  $requirements['php_extensions'] = array(
    'title' => $t('PHP extensions'),
  );

  $missing_extensions = array();
  $required_extensions = array(
    'date',
    'dom',
    'filter',
    'gd',
    'hash',
    'json',
    'pcre',
    'pdo',
    'session',
    'SimpleXML',
    'SPL',
    'xml',
  );
  foreach ($required_extensions as $extension) {
    if (!extension_loaded($extension)) {
      $missing_extensions[] = $extension;
    }
  }

  if (!empty($missing_extensions)) {
    $description = $t('Drupal requires you to enable the PHP extensions in the following list (see the <a href="@system_requirements">system requirements page</a> for more information):', array(
      '@system_requirements' => 'http://drupal.org/requirements',
    ));

    $description .= theme('item_list', array('items' => $missing_extensions));

    $requirements['php_extensions']['value'] = $t('Disabled');
    $requirements['php_extensions']['severity'] = REQUIREMENT_ERROR;
    $requirements['php_extensions']['description'] = $description;
  }
  else {
    $requirements['php_extensions']['value'] = $t('Enabled');
  }

  if ($phase == 'install' || $phase == 'update') {
    // Test for PDO (database).
    $requirements['database_extensions'] = array(
      'title' => $t('Database support'),
    );

    // Make sure PDO is available.
    $database_ok = extension_loaded('pdo');
    if (!$database_ok) {
      $pdo_message = $t('Your web server does not appear to support PDO (PHP Data Objects). Ask your hosting provider if they support the native PDO extension. See the <a href="@link">system requirements</a> page for more information.', array(
        '@link' => 'http://drupal.org/requirements/pdo',
      ));
    }
    else {
      // Make sure at least one supported database driver exists.
      $drivers = drupal_detect_database_types();
      if (empty($drivers)) {
        $database_ok = FALSE;
        $pdo_message = $t('Your web server does not appear to support any common PDO database extensions. Check with your hosting provider to see if they support PDO (PHP Data Objects) and offer any databases that <a href="@drupal-databases">Drupal supports</a>.', array(
          '@drupal-databases' => 'https://www.drupal.org/requirements/database',
        ));
      }
      // Make sure the native PDO extension is available, not the older PEAR
      // version. (See install_verify_pdo() for details.)
      if (!defined('PDO::ATTR_DEFAULT_FETCH_MODE')) {
        $database_ok = FALSE;
        $pdo_message = $t('Your web server seems to have the wrong version of PDO installed. Drupal 7 requires the PDO extension from PHP core. This system has the older PECL version. See the <a href="@link">system requirements</a> page for more information.', array(
          '@link' => 'http://drupal.org/requirements/pdo#pecl',
        ));
      }
    }

    if (!$database_ok) {
      $requirements['database_extensions']['value'] = $t('Disabled');
      $requirements['database_extensions']['severity'] = REQUIREMENT_ERROR;
      $requirements['database_extensions']['description'] = $pdo_message;
    }
    else {
      $requirements['database_extensions']['value'] = $t('Enabled');
    }
  }
  else {
    // Database information.
    $class = 'DatabaseTasks_' . Database::getConnection()->driver();
    $tasks = new $class();
    $requirements['database_system'] = array(
      'title' => $t('Database system'),
      'value' => $tasks->name(),
    );
    $requirements['database_system_version'] = array(
      'title' => $t('Database system version'),
      'value' => Database::getConnection()->version(),
    );
  }

  // Test database-specific multi-byte UTF-8 related requirements.
  $charset_requirements = _system_check_db_utf8mb4_requirements($phase);
  if (!empty($charset_requirements)) {
    $requirements['database_charset'] = $charset_requirements;
  }

  // Test PHP memory_limit
  $memory_limit = ini_get('memory_limit');
  $requirements['php_memory_limit'] = array(
    'title' => $t('PHP memory limit'),
    'value' => $memory_limit == -1 ? t('-1 (Unlimited)') : $memory_limit,
  );

  if (!drupal_check_memory_limit(DRUPAL_MINIMUM_PHP_MEMORY_LIMIT, $memory_limit)) {
    $description = '';
    if ($phase == 'install') {
      $description = $t('Consider increasing your PHP memory limit to %memory_minimum_limit to help prevent errors in the installation process.', array('%memory_minimum_limit' => DRUPAL_MINIMUM_PHP_MEMORY_LIMIT));
    }
    elseif ($phase == 'update') {
      $description = $t('Consider increasing your PHP memory limit to %memory_minimum_limit to help prevent errors in the update process.', array('%memory_minimum_limit' => DRUPAL_MINIMUM_PHP_MEMORY_LIMIT));
    }
    elseif ($phase == 'runtime') {
      $description = $t('Depending on your configuration, Drupal can run with a %memory_limit PHP memory limit. However, a %memory_minimum_limit PHP memory limit or above is recommended, especially if your site uses additional custom or contributed modules.', array('%memory_limit' => $memory_limit, '%memory_minimum_limit' => DRUPAL_MINIMUM_PHP_MEMORY_LIMIT));
    }

    if (!empty($description)) {
      if ($php_ini_path = get_cfg_var('cfg_file_path')) {
        $description .= ' ' . $t('Increase the memory limit by editing the memory_limit parameter in the file %configuration-file and then restart your web server (or contact your system administrator or hosting provider for assistance).', array('%configuration-file' => $php_ini_path));
      }
      else {
        $description .= ' ' . $t('Contact your system administrator or hosting provider for assistance with increasing your PHP memory limit.');
      }

      $requirements['php_memory_limit']['description'] = $description . ' ' . $t('See the <a href="@url">Drupal requirements</a> for more information.', array('@url' => 'http://drupal.org/requirements'));
      $requirements['php_memory_limit']['severity'] = REQUIREMENT_WARNING;
    }
  }

  // Test settings.php file writability
  if ($phase == 'runtime') {
    $conf_errors = array();
    // Allow system administrators to ignore permissions hardening for the site
    // directory. This allows additional files in the site directory to be
    // updated when they are managed in a version control system.
    $skip_permissions_hardening = variable_get('skip_permissions_hardening', FALSE);

    if ($skip_permissions_hardening) {
      $error_value = t('Protection disabled');
      // If permissions hardening is disabled, then only show a warning for a
      // writable file, as a reminder, rather than an error.
      $file_protection_severity = REQUIREMENT_WARNING;
    }
    else {
      $error_value = t('Not protected');
      // In normal operation, writable files or directories are an error.
      $file_protection_severity = REQUIREMENT_ERROR;
      if (!drupal_verify_install_file(conf_path(), FILE_NOT_WRITABLE, 'dir')) {
        $conf_errors[] = $t('The directory %file is not protected from modifications and poses a security risk. You must change the directory\'s permissions to be non-writable. ', array('%file' => conf_path()));
      }
    }
    if (!drupal_verify_install_file(conf_path() . '/settings.php', FILE_EXIST | FILE_READABLE | FILE_NOT_WRITABLE, 'file', !$skip_permissions_hardening)) {
      $conf_errors[] = $t('The file %file is not protected from modifications and poses a security risk. You must change the file\'s permissions to be non-writable.', array('%file' => conf_path() . '/settings.php'));
    }

    if (!empty($conf_errors)) {
      $requirements['settings.php'] = array(
        'value' => $error_value,
        'severity' => $file_protection_severity,
        'description' => implode('<br />', $conf_errors),
      );
    }
    else {
      $requirements['settings.php'] = array(
        'value' => $t('Protected'),
      );
    }
    $requirements['settings.php']['title'] = $t('Configuration file');
  }

  // Test the contents of the .htaccess files.
  if ($phase == 'runtime') {
    // Try to write the .htaccess files first, to prevent false alarms in case
    // (for example) the /tmp directory was wiped.
    file_ensure_htaccess();
    $htaccess_files['public://.htaccess'] = array(
      'title' => $t('Public files directory'),
      'directory' => variable_get('file_public_path', conf_path() . '/files'),
    );
    if ($private_files_directory = variable_get('file_private_path')) {
      $htaccess_files['private://.htaccess'] = array(
        'title' => $t('Private files directory'),
        'directory' => $private_files_directory,
      );
    }
    $htaccess_files['temporary://.htaccess'] = array(
      'title' => $t('Temporary files directory'),
      'directory' => variable_get('file_temporary_path', file_directory_temp()),
    );
    foreach ($htaccess_files as $htaccess_file => $info) {
      // Check for the string which was added to the recommended .htaccess file
      // in the latest security update.
      if (!file_exists($htaccess_file) || !($contents = @file_get_contents($htaccess_file)) || strpos($contents, 'Drupal_Security_Do_Not_Remove_See_SA_2013_003') === FALSE) {
        $requirements[$htaccess_file] = array(
          'title' => $info['title'],
          'value' => $t('Not fully protected'),
          'severity' => REQUIREMENT_ERROR,
          'description' => $t('See <a href="@url">@url</a> for information about the recommended .htaccess file which should be added to the %directory directory to help protect against arbitrary code execution.', array('@url' => 'http://drupal.org/SA-CORE-2013-003', '%directory' => $info['directory'])),
        );
      }
    }
  }

  // Report cron status.
  if ($phase == 'runtime') {
    // Cron warning threshold defaults to two days.
    $threshold_warning = variable_get('cron_threshold_warning', 172800);
    // Cron error threshold defaults to two weeks.
    $threshold_error = variable_get('cron_threshold_error', 1209600);
    // Cron configuration help text.
    $help = $t('For more information, see the online handbook entry for <a href="@cron-handbook">configuring cron jobs</a>.', array('@cron-handbook' => 'http://drupal.org/cron'));

    // Determine when cron last ran.
    $cron_last = variable_get('cron_last');
    if (!is_numeric($cron_last)) {
      $cron_last = variable_get('install_time', 0);
    }

    // Determine severity based on time since cron last ran.
    $severity = REQUIREMENT_OK;
    if (REQUEST_TIME - $cron_last > $threshold_error) {
      $severity = REQUIREMENT_ERROR;
    }
    elseif (REQUEST_TIME - $cron_last > $threshold_warning) {
      $severity = REQUIREMENT_WARNING;
    }

    // Set summary and description based on values determined above.
    $summary = $t('Last run !time ago', array('!time' => format_interval(REQUEST_TIME - $cron_last)));
    $description = '';
    if ($severity != REQUIREMENT_OK) {
      $description = $t('Cron has not run recently.') . ' ' . $help;
    }

    $description .= ' ' . $t('You can <a href="@cron">run cron manually</a>.', array('@cron' => url('admin/reports/status/run-cron', array('query' => array('token' => drupal_get_token('run-cron'))))));
    $description .= '<br />' . $t('To run cron from outside the site, go to <a href="!cron">!cron</a>', array('!cron' => url($base_url . '/cron.php', array('external' => TRUE, 'query' => array('cron_key' => variable_get('cron_key', 'drupal'))))));

    $requirements['cron'] = array(
      'title' => $t('Cron maintenance tasks'),
      'severity' => $severity,
      'value' => $summary,
      'description' => $description
    );
  }

  // Test files directories.
  $directories = array(
    variable_get('file_public_path', conf_path() . '/files'),
    // By default no private files directory is configured. For private files
    // to be secure the admin needs to provide a path outside the webroot.
    variable_get('file_private_path', FALSE),
  );

  // Do not check for the temporary files directory during installation
  // unless it has been set in settings.php. In this case the user has
  // no alternative but to fix the directory if it is not writable.
  if ($phase == 'install') {
    $directories[] = variable_get('file_temporary_path', FALSE);
  }
  else {
    $directories[] = variable_get('file_temporary_path', file_directory_temp());
  }

  $requirements['file system'] = array(
    'title' => $t('File system'),
  );

  $error = '';
  // For installer, create the directories if possible.
  foreach ($directories as $directory) {
    if (!$directory) {
      continue;
    }
    if ($phase == 'install') {
      file_prepare_directory($directory, FILE_CREATE_DIRECTORY);
    }
    $is_writable = is_writable($directory);
    $is_directory = is_dir($directory);
    if (!$is_writable || !$is_directory) {
      $description = '';
      $requirements['file system']['value'] = $t('Not writable');
      if (!$is_directory) {
        $error .= $t('The directory %directory does not exist.', array('%directory' => $directory)) . ' ';
      }
      else {
        $error .= $t('The directory %directory is not writable.', array('%directory' => $directory)) . ' ';
      }
      // The files directory requirement check is done only during install and runtime.
      if ($phase == 'runtime') {
        $description = $error . $t('You may need to set the correct directory at the <a href="@admin-file-system">file system settings page</a> or change the current directory\'s permissions so that it is writable.', array('@admin-file-system' => url('admin/config/media/file-system')));
      }
      elseif ($phase == 'install') {
        // For the installer UI, we need different wording. 'value' will
        // be treated as version, so provide none there.
        $description = $error . $t('An automated attempt to create this directory failed, possibly due to a permissions problem. To proceed with the installation, either create the directory and modify its permissions manually or ensure that the installer has the permissions to create it automatically. For more information, see INSTALL.txt or the <a href="@handbook_url">online handbook</a>.', array('@handbook_url' => 'http://drupal.org/server-permissions'));
        $requirements['file system']['value'] = '';
      }
      if (!empty($description)) {
        $requirements['file system']['description'] = $description;
        $requirements['file system']['severity'] = REQUIREMENT_ERROR;
      }
    }
    else {
      if (file_default_scheme() == 'public') {
        $requirements['file system']['value'] = $t('Writable (<em>public</em> download method)');
      }
      else {
        $requirements['file system']['value'] = $t('Writable (<em>private</em> download method)');
      }
    }
  }

  // See if updates are available in update.php.
  if ($phase == 'runtime') {
    $requirements['update'] = array(
      'title' => $t('Database updates'),
      'severity' => REQUIREMENT_OK,
      'value' => $t('Up to date'),
    );

    // Check installed modules.
    foreach (module_list() as $module) {
      $updates = drupal_get_schema_versions($module);
      if ($updates !== FALSE) {
        $default = drupal_get_installed_schema_version($module);
        if (max($updates) > $default) {
          $requirements['update']['severity'] = REQUIREMENT_ERROR;
          $requirements['update']['value'] = $t('Out of date');
          $requirements['update']['description'] = $t('Some modules have database schema updates to install. You should run the <a href="@update">database update script</a> immediately.', array('@update' => base_path() . 'update.php'));
          break;
        }
      }
    }
  }

  // Verify the update.php access setting
  if ($phase == 'runtime') {
    if (!empty($GLOBALS['update_free_access'])) {
      $requirements['update access'] = array(
        'value' => $t('Not protected'),
        'severity' => REQUIREMENT_ERROR,
        'description' => $t('The update.php script is accessible to everyone without authentication check, which is a security risk. You must change the $update_free_access value in your settings.php back to FALSE.'),
      );
    }
    else {
      $requirements['update access'] = array(
        'value' => $t('Protected'),
      );
    }
    $requirements['update access']['title'] = $t('Access to update.php');
  }

  // Display an error if a newly introduced dependency in a module is not resolved.
  if ($phase == 'update') {
    $profile = drupal_get_profile();
    $files = system_rebuild_module_data();
    foreach ($files as $module => $file) {
      // Ignore disabled modules and installation profiles.
      if (!$file->status || $module == $profile) {
        continue;
      }
      // Check the module's PHP version.
      $name = $file->info['name'];
      $php = $file->info['php'];
      if (version_compare($php, PHP_VERSION, '>')) {
        $requirements['php']['description'] .= $t('@name requires at least PHP @version.', array('@name' => $name, '@version' => $php));
        $requirements['php']['severity'] = REQUIREMENT_ERROR;
      }
      // Check the module's required modules.
      foreach ($file->requires as $requirement) {
        $required_module = $requirement['name'];
        // Check if the module exists.
        if (!isset($files[$required_module])) {
          $requirements["$module-$required_module"] = array(
            'title' => $t('Unresolved dependency'),
            'description' => $t('@name requires this module.', array('@name' => $name)),
            'value' => t('@required_name (Missing)', array('@required_name' => $required_module)),
            'severity' => REQUIREMENT_ERROR,
          );
          continue;
        }
        // Check for an incompatible version.
        $required_file = $files[$required_module];
        $required_name = $required_file->info['name'];
        $version = str_replace(DRUPAL_CORE_COMPATIBILITY . '-', '', (string) $required_file->info['version']);
        $compatibility = drupal_check_incompatibility($requirement, $version);
        if ($compatibility) {
          $compatibility = rtrim(substr($compatibility, 2), ')');
          $requirements["$module-$required_module"] = array(
            'title' => $t('Unresolved dependency'),
            'description' => $t('@name requires this module and version. Currently using @required_name version @version', array('@name' => $name, '@required_name' => $required_name, '@version' => $version)),
            'value' => t('@required_name (Version @compatibility required)', array('@required_name' => $required_name, '@compatibility' => $compatibility)),
            'severity' => REQUIREMENT_ERROR,
          );
          continue;
        }
      }
    }
  }

  // Test Unicode library
  include_once DRUPAL_ROOT . '/includes/unicode.inc';
  $requirements = array_merge($requirements, unicode_requirements());

  if ($phase == 'runtime') {
    // Check for update status module.
    if (!module_exists('update')) {
      $requirements['update status'] = array(
        'value' => $t('Not enabled'),
        'severity' => REQUIREMENT_WARNING,
        'description' => $t('Update notifications are not enabled. It is <strong>highly recommended</strong> that you enable the update manager module from the <a href="@module">module administration page</a> in order to stay up-to-date on new releases. For more information, <a href="@update">Update status handbook page</a>.', array('@update' => 'http://drupal.org/documentation/modules/update', '@module' => url('admin/modules'))),
      );
    }
    else {
      $requirements['update status'] = array(
        'value' => $t('Enabled'),
      );
    }
    $requirements['update status']['title'] = $t('Update notifications');

    // Check that Drupal can issue HTTP requests.
    if (variable_get('drupal_http_request_fails', TRUE) && !system_check_http_request()) {
      $requirements['http requests'] = array(
        'title' => $t('HTTP request status'),
        'value' => $t('Fails'),
        'severity' => REQUIREMENT_ERROR,
        'description' => $t('Your system or network configuration does not allow Drupal to access web pages, resulting in reduced functionality. This could be due to your webserver configuration or PHP settings, and should be resolved in order to download information about available updates, fetch aggregator feeds, sign in via OpenID, or use other network-dependent services. If you are certain that Drupal can access web pages but you are still seeing this message, you may add <code>$conf[\'drupal_http_request_fails\'] = FALSE;</code> to the bottom of your settings.php file.'),
      );
    }
  }

  // Warning for httpoxy on IIS with affected PHP versions.
  // @see https://www.drupal.org/node/2783079
  if (strpos((string) $software, 'Microsoft-IIS') !== FALSE && (version_compare(PHP_VERSION, '5.5.38', '<')
    || (version_compare(PHP_VERSION, '5.6.0', '>=') && version_compare(PHP_VERSION, '5.6.24', '<'))
    || (version_compare(PHP_VERSION, '7.0.0', '>=') && version_compare(PHP_VERSION, '7.0.9', '<'))
    )) {
    $dom = new \DOMDocument('1.0', 'UTF-8');
    $webconfig = file_get_contents('web.config');
    // If you are here the web.config file must - of course - be well formed.
    // But the PHP DOM component will throw warnings on some XML compliant
    // stuff, so silently parse the configuration file.
    @$dom->loadHTML($webconfig);
    $httpoxy_rewrite = FALSE;
    foreach ($dom->getElementsByTagName('rule') as $rule) {
      foreach ($rule->attributes as $attr) {
        if (@$attr->name == 'name' && @$attr->nodeValue == 'Erase HTTP_PROXY') {
          $httpoxy_rewrite = TRUE;
          break 2;
        }
      }
    }
    if (!$httpoxy_rewrite) {
      $requirements['iis_httpoxy_protection'] = array(
        'title' => t('IIS httpoxy protection'),
        'value' => t('Your PHP runtime version is affected by the httpoxy vulnerability.'),
        'description' => t('Either update your PHP runtime version or uncomment the "Erase HTTP_PROXY" rule in your web.config file and add HTTP_PROXY to the allowed headers list. See more details in the <a href="@link">security advisory</a>.', array('@link' => 'https://www.drupal.org/SA-CORE-2016-003')),
        'severity' => REQUIREMENT_ERROR,
      );
    }
  }

  // See if trusted hostnames have been configured, and warn the user if they
  // are not set.
  if ($phase == 'runtime') {
    $trusted_host_patterns = variable_get('trusted_host_patterns', array());
    if (empty($trusted_host_patterns)) {
      $requirements['trusted_host_patterns'] = array(
        'title' => $t('Trusted Host Settings'),
        'value' => $t('Not enabled'),
        'description' => $t('The trusted_host_patterns setting is not configured in settings.php. This can lead to security vulnerabilities. It is <strong>highly recommended</strong> that you configure this. See <a href="@url">Protecting against HTTP HOST Header attacks</a> for more information.', array('@url' => 'https://www.drupal.org/node/1992030')),
        'severity' => REQUIREMENT_ERROR,
      );
    }
    else {
      $requirements['trusted_host_patterns'] = array(
        'title' => $t('Trusted Host Settings'),
        'value' => $t('Enabled'),
        'description' => $t('The trusted_host_patterns setting is set to allow %trusted_host_patterns', array('%trusted_host_patterns' => implode(', ', $trusted_host_patterns))),
      );
    }
  }

  return $requirements;
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
