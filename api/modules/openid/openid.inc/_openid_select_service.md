# _openid_select_service()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 216–258 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L216-L258)
- **Module/theme:** openid

## Signature

```php
function _openid_select_service(array $services)
```

## Documentation

```text
Select a service element.

The procedure is described in OpenID Authentication 2.0, section 7.3.2.

A new entry is added to the returned array with the key 'version' and the
value 1 or 2 specifying the protocol version used by the service.

@param $services
  An array of service arrays as returned by openid_discovery().
@return
  The selected service array, or NULL if no valid services were found.
```

## Code

```php
function _openid_select_service(array $services) {
  // Extensible Resource Identifier (XRI) Resolution Version 2.0, section 4.3.3:
  // Find the service with the highest priority (lowest integer value). If there
  // is a tie, select a random one, not just the first in the XML document.
  shuffle($services);
  $selected_service = NULL;
  $selected_type_priority = FALSE;

  // Search for an OP Identifier Element.
  foreach ($services as $service) {
    if (!empty($service['uri'])) {
      $type_priority = FALSE;
      if (in_array('http://specs.openid.net/auth/2.0/server', $service['types'])) {
        $service['version'] = 2;
        $type_priority = 1;
      }
      elseif (in_array('http://specs.openid.net/auth/2.0/signon', $service['types'])) {
        $service['version'] = 2;
        $type_priority = 2;
      }
      elseif (in_array(OPENID_NS_1_0, $service['types']) || in_array(OPENID_NS_1_1, $service['types'])) {
        $service['version'] = 1;
        $type_priority = 3;
      }

      if ($type_priority
          && (!$selected_service
              || $type_priority < $selected_type_priority
              || ($type_priority == $selected_type_priority && $service['priority'] < $selected_service['priority']))) {
        $selected_service = $service;
        $selected_type_priority = $type_priority;
      }
    }
  }

  if ($selected_service) {
    // Unset SimpleXMLElement instances that cannot be saved in $_SESSION.
    unset($selected_service['xrd']);
    unset($selected_service['service']);
  }

  return $selected_service;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
