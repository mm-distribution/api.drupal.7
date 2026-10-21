# openid_verify_assertion_nonce()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 945–990 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L945-L990)
- **Module/theme:** openid

## Signature

```php
function openid_verify_assertion_nonce($service, $response)
```

## Documentation

```text
Verify that the nonce has not been used in earlier assertions from the same OpenID provider.

@param $service
  Array describing the OpenID provider.
@param $response
  Array of response values from the provider.

@return
  TRUE if the nonce has not expired and has not been used earlier.
```

## Code

```php
function openid_verify_assertion_nonce($service, $response) {
  if ($service['version'] != 2) {
    return TRUE;
  }

  if (preg_match('/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})Z/', $response['openid.response_nonce'], $matches)) {
    list(, $year, $month, $day, $hour, $minutes, $seconds) = $matches;
    $nonce_timestamp = gmmktime($hour, $minutes, $seconds, $month, $day, $year);
  }
  else {
    watchdog('openid', 'Nonce from @endpoint rejected because it is not correctly formatted, nonce: @nonce.', array('@endpoint' => $service['uri'], '@nonce' => $response['openid.response_nonce']), WATCHDOG_WARNING);
    return FALSE;
  }

  // A nonce with a timestamp to far in the past or future will already have
  // been removed and cannot be checked for single use anymore.
  $time = time();
  $expiry = 900;
  if ($nonce_timestamp <= $time - $expiry || $nonce_timestamp >= $time + $expiry) {
    watchdog('openid', 'Nonce received from @endpoint is out of range (time difference: @intervals). Check possible clock skew.', array('@endpoint' => $service['uri'], '@interval' => $time - $nonce_timestamp), WATCHDOG_WARNING);
    return FALSE;
  }

  // Record that this nonce was used.
  db_insert('openid_nonce')
    ->fields(array(
      'idp_endpoint_uri' => $service['uri'],
      'nonce' => $response['openid.response_nonce'],
      'expires' => $nonce_timestamp + $expiry,
    ))
    ->execute();

  // Count the number of times this nonce was used.
  $count_used = db_query("SELECT COUNT(*) FROM {openid_nonce} WHERE nonce = :nonce AND idp_endpoint_uri = :idp_endpoint_uri", array(
    ':nonce' => $response['openid.response_nonce'],
    ':idp_endpoint_uri' => $service['uri'],
  ))->fetchField();

  if ($count_used == 1) {
    return TRUE;
  }
  else {
    watchdog('openid', 'Nonce replay attempt blocked from @ip, nonce: @nonce.', array('@ip' => ip_address(), '@nonce' => $response['openid.response_nonce']), WATCHDOG_CRITICAL);
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
