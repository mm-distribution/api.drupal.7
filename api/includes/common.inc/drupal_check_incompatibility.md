# drupal_check_incompatibility()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8003–8011 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8003-L8011)

## Signature

```php
function drupal_check_incompatibility($v, $current_version)
```

## Documentation

```text
Checks whether a version is compatible with a given dependency.

@param $v
  The parsed dependency structure from drupal_parse_dependency().
@param $current_version
  The version to check against (like 4.2).

@return
  NULL if compatible, otherwise the original dependency version string that
  caused the incompatibility.

@see drupal_parse_dependency()
```

## Code

```php
function drupal_check_incompatibility($v, $current_version) {
  if (!empty($v['versions'])) {
    foreach ($v['versions'] as $required_version) {
      if ((isset($required_version['op']) && !version_compare($current_version, $required_version['version'], $required_version['op']))) {
        return $v['original_version'];
      }
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
