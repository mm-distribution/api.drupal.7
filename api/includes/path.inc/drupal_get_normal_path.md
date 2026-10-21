# drupal_get_normal_path()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 259–276 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L259-L276)

## Signature

```php
function drupal_get_normal_path($path, $path_language = NULL)
```

## Documentation

```text
Given a path alias, return the internal path it represents.

@param $path
  A Drupal path alias.
@param $path_language
  An optional language code to look up the path in.

@return
  The internal path represented by the alias, or the original alias if no
  internal path was found.
```

## Code

```php
function drupal_get_normal_path($path, $path_language = NULL) {
  $original_path = $path;

  // Lookup the path alias first.
  if ($source = drupal_lookup_path('source', $path, $path_language)) {
    $path = $source;
  }

  // Allow other modules to alter the inbound URL. We cannot use drupal_alter()
  // here because we need to run hook_url_inbound_alter() in the reverse order
  // of hook_url_outbound_alter().
  foreach (array_reverse(module_implements('url_inbound_alter')) as $module) {
    $function = $module . '_url_inbound_alter';
    $function($path, $original_path, $path_language);
  }

  return $path;
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
