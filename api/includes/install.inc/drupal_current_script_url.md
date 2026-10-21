# drupal_current_script_url()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1074–1081 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1074-L1081)

## Signature

```php
function drupal_current_script_url($query = array())
```

## Documentation

```text
Returns the URL of the current script, with modified query parameters.

This function can be called by low-level scripts (such as install.php and
update.php) and returns the URL of the current script. Existing query
parameters are preserved by default, but new ones can optionally be merged
in.

This function is used when the script must maintain certain query parameters
over multiple page requests in order to work correctly. In such cases (for
example, update.php, which requires the 'continue=1' parameter to remain in
the URL throughout the update process if there are any requirement warnings
that need to be bypassed), using this function to generate the URL for links
to the next steps of the script ensures that the links will work correctly.

@param $query
  (optional) An array of query parameters to merge in to the existing ones.

@return
  The URL of the current script, with query parameters modified by the
  passed-in $query. The URL is not sanitized, so it still needs to be run
  through check_url() if it will be used as an HTML attribute value.

@see drupal_requirements_url()
```

## Code

```php
function drupal_current_script_url($query = array()) {
  $uri = $_SERVER['SCRIPT_NAME'];
  $query = array_merge(drupal_get_query_parameters(), $query);
  if (!empty($query)) {
    $uri .= '?' . drupal_http_build_query($query);
  }
  return $uri;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
