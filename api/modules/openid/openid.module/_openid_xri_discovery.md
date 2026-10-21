# _openid_xri_discovery()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 463–485 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L463-L485)
- **Module/theme:** openid

## Signature

```php
function _openid_xri_discovery($claimed_id)
```

## Documentation

```text
OpenID discovery method: perform an XRI discovery.

@see http://openid.net/specs/openid-authentication-2_0.html#discovery
@see hook_openid_discovery_method_info()
@see openid_discovery()

@return
  An array of discovered services and claimed identifier or NULL. See
  openid_discovery() for more specific information.
```

## Code

```php
function _openid_xri_discovery($claimed_id) {
  if (_openid_is_xri($claimed_id)) {
    // Resolve XRI using a proxy resolver (Extensible Resource Identifier (XRI)
    // Resolution Version 2.0, section 11.2 and 14.3).
    $xrds_url = variable_get('xri_proxy_resolver', 'http://xri.net/') . rawurlencode($claimed_id) . '?_xrd_r=application/xrds+xml';
    $discovery = _openid_xrds_discovery($xrds_url);
    if (!empty($discovery['services']) && is_array($discovery['services'])) {
      foreach ($discovery['services'] as $i => &$service) {
        $status = $service['xrd']->children(OPENID_NS_XRD)->Status;
        if ($status && $status->attributes()->cid == 'verified') {
          $service['claimed_id'] = openid_normalize((string)$service['xrd']->children(OPENID_NS_XRD)->CanonicalID);
        }
        else {
          // Ignore service if the Canonical ID could not be verified.
          unset($discovery['services'][$i]);
        }
      }
      if (!empty($discovery['services'])) {
        return $discovery;
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
