# drupal_requirements_severity()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1211–1219 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1211-L1219)

## Signature

```php
function drupal_requirements_severity(&$requirements)
```

## Documentation

```text
Extracts the highest severity from the requirements array.

@param $requirements
  An array of requirements, in the same format as is returned by
  hook_requirements().

@return
  The highest severity in the array.
```

## Code

```php
function drupal_requirements_severity(&$requirements) {
  $severity = REQUIREMENT_OK;
  foreach ($requirements as $requirement) {
    if (isset($requirement['severity'])) {
      $severity = max($severity, $requirement['severity']);
    }
  }
  return $severity;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
