# drupal_requirements_url()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1101–1109 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1101-L1109)

## Signature

```php
function drupal_requirements_url($severity)
```

## Documentation

```text
Returns a URL for proceeding to the next page after a requirements problem.

This function can be called by low-level scripts (such as install.php and
update.php) and returns a URL that can be used to attempt to proceed to the
next step of the script.

@param $severity
  The severity of the requirements problem, as returned by
  drupal_requirements_severity().

@return
  A URL for attempting to proceed to the next step of the script. The URL is
  not sanitized, so it still needs to be run through check_url() if it will
  be used as an HTML attribute value.

@see drupal_current_script_url()
```

## Code

```php
function drupal_requirements_url($severity) {
  $query = array();
  // If there are no errors, only warnings, append 'continue=1' to the URL so
  // the user can bypass this screen on the next page load.
  if ($severity == REQUIREMENT_WARNING) {
    $query['continue'] = 1;
  }
  return drupal_current_script_url($query);
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
