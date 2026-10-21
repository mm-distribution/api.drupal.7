# drupal_parse_info_file()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7667–7680 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7667-L7680)

## Signature

```php
function drupal_parse_info_file($filename)
```

## Documentation

```text
Parses Drupal module and theme .info files.

Info files are NOT for placing arbitrary theme and module-specific settings.
Use variable_get() and variable_set() for that.

Information stored in a module .info file:
- name: The real name of the module for display purposes.
- description: A brief description of the module.
- dependencies: An array of dependency strings. Each is in the form
  'project:module (versions)'; with the following meanings:
  - project: (optional) Project shortname, recommended to ensure uniqueness,
    if the module is part of a project hosted on drupal.org. If omitted,
    also omit the : that follows. The project name is currently ignored by
    Drupal core but is used for automated testing.
  - module: (required) Module shortname within the project.
  - (versions): Optional version information, consisting of one or more
    comma-separated operator/value pairs or simply version numbers, which
    can contain "x" as a wildcard. Examples: (>=7.22, <7.28), (7.x-3.x).
- package: The name of the package of modules this module belongs to.

See forum.info for an example of a module .info file.

Information stored in a theme .info file:
- name: The real name of the theme for display purposes.
- description: Brief description.
- screenshot: Path to screenshot relative to the theme's .info file.
- engine: Theme engine; typically phptemplate.
- base: Name of a base theme, if applicable; e.g., base = zen.
- regions: Listed regions; e.g., region[left] = Left sidebar.
- features: Features available; e.g., features[] = logo.
- stylesheets: Theme stylesheets; e.g., stylesheets[all][] = my-style.css.
- scripts: Theme scripts; e.g., scripts[] = my-script.js.

See bartik.info for an example of a theme .info file.

@param $filename
  The file we are parsing. Accepts file with relative or absolute path.

@return
  The info array.

@see drupal_parse_info_format()
```

## Code

```php
function drupal_parse_info_file($filename) {
  $info = &drupal_static(__FUNCTION__, array());

  if (!isset($info[$filename])) {
    if (!file_exists($filename)) {
      $info[$filename] = array();
    }
    else {
      $data = file_get_contents($filename);
      $info[$filename] = drupal_parse_info_format($data);
    }
  }
  return $info[$filename];
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
