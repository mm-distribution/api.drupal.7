# install_verify_requirements()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 741–777 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L741-L777)

## Signature

```php
function install_verify_requirements(&$install_state)
```

## Documentation

```text
Verifies the requirements for installing Drupal.

@param $install_state
  An array of information about the current installation state.

@return
  A themed status report, or an exception if there are requirement errors.
  If there are only requirement warnings, a themed status report is shown
  initially, but the user is allowed to bypass it by providing 'continue=1'
  in the URL. Otherwise, no output is returned, so that the next task can be
  run in the same page request.
```

## Code

```php
function install_verify_requirements(&$install_state) {
  // Check the installation requirements for Drupal and this profile.
  $requirements = install_check_requirements($install_state);

  // Verify existence of all required modules.
  $requirements += drupal_verify_profile($install_state);

  // Check the severity of the requirements reported.
  $severity = drupal_requirements_severity($requirements);

  // If there are errors, always display them. If there are only warnings, skip
  // them if the user has provided a URL parameter acknowledging the warnings
  // and indicating a desire to continue anyway. See drupal_requirements_url().
  if ($severity == REQUIREMENT_ERROR || ($severity == REQUIREMENT_WARNING && empty($install_state['parameters']['continue']))) {
    if ($install_state['interactive']) {
      drupal_set_title(st('Requirements problem'));
      $status_report = theme('status_report', array('requirements' => $requirements));
      $status_report .= st('Check the error messages and <a href="!url">proceed with the installation</a>.', array('!url' => check_url(drupal_requirements_url($severity))));
      return $status_report;
    }
    else {
      // Throw an exception showing any unmet requirements.
      $failures = array();
      foreach ($requirements as $requirement) {
        // Skip warnings altogether for non-interactive installations; these
        // proceed in a single request so there is no good opportunity (and no
        // good method) to warn the user anyway.
        if (isset($requirement['severity']) && $requirement['severity'] == REQUIREMENT_ERROR) {
          $failures[] = $requirement['title'] . ': ' . $requirement['value'] . "\n\n" . $requirement['description'];
        }
      }
      if (!empty($failures)) {
        throw new Exception(implode("\n\n", $failures));
      }
    }
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
