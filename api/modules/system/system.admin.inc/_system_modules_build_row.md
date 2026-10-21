# _system_modules_build_row()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 983–1064 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L983-L1064)
- **Module/theme:** system

## Signature

```php
function _system_modules_build_row($info, $extra)
```

## Documentation

```text
Build a table row for the system modules page.
```

## Code

```php
function _system_modules_build_row($info, $extra) {
  // Add in the defaults.
  $extra += array(
    'requires' => array(),
    'required_by' => array(),
    'disabled' => FALSE,
    'enabled' => FALSE,
    'links' => array(),
  );
  $form = array(
    '#tree' => TRUE,
  );
  // Set the basic properties.
  $form['name'] = array(
    '#markup' => $info['name'],
  );
  $form['description'] = array(
    '#markup' => t($info['description']),
  );
  $form['version'] = array(
    '#markup' => $info['version'],
  );
  $form['#requires'] = $extra['requires'];
  $form['#required_by'] = $extra['required_by'];

  // Check the compatibilities.
  $compatible = TRUE;
  $status_short = '';
  $status_long = '';

  // Initialize empty arrays of long and short reasons explaining why the
  // module is incompatible.
  // Add each reason as a separate element in both the arrays.
  $reasons_short = array();
  $reasons_long = array();

  // Check the core compatibility.
  if (!isset($info['core']) || $info['core'] != DRUPAL_CORE_COMPATIBILITY) {
    $compatible = FALSE;
    $reasons_short[] = t('Incompatible with this version of Drupal core.');
    $reasons_long[] = t('This version is not compatible with Drupal !core_version and should be replaced.', array('!core_version' => DRUPAL_CORE_COMPATIBILITY));
  }

  // Ensure this module is compatible with the currently installed version of PHP.
  if (version_compare(phpversion(), $info['php']) < 0) {
    $compatible = FALSE;
    $reasons_short[] = t('Incompatible with this version of PHP');
    $php_required = $info['php'];
    if (substr_count($info['php'], '.') < 2) {
      $php_required .= '.*';
    }
    $reasons_long[] = t('This module requires PHP version @php_required and is incompatible with PHP version !php_version.', array('@php_required' => $php_required, '!php_version' => phpversion()));
  }

  // If this module is compatible, present a checkbox indicating
  // this module may be installed. Otherwise, show a big red X.
  if ($compatible) {
    $form['enable'] = array(
      '#type' => 'checkbox',
      '#title' => t('Enable'),
      '#default_value' => $extra['enabled'],
    );
    if ($extra['disabled']) {
      $form['enable']['#disabled'] = TRUE;
    }
  }
  else {
    $status_short = implode(' ', $reasons_short);
    $status_long = implode(' ', $reasons_long);
    $form['enable'] = array(
      '#markup' =>  theme('image', array('path' => 'misc/watchdog-error.png', 'alt' => $status_short, 'title' => $status_short)),
    );
    $form['description']['#markup'] .= theme('system_modules_incompatible', array('message' => $status_long));
  }

  // Build operation links.
  foreach (array('help', 'permissions', 'configure') as $key) {
    $form['links'][$key] = (isset($extra['links'][$key]) ? $extra['links'][$key] : array());
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
