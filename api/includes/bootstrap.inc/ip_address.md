# ip_address()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3301–3340 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3301-L3340)

## Signature

```php
function ip_address()
```

## Documentation

```text
Returns the IP address of the client machine.

If Drupal is behind a reverse proxy, we use the X-Forwarded-For header
instead of $_SERVER['REMOTE_ADDR'], which would be the IP address of
the proxy server, and not the client's. The actual header name can be
configured by the reverse_proxy_header variable.

@return
  IP address of client machine, adjusted for reverse proxy and/or cluster
  environments.
```

## Code

```php
function ip_address() {
  $ip_address = &drupal_static(__FUNCTION__);

  if (!isset($ip_address)) {
    $ip_address = $_SERVER['REMOTE_ADDR'];

    if (variable_get('reverse_proxy', 0)) {
      $reverse_proxy_header = variable_get('reverse_proxy_header', 'HTTP_X_FORWARDED_FOR');
      if (!empty($_SERVER[$reverse_proxy_header])) {
        // If an array of known reverse proxy IPs is provided, then trust
        // the XFF header if request really comes from one of them.
        $reverse_proxy_addresses = variable_get('reverse_proxy_addresses', array());

        // Turn XFF header into an array.
        $forwarded = explode(',', $_SERVER[$reverse_proxy_header]);

        // Trim the forwarded IPs; they may have been delimited by commas and spaces.
        $forwarded = array_map('trim', $forwarded);

        // Tack direct client IP onto end of forwarded array.
        $forwarded[] = $ip_address;

        // Eliminate all trusted IPs.
        $untrusted = array_diff($forwarded, $reverse_proxy_addresses);

        if (!empty($untrusted)) {
          // The right-most IP is the most specific we can trust.
          $ip_address = array_pop($untrusted);
        }
        else {
          // All IP addresses in the forwarded array are configured proxy IPs
          // (and thus trusted). We take the leftmost IP.
          $ip_address = array_shift($forwarded);
        }
      }
    }
  }

  return $ip_address;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
