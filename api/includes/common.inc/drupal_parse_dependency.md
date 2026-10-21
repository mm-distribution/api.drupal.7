# drupal_parse_dependency()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7944–7987 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7944-L7987)

## Signature

```php
function drupal_parse_dependency($dependency)
```

## Documentation

```text
Parses a dependency for comparison by drupal_check_incompatibility().

@param $dependency
  A dependency string, which specifies a module dependency, and optionally
  the project it comes from and versions that are supported. Supported
  formats include:
  - 'module'
  - 'project:module'
  - 'project:module (>=version, version)'

@return
  An associative array with three keys:
  - 'name' includes the name of the thing to depend on (e.g. 'foo').
  - 'original_version' contains the original version string (which can be
    used in the UI for reporting incompatibilities).
  - 'versions' is a list of associative arrays, each containing the keys
    'op' and 'version'. 'op' can be one of: '=', '==', '!=', '<>', '<',
    '<=', '>', or '>='. 'version' is one piece like '4.5-beta3'.
  Callers should pass this structure to drupal_check_incompatibility().

@see drupal_check_incompatibility()
```

## Code

```php
function drupal_parse_dependency($dependency) {
  $value = array();
  // Split out the optional project name.
  if (strpos($dependency, ':')) {
    list($project_name, $dependency) = explode(':', $dependency);
    $value['project'] = $project_name;
  }
  // We use named subpatterns and support every op that version_compare
  // supports. Also, op is optional and defaults to equals.
  $p_op = '(?P<operation>!=|==|=|<|<=|>|>=|<>)?';
  // Core version is always optional: 7.x-2.x and 2.x is treated the same.
  $p_core = '(?:' . preg_quote(DRUPAL_CORE_COMPATIBILITY) . '-)?';
  $p_major = '(?P<major>\d+)';
  // By setting the minor version to x, branches can be matched.
  $p_minor = '(?P<minor>(?:\d+|x)(?:-[A-Za-z]+\d+)?)';
  $parts = explode('(', $dependency, 2);
  $value['name'] = trim($parts[0]);
  if (isset($parts[1])) {
    $value['original_version'] = ' (' . $parts[1];
    foreach (explode(',', $parts[1]) as $version) {
      if (preg_match("/^\s*$p_op\s*$p_core$p_major\.$p_minor/", $version, $matches)) {
        $op = !empty($matches['operation']) ? $matches['operation'] : '=';
        if ($matches['minor'] == 'x') {
          // Drupal considers "2.x" to mean any version that begins with
          // "2" (e.g. 2.0, 2.9 are all "2.x"). PHP's version_compare(),
          // on the other hand, treats "x" as a string; so to
          // version_compare(), "2.x" is considered less than 2.0. This
          // means that >=2.x and <2.x are handled by version_compare()
          // as we need, but > and <= are not.
          if ($op == '>' || $op == '<=') {
            $matches['major']++;
          }
          // Equivalence can be checked by adding two restrictions.
          if ($op == '=' || $op == '==') {
            $value['versions'][] = array('op' => '<', 'version' => ($matches['major'] + 1) . '.x');
            $op = '>=';
          }
        }
        $value['versions'][] = array('op' => $op, 'version' => $matches['major'] . '.' . $matches['minor']);
      }
    }
  }
  return $value;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
