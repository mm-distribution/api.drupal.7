# drupal_check_module()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1230–1250 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1230-L1250)

## Signature

```php
function drupal_check_module($module)
```

## Documentation

```text
Checks a module's requirements.

@param $module
  Machine name of module to check.

@return
  TRUE or FALSE, depending on whether the requirements are met.
```

## Code

```php
function drupal_check_module($module) {
  module_load_install($module);
  if (module_hook($module, 'requirements')) {
    // Check requirements
    $requirements = module_invoke($module, 'requirements', 'install');
    if (is_array($requirements) && drupal_requirements_severity($requirements) == REQUIREMENT_ERROR) {
      // Print any error messages
      foreach ($requirements as $requirement) {
        if (isset($requirement['severity']) && $requirement['severity'] == REQUIREMENT_ERROR) {
          $message = $requirement['description'];
          if (isset($requirement['value']) && $requirement['value']) {
            $message .= ' (' . t('Currently using !item !version', array('!item' => $requirement['title'], '!version' => $requirement['value'])) . ')';
          }
          drupal_set_message($message, 'error');
        }
      }
      return FALSE;
    }
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
