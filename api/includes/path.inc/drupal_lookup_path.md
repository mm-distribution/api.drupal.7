# drupal_lookup_path()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 45–193 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L45-L193)

## Signature

```php
function drupal_lookup_path($action, $path = '', $path_language = NULL)
```

## Documentation

```text
Given an alias, return its Drupal system URL if one exists. Given a Drupal
system URL return one of its aliases if such a one exists. Otherwise,
return FALSE.

@param $action
  One of the following values:
  - wipe: delete the alias cache.
  - alias: return an alias for a given Drupal system path (if one exists).
  - source: return the Drupal system URL for a path alias (if one exists).
@param $path
  The path to investigate for corresponding aliases or system URLs.
@param $path_language
  Optional language code to search the path with. Defaults to the page language.
  If there's no path defined for that language it will search paths without
  language.

@return
  Either a Drupal system path, an aliased path, or FALSE if no path was
  found.
```

## Code

```php
function drupal_lookup_path($action, $path = '', $path_language = NULL) {
  global $language_url;
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['cache'] = &drupal_static(__FUNCTION__);
  }
  $cache = &$drupal_static_fast['cache'];

  if (!isset($cache)) {
    $cache = array(
      'map' => array(),
      'no_source' => array(),
      'whitelist' => NULL,
      'system_paths' => array(),
      'no_aliases' => array(),
      'first_call' => TRUE,
    );
  }

  // Retrieve the path alias whitelist.
  if (!isset($cache['whitelist'])) {
    $cache['whitelist'] = variable_get('path_alias_whitelist', NULL);
    if (!isset($cache['whitelist'])) {
      $cache['whitelist'] = drupal_path_alias_whitelist_rebuild();
    }
  }

  // If no language is explicitly specified we default to the current URL
  // language. If we used a language different from the one conveyed by the
  // requested URL, we might end up being unable to check if there is a path
  // alias matching the URL path.
  $path_language = $path_language ? $path_language : $language_url->language;

  if ($action == 'wipe') {
    $cache = array();
    $cache['whitelist'] = drupal_path_alias_whitelist_rebuild();
  }
  elseif ($cache['whitelist'] && $path != '') {
    if ($action == 'alias') {
      // During the first call to drupal_lookup_path() per language, load the
      // expected system paths for the page from cache.
      if (!empty($cache['first_call'])) {
        $cache['first_call'] = FALSE;

        $cache['map'][$path_language] = array();
        // Load system paths from cache.
        $cid = current_path();
        if ($cached = cache_get($cid, 'cache_path')) {
          $cache['system_paths'] = $cached->data;
          // Now fetch the aliases corresponding to these system paths.
          $args = array(
            ':system' => $cache['system_paths'],
            ':language' => $path_language,
            ':language_none' => LANGUAGE_NONE,
          );
          // Always get the language-specific alias before the language-neutral
          // one. For example 'de' is less than 'und' so the order needs to be
          // ASC, while 'xx-lolspeak' is more than 'und' so the order needs to
          // be DESC. We also order by pid ASC so that fetchAllKeyed() returns
          // the most recently created alias for each source. Subsequent queries
          // using fetchField() must use pid DESC to have the same effect.
          // For performance reasons, the query builder is not used here.
          if ($path_language == LANGUAGE_NONE) {
            // Prevent PDO from complaining about a token the query doesn't use.
            unset($args[':language']);
            $result = db_query('SELECT source, alias FROM {url_alias} WHERE source IN (:system) AND language = :language_none ORDER BY pid ASC', $args);
          }
          elseif ($path_language < LANGUAGE_NONE) {
            $result = db_query('SELECT source, alias FROM {url_alias} WHERE source IN (:system) AND language IN (:language, :language_none) ORDER BY language ASC, pid ASC', $args);
          }
          else {
            $result = db_query('SELECT source, alias FROM {url_alias} WHERE source IN (:system) AND language IN (:language, :language_none) ORDER BY language DESC, pid ASC', $args);
          }
          $cache['map'][$path_language] = $result->fetchAllKeyed();
          // Keep a record of paths with no alias to avoid querying twice.
          $cache['no_aliases'][$path_language] = array_flip(array_diff_key($cache['system_paths'], array_keys($cache['map'][$path_language])));
        }
      }
      // If the alias has already been loaded, return it.
      if (isset($cache['map'][$path_language][$path])) {
        return $cache['map'][$path_language][$path];
      }
      // Check the path whitelist, if the top_level part before the first /
      // is not in the list, then there is no need to do anything further,
      // it is not in the database.
      elseif (!isset($cache['whitelist'][strtok($path, '/')])) {
        return FALSE;
      }
      // For system paths which were not cached, query aliases individually.
      elseif (!isset($cache['no_aliases'][$path_language][$path])) {
        $args = array(
          ':source' => $path,
          ':language' => $path_language,
          ':language_none' => LANGUAGE_NONE,
        );
        // See the queries above.
        if ($path_language == LANGUAGE_NONE) {
          unset($args[':language']);
          $alias = db_query("SELECT alias FROM {url_alias} WHERE source = :source AND language = :language_none ORDER BY pid DESC", $args)->fetchField();
        }
        elseif ($path_language > LANGUAGE_NONE) {
          $alias = db_query("SELECT alias FROM {url_alias} WHERE source = :source AND language IN (:language, :language_none) ORDER BY language DESC, pid DESC", $args)->fetchField();
        }
        else {
          $alias = db_query("SELECT alias FROM {url_alias} WHERE source = :source AND language IN (:language, :language_none) ORDER BY language ASC, pid DESC", $args)->fetchField();
        }
        $cache['map'][$path_language][$path] = $alias;
        return $alias;
      }
    }
    // Check $no_source for this $path in case we've already determined that there
    // isn't a path that has this alias
    elseif ($action == 'source' && !isset($cache['no_source'][$path_language][$path])) {
      // Look for the value $path within the cached $map
      $source = FALSE;
      if (!isset($cache['map'][$path_language]) || !($source = array_search($path, $cache['map'][$path_language]))) {
        $args = array(
          ':alias' => $path,
          ':language' => $path_language,
          ':language_none' => LANGUAGE_NONE,
        );
        // See the queries above.
        if ($path_language == LANGUAGE_NONE) {
          unset($args[':language']);
          $result = db_query("SELECT source FROM {url_alias} WHERE alias = :alias AND language = :language_none ORDER BY pid DESC", $args);
        }
        elseif ($path_language > LANGUAGE_NONE) {
          $result = db_query("SELECT source FROM {url_alias} WHERE alias = :alias AND language IN (:language, :language_none) ORDER BY language DESC, pid DESC", $args);
        }
        else {
          $result = db_query("SELECT source FROM {url_alias} WHERE alias = :alias AND language IN (:language, :language_none) ORDER BY language ASC, pid DESC", $args);
        }
        if ($source = $result->fetchField()) {
          $cache['map'][$path_language][$source] = $path;
        }
        else {
          // We can't record anything into $map because we do not have a valid
          // index and there is no need because we have not learned anything
          // about any Drupal path. Thus cache to $no_source.
          $cache['no_source'][$path_language][$path] = TRUE;
        }
      }
      return $source;
    }
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
