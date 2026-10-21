# _update_process_fetch_task()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 133–199 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L133-L199)
- **Module/theme:** update

## Signature

```php
function _update_process_fetch_task($project)
```

## Documentation

```text
Processes a task to fetch available update data for a single project.

Once the release history XML data is downloaded, it is parsed and saved into
the {cache_update} table in an entry just for that project.

@param $project
  Associative array of information about the project to fetch data for.

@return
  TRUE if we fetched parsable XML, otherwise FALSE.
```

## Code

```php
function _update_process_fetch_task($project) {
  global $base_url;
  $fail = &drupal_static(__FUNCTION__, array());
  // This can be in the middle of a long-running batch, so REQUEST_TIME won't
  // necessarily be valid.
  $now = time();
  if (empty($fail)) {
    // If we have valid data about release history XML servers that we have
    // failed to fetch from on previous attempts, load that from the cache.
    if (($cache = _update_cache_get('fetch_failures')) && ($cache->expire > $now)) {
      $fail = $cache->data;
    }
  }

  $max_fetch_attempts = variable_get('update_max_fetch_attempts', UPDATE_MAX_FETCH_ATTEMPTS);

  $success = FALSE;
  $available = array();
  $site_key = drupal_hmac_base64($base_url, drupal_get_private_key());
  $url = _update_build_fetch_url($project, $site_key);
  $fetch_url_base = _update_get_fetch_url_base($project);
  $project_name = $project['name'];

  if (empty($fail[$fetch_url_base]) || $fail[$fetch_url_base] < $max_fetch_attempts) {
    $xml = drupal_http_request($url);
    if (isset($xml->error)) {
      watchdog('update', 'Error %errorcode (%message) occurred when trying to fetch available update data for the project %project.', array('%errorcode' => $xml->code, '%message' => $xml->error, '%project' => $project_name), WATCHDOG_ERROR);
    }
    if (!isset($xml->error) && isset($xml->data)) {
      $data = $xml->data;
    }
  }

  if (!empty($data)) {
    $available = update_parse_xml($data);
    // @todo: Purge release data we don't need (http://drupal.org/node/238950).
    if (!empty($available)) {
      // Only if we fetched and parsed something sane do we return success.
      $success = TRUE;
    }
  }
  else {
    $available['project_status'] = 'not-fetched';
    if (empty($fail[$fetch_url_base])) {
      $fail[$fetch_url_base] = 1;
    }
    else {
      $fail[$fetch_url_base]++;
    }
  }

  $frequency = variable_get('update_check_frequency', 1);
  $cid = 'available_releases::' . $project_name;
  _update_cache_set($cid, $available, $now + (60 * 60 * 24 * $frequency));

  // Stash the $fail data back in the DB for the next 5 minutes.
  _update_cache_set('fetch_failures', $fail, $now + (60 * 5));

  // Whether this worked or not, we did just (try to) check for updates.
  variable_set('update_last_check', $now);

  // Now that we processed the fetch task for this project, clear out the
  // record in {cache_update} for this task so we're willing to fetch again.
  _update_cache_clear('fetch_task::' . $project_name);

  return $success;
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
