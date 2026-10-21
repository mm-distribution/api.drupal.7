# url()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2300–2421 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2300-L2421)

## Signature

```php
function url($path = NULL, array $options = array())
```

## Documentation

```text
Generates an internal or external URL.

When creating links in modules, consider whether l() could be a better
alternative than url().

@param $path
  (optional) The internal path or external URL being linked to, such as
  "node/34" or "http://example.com/foo". The default value is equivalent to
  passing in '<front>'. A few notes:
  - If you provide a full URL, it will be considered an external URL.
  - If you provide only the path (e.g. "node/34"), it will be
    considered an internal link. In this case, it should be a system URL,
    and it will be replaced with the alias, if one exists. Additional query
    arguments for internal paths must be supplied in $options['query'], not
    included in $path.
  - If you provide an internal path and $options['alias'] is set to TRUE, the
    path is assumed already to be the correct path alias, and the alias is
    not looked up.
  - The special string '<front>' generates a link to the site's base URL.
  - If your external URL contains a query (e.g. http://example.com/foo?a=b),
    then you can either URL encode the query keys and values yourself and
    include them in $path, or use $options['query'] to let this function
    URL encode them.
@param $options
  (optional) An associative array of additional options, with the following
  elements:
  - 'query': An array of query key/value-pairs (without any URL-encoding) to
    append to the URL.
  - 'fragment': A fragment identifier (named anchor) to append to the URL.
    Do not include the leading '#' character.
  - 'absolute': Defaults to FALSE. Whether to force the output to be an
    absolute link (beginning with http:). Useful for links that will be
    displayed outside the site, such as in an RSS feed.
  - 'alias': Defaults to FALSE. Whether the given path is a URL alias
    already.
  - 'external': Whether the given path is an external URL.
  - 'language': An optional language object. If the path being linked to is
    internal to the site, $options['language'] is used to look up the alias
    for the URL. If $options['language'] is omitted, the global $language_url
    will be used.
  - 'https': Whether this URL should point to a secure location. If not
    defined, the current scheme is used, so the user stays on HTTP or HTTPS
    respectively. TRUE enforces HTTPS and FALSE enforces HTTP, but HTTPS can
    only be enforced when the variable 'https' is set to TRUE.
  - 'base_url': Only used internally, to modify the base URL when a language
    dependent URL requires so.
  - 'prefix': Only used internally, to modify the path when a language
    dependent URL requires so.
  - 'script': The script filename in Drupal's root directory to use when
    clean URLs are disabled, such as 'index.php'. Defaults to an empty
    string, as most modern web servers automatically find 'index.php'. If
    clean URLs are disabled, the value of $path is appended as query
    parameter 'q' to $options['script'] in the returned URL. When deploying
    Drupal on a web server that cannot be configured to automatically find
    index.php, then hook_url_outbound_alter() can be implemented to force
    this value to 'index.php'.
  - 'entity_type': The entity type of the object that called url(). Only
    set if url() is invoked by entity_uri().
  - 'entity': The entity object (such as a node) for which the URL is being
    generated. Only set if url() is invoked by entity_uri().

@return
  A string containing a URL to the given path.
```

## Code

```php
function url($path = NULL, array $options = array()) {
  // Merge in defaults.
  $options += array(
    'fragment' => '',
    'query' => array(),
    'absolute' => FALSE,
    'alias' => FALSE,
    'prefix' => ''
  );

  // Determine whether this is an external link, but ensure that the current
  // path is always treated as internal by default (to prevent external link
  // injection vulnerabilities).
  if (!isset($options['external'])) {
    $options['external'] = $path === $_GET['q'] ? FALSE : url_is_external($path);
  }

  // Preserve the original path before altering or aliasing.
  $original_path = $path;

  // Allow other modules to alter the outbound URL and options.
  drupal_alter('url_outbound', $path, $options, $original_path);

  if (isset($options['fragment']) && $options['fragment'] !== '') {
    $options['fragment'] = '#' . $options['fragment'];
  }

  if ($options['external']) {
    // Split off the fragment.
    if (strpos($path, '#') !== FALSE) {
      list($path, $old_fragment) = explode('#', $path, 2);
      // If $options contains no fragment, take it over from the path.
      if (isset($old_fragment) && !$options['fragment']) {
        $options['fragment'] = '#' . $old_fragment;
      }
    }
    // Append the query.
    if ($options['query']) {
      $path .= (strpos($path, '?') !== FALSE ? '&' : '?') . drupal_http_build_query($options['query']);
    }
    if (isset($options['https']) && variable_get('https', FALSE)) {
      if ($options['https'] === TRUE) {
        $path = str_replace('http://', 'https://', $path);
      }
      elseif ($options['https'] === FALSE) {
        $path = str_replace('https://', 'http://', $path);
      }
    }
    // Reassemble.
    return $path . $options['fragment'];
  }

  // Strip leading slashes from internal paths to prevent them becoming external
  // URLs without protocol. /example.com should not be turned into
  // //example.com.
  $path = ltrim((string) $path, '/');

  global $base_url, $base_secure_url, $base_insecure_url;

  // The base_url might be rewritten from the language rewrite in domain mode.
  if (!isset($options['base_url'])) {
    if (isset($options['https']) && variable_get('https', FALSE)) {
      if ($options['https'] === TRUE) {
        $options['base_url'] = $base_secure_url;
        $options['absolute'] = TRUE;
      }
      elseif ($options['https'] === FALSE) {
        $options['base_url'] = $base_insecure_url;
        $options['absolute'] = TRUE;
      }
    }
    else {
      $options['base_url'] = $base_url;
    }
  }

  // The special path '<front>' links to the default front page.
  if ($path == '<front>') {
    $path = '';
  }
  elseif (!empty($path) && !$options['alias']) {
    $language = isset($options['language']) && isset($options['language']->language) ? $options['language']->language : '';
    require_once DRUPAL_ROOT . '/' . variable_get('path_inc', 'includes/path.inc');
    $alias = drupal_get_path_alias($original_path, $language);
    if ($alias != $original_path) {
      // Strip leading slashes from internal path aliases to prevent them
      // becoming external URLs without protocol. /example.com should not be
      // turned into //example.com.
      $path = ltrim($alias, '/');
    }
  }

  $base = $options['absolute'] ? $options['base_url'] . '/' : base_path();
  $prefix = empty($path) ? rtrim((string) $options['prefix'], '/') : $options['prefix'];

  // With Clean URLs.
  if (!empty($GLOBALS['conf']['clean_url'])) {
    $path = drupal_encode_path($prefix . $path);
    if ($options['query']) {
      return $base . $path . '?' . drupal_http_build_query($options['query']) . $options['fragment'];
    }
    else {
      return $base . $path . $options['fragment'];
    }
  }
  // Without Clean URLs.
  else {
    $path = $prefix . $path;
    $query = array();
    if (!empty($path)) {
      $query['q'] = $path;
    }
    if ($options['query']) {
      // We do not use array_merge() here to prevent overriding $path via query
      // parameters.
      $query += $options['query'];
    }
    $query = $query ? ('?' . drupal_http_build_query($query)) : '';
    $script = isset($options['script']) ? $options['script'] : '';
    return $base . $script . $query . $options['fragment'];
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
