# path_to_theme()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1227–1235 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1227-L1235)

## Signature

```php
function path_to_theme()
```

## Documentation

```text
Returns the path to the current themed element.

It can point to the active theme or the module handling a themed
implementation. For example, when invoked within the scope of a theming call
it will depend on where the theming function is handled. If implemented from
a module, it will point to the module. If implemented from the active theme,
it will point to the active theme. When called outside the scope of a
theming call, it will always point to the active theme.
```

## Code

```php
function path_to_theme() {
  global $theme_path;

  if (!isset($theme_path)) {
    drupal_theme_initialize();
  }

  return $theme_path;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
