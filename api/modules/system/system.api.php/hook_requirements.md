# hook_requirements()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3139–3184 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3139-L3184)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_requirements($phase)
```

## Documentation

```text
Check installation requirements and do status reporting.

This hook has three closely related uses, determined by the $phase argument:
- Checking installation requirements ($phase == 'install').
- Checking update requirements ($phase == 'update').
- Status reporting ($phase == 'runtime').

Note that this hook, like all others dealing with installation and updates,
must reside in a module_name.install file, or it will not properly abort
the installation of the module if a critical requirement is missing.

During the 'install' phase, modules can for example assert that
library or server versions are available or sufficient.
Note that the installation of a module can happen during installation of
Drupal itself (by install.php) with an installation profile or later by hand.
As a consequence, install-time requirements must be checked without access
to the full Drupal API, because it is not available during install.php.
For localization you should for example use $t = get_t() to
retrieve the appropriate localization function name (t() or st()).
If a requirement has a severity of REQUIREMENT_ERROR, install.php will abort
or at least the module will not install.
Other severity levels have no effect on the installation.
Module dependencies do not belong to these installation requirements,
but should be defined in the module's .info file.

The 'runtime' phase is not limited to pure installation requirements
but can also be used for more general status information like maintenance
tasks and security issues.
The returned 'requirements' will be listed on the status report in the
administration section, with indication of the severity level.
Moreover, any requirement with a severity of REQUIREMENT_ERROR severity will
result in a notice on the administration configuration page.

@param $phase
  The phase in which requirements are checked:
  - install: The module is being installed.
  - update: The module is enabled and update.php is run.
  - runtime: The runtime requirements are being checked and shown on the
    status report page.

@return
  An associative array where the keys are arbitrary but must be unique (it
  is suggested to use the module short name as a prefix) and the values are
  themselves associative arrays with the following elements:
  - title: The name of the requirement.
  - value: The current value (e.g., version, time, level, etc). During
    install phase, this should only be used for version numbers, do not set
    it if not applicable.
  - description: The description of the requirement/status.
  - severity: The requirement's result/severity level, one of:
    - REQUIREMENT_INFO: For info only.
    - REQUIREMENT_OK: The requirement is satisfied.
    - REQUIREMENT_WARNING: The requirement failed with a warning.
    - REQUIREMENT_ERROR: The requirement failed with an error.
```

## Code

```php
function hook_requirements($phase) {
  $requirements = array();
  // Ensure translations don't break during installation.
  $t = get_t();

  // Report Drupal version
  if ($phase == 'runtime') {
    $requirements['drupal'] = array(
      'title' => $t('Drupal'),
      'value' => VERSION,
      'severity' => REQUIREMENT_INFO
    );
  }

  // Test PHP version
  $requirements['php'] = array(
    'title' => $t('PHP'),
    'value' => ($phase == 'runtime') ? l(phpversion(), 'admin/reports/status/php') : phpversion(),
  );
  if (version_compare(phpversion(), DRUPAL_MINIMUM_PHP) < 0) {
    $requirements['php']['description'] = $t('Your PHP installation is too old. Drupal requires at least PHP %version.', array('%version' => DRUPAL_MINIMUM_PHP));
    $requirements['php']['severity'] = REQUIREMENT_ERROR;
  }

  // Report cron status
  if ($phase == 'runtime') {
    $cron_last = variable_get('cron_last');

    if (is_numeric($cron_last)) {
      $requirements['cron']['value'] = $t('Last run !time ago', array('!time' => format_interval(REQUEST_TIME - $cron_last)));
    }
    else {
      $requirements['cron'] = array(
        'description' => $t('Cron has not run. It appears cron jobs have not been setup on your system. Check the help pages for <a href="@url">configuring cron jobs</a>.', array('@url' => 'http://drupal.org/cron')),
        'severity' => REQUIREMENT_ERROR,
        'value' => $t('Never run'),
      );
    }

    $requirements['cron']['description'] .= ' ' . $t('You can <a href="@cron">run cron manually</a>.', array('@cron' => url('admin/reports/status/run-cron', array('query' => array('token' => drupal_get_token('run-cron'))))));

    $requirements['cron']['title'] = $t('Cron maintenance tasks');
  }

  return $requirements;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_requirements()".

- [requirements1_test_requirements()](../../simpletest/tests/requirements1_test.install/requirements1_test_requirements.md) — `modules/simpletest/tests/requirements1_test.install`
- [update_script_test_requirements()](../../simpletest/tests/update_script_test.install/update_script_test_requirements.md) — `modules/simpletest/tests/update_script_test.install`
- [color_requirements()](../../color/color.install/color_requirements.md) — `modules/color/color.install`
- [file_requirements()](../../file/file.install/file_requirements.md) — `modules/file/file.install`
- [image_requirements()](../../image/image.install/image_requirements.md) — `modules/image/image.install`
- [node_requirements()](../../node/node.module/node_requirements.md) — `modules/node/node.module`
- [openid_requirements()](../../openid/openid.install/openid_requirements.md) — `modules/openid/openid.install`
- [simpletest_requirements()](../../simpletest/simpletest.install/simpletest_requirements.md) — `modules/simpletest/simpletest.install`
- [system_requirements()](../system.install/system_requirements.md) — `modules/system/system.install`
- [update_requirements()](../../update/update.install/update_requirements.md) — `modules/update/update.install`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
