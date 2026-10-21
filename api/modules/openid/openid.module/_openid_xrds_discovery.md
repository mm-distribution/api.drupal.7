# _openid_xrds_discovery()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 498–572 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L498-L572)
- **Module/theme:** openid

## Signature

```php
function _openid_xrds_discovery($claimed_id)
```

## Documentation

```text
OpenID discovery method: perform a XRDS discovery.

@see http://openid.net/specs/openid-authentication-2_0.html#discovery
@see hook_openid_discovery_method_info()
@see openid_discovery()

@return
  An array of discovered services and claimed identifier or NULL. See
  openid_discovery() for more specific information.
```

## Code

```php
function _openid_xrds_discovery($claimed_id) {
  $services = array();

  $xrds_url = $claimed_id;
  $scheme = @parse_url($xrds_url, PHP_URL_SCHEME);
  if ($scheme == 'http' || $scheme == 'https') {
    // For regular URLs, try Yadis resolution first, then HTML-based discovery
    $headers = array('Accept' => 'application/xrds+xml');
    $result = drupal_http_request($xrds_url, array('headers' => $headers));

    // Check for HTTP error and make sure, that we reach the target. If the
    // maximum allowed redirects are exhausted, final destination URL isn't
    // reached, but drupal_http_request() doesn't return any error.
    // @todo Remove the check for 200 HTTP result code after the following issue
    // will be fixed: http://drupal.org/node/1096890.
    if (!isset($result->error) && $result->code == 200) {

      // Replace the user-entered claimed_id if we received a redirect.
      if (!empty($result->redirect_url)) {
        $claimed_id = openid_normalize($result->redirect_url);
      }

      if (isset($result->headers['content-type']) && preg_match("/application\/xrds\+xml/", $result->headers['content-type'])) {
        // Parse XML document to find URL
        $services = _openid_xrds_parse($result->data);
      }
      else {
        $xrds_url = NULL;
        if (isset($result->headers['x-xrds-location'])) {
          $xrds_url = $result->headers['x-xrds-location'];
        }
        else {
          // Look for meta http-equiv link in HTML head
          $xrds_url = _openid_meta_httpequiv('X-XRDS-Location', $result->data);
        }
        if (!empty($xrds_url)) {
          $headers = array('Accept' => 'application/xrds+xml');
          $xrds_result = drupal_http_request($xrds_url, array('headers' => $headers));
          if (!isset($xrds_result->error)) {
            $services = _openid_xrds_parse($xrds_result->data);
          }
        }
      }

      // Check for HTML delegation
      if (count($services) == 0) {
        // Look for 2.0 links
        $uri = _openid_link_href('openid2.provider', $result->data);
        $identity = _openid_link_href('openid2.local_id', $result->data);
        $type = 'http://specs.openid.net/auth/2.0/signon';

        // 1.x links
        if (empty($uri)) {
          $uri = _openid_link_href('openid.server', $result->data);
          $identity = _openid_link_href('openid.delegate', $result->data);
          $type = 'http://openid.net/signon/1.1';
        }
        if (!empty($uri)) {
          $services[] = array(
            'uri' => $uri,
            'identity' => $identity,
            'types' => array($type),
          );
        }
      }
    }
  }

  if (!empty($services)) {
    return array(
      'services' => $services,
      'claimed_id' => $claimed_id,
    );
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
